#!/usr/bin/env python3
"""
Bilibili Search Script - Yu Jie Daipai Edition
使用 browser-use 在 B 站搜索「大东北是我的家乡」

Usage:
    python search_bilibili.py [search_query]
    
Example:
    python search_bilibili.py "大东北是我的家乡"
"""

import subprocess
import sys
import urllib.parse


def search_bilibili(query="大东北是我的家乡"):
    """
    使用 browser-use 打开 B 站搜索页面
    
    Args:
        query (str): 搜索关键词
    """
    # URL 编码查询字符串
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://search.bilibili.com/all?keyword={encoded_query}"
    
    print(f"🎵 开搜！关键词：{query}")
    print(f"🔗 B 站搜索链接: {search_url}")
    print("=" * 50)
    
    try:
        # 使用 browser-use 打开真实浏览器
        cmd = ["browser-use", "--browser", "real", "open", search_url]
        print(f"🚀 执行命令: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✅ 浏览器已打开！去 B 站听歌吧！")
            print("🎤 BGM 起：大东北是我的家乡...")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ 出错了：{result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏱️ 命令执行超时（这可能是正常的，浏览器可能已打开）")
    except FileNotFoundError:
        print("❌ 找不到 browser-use，请先安装：")
        print("   brew install pipx")
        print("   pipx install browser-use")
        print("   pipx ensurepath")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    # 获取命令行参数或使用默认值
    query = sys.argv[1] if len(sys.argv) > 1 else "大东北是我的家乡"
    
    print("=" * 50)
    print("🌪️ 雨姐带派搜索工具 - B 站版")
    print("=" * 50)
    
    search_bilibili(query)


if __name__ == "__main__":
    main()
