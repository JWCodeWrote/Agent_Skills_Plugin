# ai-search-browser-use

用于在真实浏览器中进行 AI 辅助检索的技能包。**主要使用 Chrome CDP（Chrome DevTools Protocol）自动化**，browser-use 作为回退方案。支持 macOS/Windows，最终输出带引用的整合答案。支持 **Gemini + 千问**。

## 内容结构

```
ai-search-browser-use/
├── SKILL.md              # 技能元数据与执行流程说明（必需）
├── ai_query.py           # CDP 查询脚本
├── scripts/
│   └── browser_plan.py   # 浏览器选择脚本
└── references/
    └── ai_search_targets.md  # 参考资料与入口链接
```

## 使用与安装

使用以下指令安装：

```
npx skills add JWCodeWrote/AI-search-browser-use
```

## 快速开始（CDP 方式）

### 1) 安装依赖

```bash
python3 -m venv .venv
./.venv/bin/pip install websockets
```

### 2) 启动 Chrome（CDP 模式）

**重要**：CDP 使用独立的用户数据目录（`--user-data-dir`），这意味着：

- ✅ **可以与你正在使用的 Chrome 同时运行**（你会在 Dock 看到两个 Chrome 图标）
- ✅ **复制配置后保留登录状态**（Gemini、千问等网站保持登录）

```bash
# 清理并复制配置（只需执行一次，或登录过期时重新执行）
rm -rf /tmp/chrome-ai-profile
rsync -a "$HOME/Library/Application Support/Google/Chrome/" /tmp/chrome-ai-profile/

# 启动 CDP Chrome（与正常 Chrome 独立运行！）
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/chrome-ai-profile" \
  "https://gemini.google.com/app" "https://chat.qwen.ai/" &
```

### 3) 验证连接

```bash
curl -s http://localhost:9222/json | python3 -m json.tool
```

应该看到包含 `gemini.google.com` 和 `chat.qwen.ai` 的页面信息。

### 4) 发送查询

```bash
python3 ai_query.py "你的查询问题"
```

### 5) 关闭 Chrome

使用完毕后关闭 CDP 启动的 Chrome 实例：

```bash
pkill -f "Google Chrome.*--remote-debugging-port=9222"
```

## 常见问题（CDP）

| 问题                                                              | 原因                    | 解法                                       |
| ----------------------------------------------------------------- | ----------------------- | ------------------------------------------ |
| `curl: (7) Failed to connect`                                     | Chrome 未以调试模式启动 | 重新用 `--remote-debugging-port=9222` 启动 |
| WebSocket connection refused                                      | Page ID 变了            | 重新获取 `/json`                           |
| `editor not found`                                                | 页面未载入              | 等待数秒后重试                             |
| 登录页面而非 `/app`                                               | Profile 无登录          | 重新复制已登录的 Chrome 配置               |
| `DevTools remote debugging requires a non-default data directory` | 使用了默认 profile      | 一律用 `/tmp/chrome-ai-profile`            |

## 回退方案：browser-use

如果 CDP 不可用，可以使用 `browser-use` 作为回退：

```bash
# 安装
brew install pipx
pipx install browser-use
pipx ensurepath

# 启动
browser-use --browser real open "https://gemini.google.com/app"
browser-use --browser real open "https://chat.qwen.ai/"

# 关闭
browser-use close
```

## 安全提示

仅使用可信来源的技能包（自建或来自可信发布者）。技能可能引导执行工具或脚本，需谨慎审查来源与内容。

## 开发与维护

- `scripts/browser_plan.py`：检测 OS、选择浏览器、提供打开/关闭/安装命令。
- `references/ai_search_targets.md`：Gemini、千问的入口与引用指引。
