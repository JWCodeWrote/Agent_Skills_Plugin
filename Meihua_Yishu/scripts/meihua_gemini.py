#!/usr/bin/env python3
"""
梅花易数 + Gemini 网页版 混合占卜系统
Meihua Yishu with Gemini Web (Chrome CDP)

使用 Chrome DevTools Protocol 连接已开启的 Gemini 网页，完全免费！

前置条件:
    1. 安装 websockets: pip install websockets
    2. 开启 Chrome 调试模式: chrome --remote-debugging-port=9222
    3. 手动打开 gemini.google.com 并登入

用法:
    python meihua_gemini.py --question "我这个项目能成功吗?" --numbers 5 27 42
    python meihua_gemini.py --question "今年财运如何?" --time
"""

import asyncio
import json
import subprocess
import sys
import argparse
from datetime import datetime
from typing import Optional, Dict

# 尝试导入 websockets
try:
    import websockets
except ImportError:
    print("❌ 请先安装 websockets: pip install websockets")
    sys.exit(1)

# 导入本地梅花易数计算模块
from meihua_calc import (
    qigua_by_numbers,
    qigua_by_gregorian_time,
    get_hexagram_strategy,
    STRATEGY_NEXT_STEPS,
    BAGUA,
    HEXAGRAMS
)


def find_gemini_page(pages):
    """从 Chrome 调试页面列表中找到 Gemini 页面"""
    for page in pages:
        if page.get("type") == "page" and "gemini.google.com" in page.get("url", ""):
            return page
    return None


async def send_to_gemini(ws_url: str, query_text: str, wait_seconds: int = 45) -> str:
    """
    通过 Chrome CDP 向 Gemini 发送查询并获取回应
    
    Args:
        ws_url: WebSocket 调试 URL
        query_text: 要发送的问题
        wait_seconds: 等待回应的秒数
    
    Returns:
        str: Gemini 的回应文本
    """
    async with websockets.connect(ws_url) as ws:
        # Step 1: 在输入框中输入文字
        # 需要转义特殊字符
        escaped_query = query_text.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
        
        input_js = f"""
        (function() {{
            // 尝试多种选择器找到输入框
            const editor = document.querySelector('div[contenteditable="true"]') 
                        || document.querySelector('rich-textarea div[contenteditable="true"]')
                        || document.querySelector('textarea')
                        || document.querySelector('.ql-editor');
            if (editor) {{
                editor.focus();
                // 清空现有内容
                editor.innerHTML = '';
                // 插入新文字
                document.execCommand('insertText', false, `{escaped_query}`);
                editor.dispatchEvent(new Event('input', {{bubbles: true}}));
                return 'input-ok';
            }}
            return 'editor-not-found';
        }})()
        """
        
        await ws.send(json.dumps({
            "id": 1, 
            "method": "Runtime.evaluate", 
            "params": {"expression": input_js}
        }))
        input_result = await ws.recv()
        input_data = json.loads(input_result)
        
        if input_data.get("result", {}).get("result", {}).get("value") == "editor-not-found":
            return "❌ 找不到 Gemini 输入框，请确认已打开 gemini.google.com"
        
        # 稍等一下让输入框更新
        await asyncio.sleep(0.5)
        
        # Step 2: 点击发送按钮
        click_js = """
        (function() {
            // 尝试多种选择器找到发送按钮
            const btn = document.querySelector('button[aria-label*="傳送"]')
                     || document.querySelector('button[aria-label*="Send"]')
                     || document.querySelector('button[aria-label*="发送"]')
                     || document.querySelector('button[type="submit"]')
                     || document.querySelector('button.send-button')
                     || document.querySelector('button[data-test-id="send-button"]');
            if (btn) { 
                btn.click(); 
                return 'clicked'; 
            }
            
            // 如果找不到按钮，尝试按 Enter
            const editor = document.querySelector('div[contenteditable="true"]');
            if (editor) {
                const enterEvent = new KeyboardEvent('keydown', {
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    which: 13,
                    bubbles: true
                });
                editor.dispatchEvent(enterEvent);
                return 'enter-pressed';
            }
            
            return 'button-not-found';
        })()
        """
        
        await ws.send(json.dumps({
            "id": 2, 
            "method": "Runtime.evaluate", 
            "params": {"expression": click_js}
        }))
        click_result = await ws.recv()
        
        # Step 3: 等待 Gemini 生成回应
        print(f"   ⏳ 等待 Gemini 回应 ({wait_seconds} 秒)...")
        await asyncio.sleep(wait_seconds)
        
        # Step 4: 提取回应内容
        extract_js = """
        (function() {
            // 尝试多种选择器找到回应内容
            const responses = document.querySelectorAll('.markdown')
                           || document.querySelectorAll('.response-content')
                           || document.querySelectorAll('[data-message-author-role="model"]');
            
            if (responses && responses.length > 0) {
                // 获取最后一个回应
                return responses[responses.length - 1].innerText;
            }
            
            // 备用：尝试获取任何看起来像回应的内容
            const modelMessages = document.querySelectorAll('.model-response-text');
            if (modelMessages && modelMessages.length > 0) {
                return modelMessages[modelMessages.length - 1].innerText;
            }
            
            return 'No response found';
        })()
        """
        
        await ws.send(json.dumps({
            "id": 3, 
            "method": "Runtime.evaluate", 
            "params": {"expression": extract_js}
        }))
        response = await ws.recv()
        result = json.loads(response)
        
        return result.get("result", {}).get("result", {}).get("value", "无法获取回应")


