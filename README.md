# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 新建项目
mkdir demo && cd demo

# 初始化项目
uv init

# 创建虚拟环境
uv venv

# 添加依赖
uv add requests pandas

# 运行脚本
uv run myscript.py


uv run python script.py
uv init
uv add tushare
uv sync

uv python install 3.12
uv python pin 3.12
