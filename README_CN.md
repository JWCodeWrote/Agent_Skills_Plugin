# Agent Skills Plugin (智能体技能插件库)

_Read this in [English](./README.md)._

欢迎来到 **Agent Skills Plugin (智能体技能插件库)**。本项目不仅仅是一个 Python 工具库，更是一套「认知升级模组」。我们通过标准化的 Prompt 工程与知识库，为 AI Agent 植入特定的思维模式、哲学框架与执行人格。

### 🧩 精选技能

| 技能名称                         | 简介                                                                                                               | 核心人格         |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :--------------- |
| **`Dialectical_Materialism`**    | **唯物辩证法 OS**：运用对立统一、质量互变等哲学规律，强制 Agent 进行客观、非线性的深度逻辑分析。                   | _辩证哲学家_     |
| **`Daipai` (带派)**              | **执行力模式**：自带 BGM 的「雨姐」风格。拒绝磨叽，主打高效执行与情绪价值拉满。「别问，问就是开整！」              | _带派执行大师_   |
| **`Shoa-Ji` (烧鸡)**             | **剧本模式**：擅长用「阳光健康」的糖衣包裹「存在主义悲剧」。刀片贩卖者，情感陷阱大师。                             | _致郁系编剧_     |
| **`Li-er` (李耳)**               | **扮演模式**：这只是一个普通的可以和你一起看星星看月亮，从诗词歌赋谈到人生哲学的聊天搭子，绝对没有任何危险的想法。 | _无害的聊天对象_ |
| **`AI-search-browser-use-main`** | **深度搜索**：结合 Chrome CDP 与 browser-use 的高阶联网搜索能力，支持多源信息综合。                                | _深度研究员_     |

### 🚀 使用指南

1.  **安装**：将您需要的技能文件夹（如 `Daipai`）复制到您的 Agent `skills/` 目录下。
2.  **激活**：读取该技能的 `SKILL.md` 内容，并将其加入到 Agent 的 **System Prompt** 或 **Context** 中。
3.  **运行**：Agent 将自动切换至对应人格，并根据需要调用文件夹内的 Python 脚本或参考资料。

### 📂 仓库结构 (Repo Structure)

```text
.
├── Daipai/                   # [Skill] High-Energy Execution (带派执行)
│   ├── SKILL.md              # Definition & Persona
│   ├── scripts/              # Action Scripts (e.g., Bilibili Search)
│   └── references/           # Slang Dictionary (黑话字典)
├── Dialectical_Materialism/  # [Skill] Philosophical Reasoning (唯物辩证法)
│   ├── SKILL.md
│   └── references/           # The Three Laws of Dialectics (三大规律)
├── Shoa-Ji/                  # [Skill] Tragic Storytelling (烧鸡式编剧)
│   ├── SKILL.md
│   └── references/           # Lore Examples (剧情设定集)
├── Li-er/                    # [Skill] Rhetorical Simulation (意识形态模拟)
│   ├── SKILL.md
│   └── references/           # Rhetorical Case Studies (修辞案例)
└── README.md                 # Project Overview
```

## 🛡️ License

MIT License.

---

_Powered by Antigravity-Team & K-Dense Inc._
