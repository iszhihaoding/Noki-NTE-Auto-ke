#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd "$SCRIPT_DIR"

echo "=========================================="
echo "    Noki-NTE-Auto Mac版 启动器"
echo "=========================================="

if ! command -v uv &>/dev/null; then
    echo "❌ uv 未安装，正在安装..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，正在创建..."
    uv venv .venv
fi

echo "✅ 激活虚拟环境..."
VENV_PYTHON=".venv/bin/python"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ 虚拟环境解释器不存在，重建环境..."
    rm -rf .venv
    uv venv .venv
fi

echo "✅ 检查依赖..."
REQUIREMENTS="numpy opencv-python pillow pyobjc"
for pkg in $REQUIREMENTS; do
    if ! $VENV_PYTHON -c "import $pkg" 2>/dev/null; then
        echo "   安装 $pkg..."
        uv pip install "$pkg"
    fi
done

echo "✅ 启动主程序..."
echo ""
$VENV_PYTHON main.py

echo ""
echo "=========================================="
echo "              程序已退出"
echo "=========================================="
