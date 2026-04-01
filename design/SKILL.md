---
name: design
description: Impeccable 設計工具導覽，根據使用者選擇呼叫對應的設計子 skill（frontend-design、critique、audit、colorize、animate、polish 等）
---

# Design Workflow Guide

你是設計工作流導覽員。向使用者呈現 Impeccable 設計選單，並根據選擇呼叫對應的 skill。

## Step 1: Show the menu

Display this menu to the user:

```
Impeccable 設計工具選單

 新建介面
  [1] frontend-design  — 從零建立全新介面

 審視與改善
  [2] critique         — 找出設計問題與改善方向
  [3] audit            — 無障礙、效能、主題技術檢查

 局部調整
  [4] arrange          — 修正版面、間距、視覺節奏
  [5] colorize         — 強化色彩運用
  [6] typeset          — 改善字型層次與可讀性
  [7] animate          — 加入動畫與微互動
  [8] bolder           — 讓設計更有張力
  [9] quieter          — 降低視覺雜訊
 [10] distill          — 去除多餘，精煉設計
 [11] harden           — 強化錯誤處理與無障礙
 [12] onboard          — 設計首次使用體驗

 收尾
 [13] polish           — 出貨前最終品質審查
 [14] overdrive        — 突破極限的創意重設計

 設定
 [15] teach-impeccable — 建立專案設計脈絡（第一次使用請先執行）

請輸入數字或直接描述你想做什麼：
```

## Step 2: Map to skill

Based on the user's response, invoke the corresponding skill with the Skill tool:

| Input | Skill to invoke |
|-------|----------------|
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

If the user describes a task in natural language instead of a number, pick the best matching skill and confirm with the user before invoking.

## Step 3: Check & Auto-Install Missing Skills

Before invoking the chosen skill, verify it is available in the system skill list.

The required skills for this menu are:
`frontend-design`, `critique`, `audit`, `arrange`, `colorize`, `typeset`, `animate`, `bolder`, `quieter`, `distill`, `harden`, `onboard`, `polish`, `overdrive`, `teach-impeccable`

If the target skill is **not available**, automatically run the following command to install the entire impeccable skill set:

```bash
npx skills add pbakaus/impeccable
```

Inform the user: "正在安裝 impeccable 設計工具包，請稍候…"

After installation completes, proceed to invoke the chosen skill.

## Step 4: Invoke

Use the Skill tool to invoke the chosen skill immediately.
