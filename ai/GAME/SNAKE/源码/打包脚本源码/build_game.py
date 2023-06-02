import sys
from pathlib import Path
import pygame
import random
import PyInstaller.__main__

# 游戏的入口文件
entry_file = Path("snake_game.py")

# 打包配置
config = [
    "--onefile",
    "--windowed",
    "--name=SnakeGame",
    f"--add-data={entry_file};.",
]

# 使用 PyInstaller 进行打包
PyInstaller.__main__.run([str(entry_file)] + config)