def build_gemini_prompt(hexagram_result: Dict, question: str) -> str:
    """构建发送给 Gemini 的 Prompt"""
    
    ben_gua = hexagram_result["本卦"]
    ti_yong = hexagram_result["体用"]
    hu_gua = hexagram_result["互卦"]
    bian_gua = hexagram_result["变卦"]
    
    # 获取策略建议
    hex_num = ben_gua['序号']
    strategy = get_hexagram_strategy(hex_num)
    
    strategy_text = ""
    if strategy:
        strategy_text = f"""
【策略统计】
类型: {strategy['type']}
建议: {strategy['advice']}
吉率: {strategy['ji_rate']}%
变卦路径: {strategy['change_path'] or '无需变卦'}
"""

    prompt = f"""你是一位精通《梅花易数》和《周易》的玄学大师。请根据以下卦象为用户解读。

【用户问题】{question}

【本卦】第{ben_gua['序号']}卦 {ben_gua['名称']}
上卦: {ben_gua['上卦']}
下卦: {ben_gua['下卦']}
动爻: {ben_gua['动爻']}

【体用分析】
体卦: {ti_yong['体卦']}
用卦: {ti_yong['用卦']}
生克关系: {ti_yong['生克关系']}

【互卦】{hu_gua['名称']}（代表事情发展过程）

【变卦】第{bian_gua['序号']}卦 {bian_gua['名称']}（代表最终结果）
{strategy_text}

请提供：
1. 卦象解读（传统易学含义）
2. 针对问题的具体分析
3. 时机判断（什么时候行动最好）
4. 行动建议（宜/忌）
5. 简短的鼓励或提醒

请用繁体中文回答，保持积极但务实的态度。"""

    return prompt


