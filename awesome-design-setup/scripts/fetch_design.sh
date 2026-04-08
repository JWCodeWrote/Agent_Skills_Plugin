#!/usr/bin/env bash
# fetch_design.sh — 从 awesome-design-md 下载指定品牌的 DESIGN.md
# 用法：./fetch_design.sh <品牌路径键> [输出目录]
# 示例：./fetch_design.sh linear.app ./my-project

BRAND="${1}"
OUTPUT_DIR="${2:-.}"
BASE_URL="https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md"

if [ -z "$BRAND" ]; then
  echo "用法：$0 <品牌路径键> [输出目录]"
  echo "示例：$0 linear.app ./my-project"
  exit 1
fi

URL="${BASE_URL}/${BRAND}/DESIGN.md"
OUTPUT_FILE="${OUTPUT_DIR}/DESIGN.md"

echo "正在下载 '${BRAND}' 的 DESIGN.md..."
if curl -fsS -o "${OUTPUT_FILE}" "${URL}"; then
  echo "已保存至 ${OUTPUT_FILE}"
else
  echo "错误：无法获取 ${URL}"
  echo "请检查 references/brands.md 中的品牌路径键是否正确"
  exit 1
fi
