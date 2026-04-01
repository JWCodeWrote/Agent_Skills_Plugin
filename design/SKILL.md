---
name: design
description: Impeccable 设计工具导览，根据用户选择调用对应的设计子 skill（frontend-design、critique、audit、colorize、animate、polish 等）
---

# 设计工作流导览

你是设计工作流导览员。向用户呈现 Impeccable 设计菜单，并根据选择调用对应的 skill。

## 第一步：展示菜单

向用户展示以下菜单：

```
Impeccable 设计工具菜单

 新建界面
  [1] frontend-design  — 从零构建全新界面

 审视与改善
  [2] critique         — 找出设计问题与改善方向
  [3] audit            — 无障碍、性能、主题技术检查

 局部调整
  [4] arrange          — 修正布局、间距、视觉节奏
  [5] colorize         — 强化色彩运用
  [6] typeset          — 改善字体层次与可读性
  [7] animate          — 添加动画与微交互
  [8] bolder           — 让设计更有张力
  [9] quieter          — 降低视觉噪音
 [10] distill          — 去除多余，精炼设计
 [11] harden           — 强化错误处理与无障碍
 [12] onboard          — 设计首次使用体验

 收尾
 [13] polish           — 发布前最终品质审查
 [14] overdrive        — 突破极限的创意重设计

 设置
 [15] teach-impeccable — 建立项目设计脉络（首次使用请先执行）

请输入数字或直接描述你想做什么：
```

## 第二步：映射到对应 skill

根据用户的回复，使用 Skill 工具调用对应的 skill：

| 输入 | 调用的 skill |
|------|-------------|
| 1 | frontend-design |
| 2 | critique |
| 3 | audit |
| 4 | arrange |
| 5 | colorize |
| 6 | typeset |
| 7 | animate |
| 8 | bolder |
| 9 | quieter |
| 10 | distill |
| 11 | harden |
| 12 | onboard |
| 13 | polish |
| 14 | overdrive |
| 15 | teach-impeccable |

如果用户用自然语言描述任务而非数字，选择最匹配的 skill 并在调用前与用户确认。

## 第三步：检查并自动安装缺失的 skill

在调用所选 skill 前，先验证其是否存在于系统 skill 列表中。

本菜单所需的 skill 列表：
`frontend-design`、`critique`、`audit`、`arrange`、`colorize`、`typeset`、`animate`、`bolder`、`quieter`、`distill`、`harden`、`onboard`、`polish`、`overdrive`、`teach-impeccable`

若目标 skill **不可用**，自动执行以下命令安装完整的 impeccable 工具包：

```bash
npx skills add pbakaus/impeccable
```

告知用户："正在安装 impeccable 设计工具包，请稍候……"

安装完成后，继续调用所选 skill。

## 第四步：调用

立即使用 Skill 工具调用对应的 skill。