def hybrid_divination_cdp(
    question: str,
    numbers: Optional[list] = None,
    use_time: bool = False,
    wait_seconds: int = 45
) -> Dict:
    """
    混合占卜系统主函数 (Chrome CDP 模式)
    """
    result = {
        "question": question,
        "timestamp": datetime.now().isoformat(),
        "local_calculation": None,
        "strategy": None,
        "gemini_response": None,
        "errors": []
    }
    
    # Step 1: 本地算卦
    print("🔮 Step 1: 本地精准起卦...")
    try:
        if numbers and len(numbers) >= 2:
            num1, num2 = numbers[0], numbers[1]
            num3 = numbers[2] if len(numbers) > 2 else None
            hexagram_result = qigua_by_numbers(num1, num2, num3)
            result["method"] = f"数字起卦: {numbers}"
        else:
            now = datetime.now()
            hexagram_result = qigua_by_gregorian_time(now.year, now.month, now.day, now.hour)
            result["method"] = f"时间起卦: {now.strftime('%Y-%m-%d %H:%M')}"
        
        result["local_calculation"] = hexagram_result
        print(f"   ✅ 本卦: {hexagram_result['本卦']['名称']}")
        print(f"   ✅ 变卦: {hexagram_result['变卦']['名称']}")
        
    except Exception as e:
        result["errors"].append(f"本地算卦失败: {str(e)}")
        print(f"   ❌ 错误: {str(e)}")
        return result
    
    # Step 2: 获取策略建议
    print("📊 Step 2: 获取策略建议...")
    hex_num = hexagram_result["本卦"]["序号"]
    strategy = get_hexagram_strategy(hex_num)
    if strategy:
        result["strategy"] = {
            "type": strategy["type"],
            "advice": strategy["advice"],
            "ji_rate": strategy["ji_rate"],
            "change_path": strategy["change_path"],
            "next_step": STRATEGY_NEXT_STEPS.get(strategy["advice"], "")
        }
        print(f"   ✅ 类型: {strategy['type']} | 建议: {strategy['advice']} | 吉率: {strategy['ji_rate']}%")
    
    # Step 3: 连接 Gemini 网页
    print("🌐 Step 3: 连接 Gemini 网页...")
    try:
        # 获取 Chrome 调试页面列表
        curl_result = subprocess.run(
            ["curl", "-s", "http://localhost:9222/json"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if curl_result.returncode != 0:
            raise Exception("无法连接 Chrome 调试端口。请确认已执行: chrome --remote-debugging-port=9222")
        
        pages = json.loads(curl_result.stdout)
        gemini_page = find_gemini_page(pages)
        
        if not gemini_page:
            raise Exception("找不到 Gemini 页面。请在 Chrome 中打开 gemini.google.com")
        
        print(f"   ✅ 找到 Gemini 页面: {gemini_page['url'][:50]}...")
        
        # 构建 Prompt
        prompt = build_gemini_prompt(hexagram_result, question)
        
        # 发送到 Gemini
        print("🤖 Step 4: 向 Gemini 发送卦象...")
        gemini_response = asyncio.run(
            send_to_gemini(gemini_page["webSocketDebuggerUrl"], prompt, wait_seconds)
        )
        
        result["gemini_response"] = gemini_response
        print("   ✅ Gemini 回应完成")
        
    except subprocess.TimeoutExpired:
        result["errors"].append("连接 Chrome 超时")
        print("   ❌ 连接 Chrome 超时")
    except json.JSONDecodeError:
        result["errors"].append("Chrome 调试端口返回无效数据")
        print("   ❌ Chrome 调试端口返回无效数据")
    except Exception as e:
        result["errors"].append(str(e))
        print(f"   ⚠️ {str(e)}")
    
    return result


def print_full_result(result: Dict):
    """格式化输出完整结果"""
    print("\n" + "=" * 60)
    print("☯️ 梅花易数 × Gemini 网页版 混合占卜结果")
    print("=" * 60)
    
    print(f"\n【问题】{result['question']}")
    print(f"【方法】{result.get('method', '未知')}")
    print(f"【时间】{result['timestamp']}")
    
    if result["local_calculation"]:
        calc = result["local_calculation"]
        print("\n" + "-" * 40)
        print("📿 本地算卦结果")
        print("-" * 40)
        
        ben = calc["本卦"]
        print(f"\n【本卦】第 {ben['序号']} 卦：{ben['名称']}")
        print(f"  上卦: {ben['上卦']}")
        print(f"  下卦: {ben['下卦']}")
        print(f"  动爻: {ben['动爻']}")
        
        ty = calc["体用"]
        print(f"\n【体用分析】")
        print(f"  体卦: {ty['体卦']}")
        print(f"  用卦: {ty['用卦']}")
        print(f"  生克: {ty['生克关系']}")
        
        hu = calc["互卦"]
        print(f"\n【互卦】{hu['名称']}（过程）")
        
        bian = calc["变卦"]
        print(f"【变卦】第 {bian['序号']} 卦：{bian['名称']}（结果）")
    
    if result["strategy"]:
        s = result["strategy"]
        print("\n" + "-" * 40)
        print("📈 策略建议")
        print("-" * 40)
        print(f"  类型: {s['type']}")
        print(f"  建议: {s['advice']}")
        print(f"  吉率: {s['ji_rate']}%")
        if s['change_path']:
            print(f"  变卦路径: {s['change_path']}")
        print(f"\n{s['next_step']}")
    
    if result["gemini_response"]:
        print("\n" + "-" * 40)
        print("🤖 Gemini AI 深度解读")
        print("-" * 40)
        print(result["gemini_response"])
    
    if result["errors"]:
        print("\n" + "-" * 40)
        print("⚠️ 提示信息")
        print("-" * 40)
        for err in result["errors"]:
            print(f"  - {err}")
    
    print("\n" + "=" * 60)
    print("💡 声明：卦象仅供参考，最终决策请结合实际情况。")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="梅花易数 × Gemini 网页版 混合占卜系统（完全免费）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
前置条件:
  1. pip install websockets
  2. 开启 Chrome 调试模式:
     Windows: chrome --remote-debugging-port=9222
     Mac: /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222
  3. 在 Chrome 中打开 gemini.google.com 并登入

示例:
  python meihua_gemini.py --question "今年事业运势如何?"
  python meihua_gemini.py --question "这个项目能成功吗?" --numbers 5 27 42
  python meihua_gemini.py --question "感情问题" --time --wait 60
        """
    )
    
    parser.add_argument(
        "--question", "-q",
        type=str,
        required=True,
        help="你想问的问题"
    )
    
    parser.add_argument(
        "--numbers", "-n",
        type=int,
        nargs="+",
        help="起卦数字 (2-3个数字)"
    )
    
    parser.add_argument(
        "--time", "-t",
        action="store_true",
        help="使用当前时间起卦"
    )
    
    parser.add_argument(
        "--wait", "-w",
        type=int,
        default=45,
        help="等待 Gemini 回应的秒数 (默认 45)"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="输出 JSON 格式"
    )
    
    args = parser.parse_args()
    
    # 执行占卜
    result = hybrid_divination_cdp(
        question=args.question,
        numbers=args.numbers,
        use_time=args.time,
        wait_seconds=args.wait
    )
    
    # 输出结果
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_full_result(result)


if __name__ == "__main__":
    main()
