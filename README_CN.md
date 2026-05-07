# Agent Skills Plugin (智能体技能插件库)

_Read this in [English](./README.md)._

欢迎来到 **Agent Skills Plugin (智能体技能插件库)**。本项目不仅仅是一个 Python 工具库，更是一套「认知升级模组」。我们通过标准化的 Prompt 工程与知识库，为 AI Agent 植入特定的思维模式、哲学框架与执行人格。

### 🧩 精选技能

| 技能名称                         | 简介                                                                                                               | 核心人格         |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :--------------- |
| **`Dialectical_Materialism`**    | **唯物辩证法 OS**：运用对立统一、质量互变等哲学规律，强制 Agent 进行客观、非线性的深度逻辑分析。                   | _辩证哲学家_     |
| **`Meihua_Yishu`** (梅花易数)    | **混合占卜系统**：古法为体，AI 为用。结合本地精准起卦与 Gemini 联网解读，提供具有现代视野的玄学决策建议。          | _玄学策士_       |
| **`AI-search-browser-use-main`** | **深度搜索**：结合 Chrome CDP 与 browser-use 的高阶联网搜索能力，支持多源信息综合。                                | _深度研究员_     |
| **`HighTriad`**                | **三高架构规划**：面向高并发/高性能/高可用的系统设计与评估，涵盖 SLO、扩展、容灾与压测。 | _系统架构师_             |
| **`story-commentary-workflow`** | **剧情解说工作流**：整理游戏剧情素材、章节拆分、字幕转录、旁白草稿，并建立旁白与画面的对应关系。 | _剧情解说制作人_ |
| **`story-worldbuilding-planner`** | **故事与世界观规划**：创建或打磨游戏剧情、网文/轻小说大纲、角色弧线、阵营设定、力量体系与 lore bible。 | _叙事设计师_ |
| **`European-Chinese-Cleaner`** | **欧式中文清洗器**：将翻译腔、欧化语法、AI 腔和英文直译式中文改写成自然、地道、流畅的中式中文。 | _中文编辑_ |
| **`PUA`**                      | **AI高压纠错模式**：仅对 AI agent 施加严格督导，要求无借口反省与立即修正；明确禁止对用户使用 PUA。 | _AI纪律督导者_ |
| **`agent-fault-retrospective`** | **过失复盘记忆**：当用户指出 AI agent 有过失、越权或误解时，询问用户认定的关键字，用 Superpowers 式根因流程复盘，并把短规则写入正确的 instruction file（如 `AGENTS.md`、`CLAUDE.md`、Cursor rules、Copilot instructions 等）。 | _过失复盘官_ |
| **`Impeccable-design-ui`**                   | **设计工作流中枢**：Impeccable 设计菜单，整合 14 个专项子技能（critique、colorize、animate、polish 等），缺失时自动执行 `npx skills add pbakaus/impeccable` 安装。 | _设计总监_ |
| **`awesome-design-setup`**     | **品牌设计风格选择器**：浏览 58 个精选品牌 DESIGN.md（Linear、Stripe、Apple、Tesla 等），选定后自动下载到项目根目录，供 AI agent 构建 UI 时直接参考。 | _品牌造型师_ |
| **`frontend-imagegen-director`** | **前端视觉概念图导演**：先核对项目现有风格与产品属性，再用内建 `imagegen` 生成页面概念图、组件参考图或风格探索图；若缺少 `superpowers` 等辅助 skill，则退化为手动需求澄清与 prompt 规划。 | _前端视觉导演_ |

### 🚀 使用指南

1.  **安装**：将您需要的技能文件夹（如 `HighTriad`）复制到您的 Agent `skills/` 目录下。
2.  **激活**：读取该技能的 `SKILL.md` 内容，并将其加入到 Agent 的 **System Prompt** 或 **Context** 中。
3.  **运行**：Agent 将自动切换至对应人格，并根据需要调用文件夹内的 Python 脚本或参考资料。

### 📂 仓库结构 (Repo Structure)

```text
.
├── Dialectical_Materialism/  # [Skill] Philosophical Reasoning (唯物辩证法)
│   ├── SKILL.md
│   └── references/           # The Three Laws of Dialectics (三大规律)
├── Meihua_Yishu/ # [Skill] Hybrid AI Divination (梅花易数)
│ ├── SKILL.md
│ ├── scripts/ # Calculation & Gemini Integration (起卦与解读)
│ └── references/ # Hexagrams & Strategy Database (卦象与策略库)
├── AI-search-browser-use-main/ # [Skill] AI 辅助浏览器深度搜索
│ ├── SKILL.md
│ ├── ai_query.py
│ ├── scripts/ # 浏览器规划与页面清理辅助脚本
│ └── references/ # AI 搜索目标说明
├── HighTriad/ # [Skill] 三高系统架构规划
│ ├── SKILL.md
│ └── references/ # 技术/行业/模板参考
├── story-commentary-workflow/ # [Skill] 剧情解说规划
│ ├── SKILL.md
│ └── references/ # 章节 schema、输出模板与工作流手册
├── story-worldbuilding-planner/ # [Skill] 故事与世界观规划
│ └── SKILL.md
├── European-Chinese-Cleaner/ # [Skill] 欧式中文清洗器
│ └── SKILL.md
├── PUA/ # [Skill] AI Agent 高压纠错模式
│ └── SKILL.md
├── agent-fault-retrospective/ # [Skill] AI 过失复盘与 instruction file 短规则沉淀
│ └── SKILL.md
├── Impeccable-design-ui/ # [Skill] Impeccable 设计工作流中枢
│ └── SKILL.md
├── awesome-design-setup/ # [Skill] 品牌设计风格选择器（58 个品牌）
│ ├── SKILL.md
│ ├── references/ # 品牌目录与路径键
│ └── scripts/ # fetch_design.sh 下载辅助脚本
├── frontend-imagegen-director/ # [Skill] 依项目风格生成前端视觉参考图
│ └── SKILL.md
└── README.md                 # Project Overview
```

## 🛡️ License

MIT License.

---

_Powered by Antigravity-Team & K-Dense Inc._
