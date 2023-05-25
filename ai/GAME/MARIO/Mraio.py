import pygame
import random

# 游戏窗口尺寸
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 玩家初始位置
PLAYER_START_X = 50
PLAYER_START_Y = WINDOW_HEIGHT - 100

# 玩家速度和跳跃力度
PLAYER_SPEED = 5
PLAYER_JUMP_FORCE = 10

# 颜色定义
WHITE = (255, 255, 255)

# 初始化游戏引擎
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Super Mario-like Game")

# 创建玩家
player = pygame.Rect(PLAYER_START_X, PLAYER_START_Y, 50, 50)

# 创建时钟对象，控制游戏帧率
clock = pygame.time.Clock()

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 玩家移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_SPACE] and player.y == PLAYER_START_Y:
        player.y -= PLAYER_JUMP_FORCE

    # 玩家下落
    if player.y < PLAYER_START_Y:
        player.y += 1

    # 绘制背景和玩家
    window.fill(WHITE)
    pygame.draw.rect(window, (255, 0, 0), player)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
