import pygame
import random

# 游戏窗口的宽度和高度
WIDTH = 400
HEIGHT = 200

# 蛇身和食物的大小
BLOCK_SIZE = 4

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 初始化pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

clock = pygame.time.Clock()

# 蛇的初始位置和初始移动方向
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake_dx = BLOCK_SIZE
snake_dy = 0

# 初始化蛇的身体
snake_body = []
snake_length = 1
snake_body.append([snake_x, snake_y])

# 生成食物的随机位置
food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

# 记分变量
score = 0

# 游戏状态
GAME_START = 0
GAME_PLAYING = 1
GAME_OVER = 2
GAME_PAUSED = 3

game_state = GAME_START
game_paused = False

# 加载字体文件
pygame.font.init()
font_path = pygame.font.match_font("arial")  # 根据实际情况修改字体
font_size = 24  # 根据实际情况修改字体大小
font = pygame.font.Font(font_path, font_size)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == GAME_START:
                if event.key == pygame.K_RETURN:
                    game_state = GAME_PLAYING
            elif game_state == GAME_PLAYING:
                if event.key == pygame.K_UP and snake_dy != BLOCK_SIZE:
                    snake_dx = 0
                    snake_dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and snake_dy != -BLOCK_SIZE:
                    snake_dx = 0
                    snake_dy = BLOCK_SIZE
                elif event.key == pygame.K_LEFT and snake_dx != BLOCK_SIZE:
                    snake_dx = -BLOCK_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -BLOCK_SIZE:
                    snake_dx = BLOCK_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_SPACE:
                    game_paused = not game_paused
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif game_state == GAME_OVER:
                if event.key == pygame.K_ESCAPE:
                    running = False

    if game_state == GAME_PLAYING and not game_paused:
        # 更新蛇的位置
        snake_x += snake_dx
        snake_y += snake_dy

        # 判断蛇是否吃到食物
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 10

        # 更新蛇的身体
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # 判断蛇是否碰到墙壁或自身
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_state = GAME_OVER
        if snake_head in snake_body[:-1]:
            game_state = GAME_OVER

    # 绘制游戏窗口
    window.fill(WHITE)

    if game_state == GAME_START:
        # 绘制开始界面
        start_text = font.render("Press Enter to start the game", True, BLACK)
        window.blit(start_text, (WIDTH / 2 - start_text.get_width() / 2, HEIGHT / 2))

    elif game_state == GAME_PLAYING:
        # 绘制食物和蛇的身体
        pygame.draw.rect(window, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        for segment in snake_body:
            pygame.draw.rect(window, RED, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

    elif game_state == GAME_OVER:
        # 绘制游戏结束界面
        end_text = font.render("Game over", True, BLACK)
        restart_text = font.render("Press Esc to exit the game", True, BLACK)
        score_text = font.render("Score: " + str(score), True, BLACK)
        window.blit(end_text, (WIDTH / 2 - end_text.get_width() / 2, HEIGHT / 2 - 50))
        window.blit(restart_text, (WIDTH / 2 - restart_text.get_width() / 2, HEIGHT / 2))
        window.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, HEIGHT / 2 + 50))

    if game_paused:
        # 绘制暂停界面
        paused_text = font.render("Paused", True, BLACK)
        window.blit(paused_text, (WIDTH / 2 - paused_text.get_width() / 2, HEIGHT / 2))

    pygame.display.update()

    clock.tick(10)  # 控制蛇的移动速度

# 游戏结束，退出pygame
pygame.quit()
