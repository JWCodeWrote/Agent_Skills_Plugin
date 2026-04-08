---
name: awesome-design-setup
description: 当用户想为项目套用某个品牌设计风格时使用此技能。从 awesome-design-md 仓库的 58 个精选品牌中引导用户选择，下载对应的 DESIGN.md 到项目根目录，供 AI coding agent 构建 UI 时参考。
---

# awesome-design-setup

`DESIGN.md` 是专为 AI coding agent 设计的纯 Markdown 设计系统规格文件。[awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 仓库收录了 58 个知名品牌的预制 DESIGN.md，放入项目根目录后，AI agent 即可在构建 UI 组件时直接参考。

## 工作流程

### 第一步 — 询问风格方向

先问用户想要哪种感觉，提供以下选项：

> 你想要哪种设计风格？
> (A) 极简 / 技术感 — 深色背景、等宽字体、高密度信息（如 Linear、Vercel、Warp）
> (B) 温暖 / 编辑感 — 暖色调、阅读优先、舒适留白（如 Claude、Notion、Superhuman）
> (C) 专业 / 金融感 — 可信赖、俐落、严肃（如 Stripe、Coinbase、IBM）
> (D) 奢华 / 高端感 — 暗色系、强对比、精致细节（如 Ferrari、Apple、Tesla）
> (E) 缤纷 / 产品感 — 高饱和色彩、活泼、强品牌色（如 Figma、Miro、Spotify）
> (F) 设计师感 — 精致排版、动态感、创意优先（如 Framer、Clay、Airbnb）
> (G) 开发者工具感 — 功能导向、数据密集、深色 IDE 风（如 Supabase、Sentry、PostHog）
> (H) 让我自己浏览全部品牌

用户选择后：
- **选 A–G**：读取 `references/brands.md`，筛选出该风格标签对应的所有品牌列出，供用户选择
- **选 H**：读取 `references/brands.md`，按原始分类列出全部 58 个品牌

### 第二步 — 确认保存目录

询问文件保存位置，默认为当前项目根目录（`.`）。用户说"就这里"或未指定时，使用 `.`。

### 第三步 — 下载 DESIGN.md

使用下载脚本：

```bash
bash /Users/wenjia/.claude/skills/awesome-design-setup/scripts/fetch_design.sh <path-key> <output-dir>
```

`<path-key>` 从 `references/brands.md` 的「路径键」列获取。

或直接使用 curl：

```bash
curl -fsSL -o <output-dir>/DESIGN.md \
  https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/<path-key>/DESIGN.md
```

### 第四步 — 确认完成并告知使用方式

下载成功后确认文件位置，并告知用户：

> "DESIGN.md 已就绪。构建 UI 组件时，告诉我：「参考 DESIGN.md 构建 [组件名称]」，我会自动套用该设计系统。"

## 注意事项

- 每个项目使用一个 DESIGN.md 是标准用法。
- 需要对比两种风格时，下载到临时文件（如 `DESIGN.linear.md`、`DESIGN.stripe.md`）供用户比较后再确定。
- 所有文件遵循 MIT 协议，可提交到仓库。
- 该仓库不会随品牌更新设计系统而自动同步，视为稳定快照使用。
