import pygame
import sys
# 游戏窗口尺寸
WIDTH = 800
HEIGHT = 600

# 游戏方格尺寸
CELL_SIZE = 50

# 游戏地图
MAP = [
    "#############",
    "#           #",
    "#    #      #",
    "#    #      #",
    "#    @      #",
    "#    $      #",
    "#           #",
    "#   ####.####",
    "#           #",
    "#           #",
    "#############"
]

# 游戏角色
PLAYER = "@"
BOX = "$"
TARGET = "."

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 初始化游戏
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("推箱子游戏")
    clock = pygame.time.Clock()
    return screen, clock

# 绘制游戏地图
def draw_map(screen, player_pos):
    for row in range(len(MAP)):
        for col in range(len(MAP[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if MAP[row][col] == "#":
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
            elif MAP[row][col] == ".":
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(screen, BLACK, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 4)
            elif MAP[row][col] == "$":
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, BLACK, (x + CELL_SIZE // 4, y + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))
    
    # 绘制玩家位置的图标
    player_row, player_col = player_pos
    pygame.draw.rect(screen, WHITE, (player_col * CELL_SIZE, player_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(screen, BLACK, (player_col * CELL_SIZE + CELL_SIZE // 2, player_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
    pygame.draw.circle(screen, WHITE, (player_col * CELL_SIZE + CELL_SIZE // 2, player_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 8)


# 找到玩家角色的初始位置
def find_player_position():
    for row in range(len(MAP)):
        for col in range(len(MAP[row])):
            if MAP[row][col] == PLAYER:
                return row, col

# 移动玩家角色
def move_player(player_pos, new_pos):
    px, py = player_pos
    nx, ny = new_pos

    if MAP[nx][ny] == "#":
        return  # 不能移动到障碍物上

    if MAP[nx][ny] == "$":
        bx, by = nx + (nx - px), ny + (ny - py)  # 计算箱子的新位置
        if MAP[bx][by] == "#" or MAP[bx][by] == "$":
            return  # 箱子无法移动到障碍物上或者另一个箱子上
        else:
            MAP[bx] = MAP[bx][:by] + "$" + MAP[bx][by+1:]  # 更新箱子的位置
    else:
        bx, by = -1, -1

    MAP[px] = MAP[px][:py] + " " + MAP[px][py+1:]  # 移动玩家
    MAP[nx] = MAP[nx][:ny] + "@" + MAP[nx][ny+1:]  # 更新玩家位置

    if bx >= 0 and by >= 0:
        MAP[nx] = MAP[nx][:ny] + "." + MAP[nx][ny+1:]  # 玩家推动箱子到目标位置



# 检查胜利条件
def check_win_condition():
    for row in range(len(MAP)):
        for col in range(len(MAP[row])):
            if MAP[row][col] == TARGET:
                return False
    return True

# 主游戏循环
def main_loop(screen, clock):
    running = True
    player_pos = find_player_position()
    while running:
        screen.fill(WHITE)
        draw_map(screen, player_pos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_pos = (player_pos[0] - 1, player_pos[1])
                    move_player(player_pos, new_pos)
                    player_pos = new_pos
                elif event.key == pygame.K_DOWN:
                    new_pos = (player_pos[0] + 1, player_pos[1])
                    move_player(player_pos, new_pos)
                    player_pos = new_pos
                elif event.key == pygame.K_LEFT:
                    new_pos = (player_pos[0], player_pos[1] - 1)
                    move_player(player_pos, new_pos)
                    player_pos = new_pos
                elif event.key == pygame.K_RIGHT:
                    new_pos = (player_pos[0], player_pos[1] + 1)
                    move_player(player_pos, new_pos)
                    player_pos = new_pos
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    print("按下 ESC 键，退出游戏")

        if check_win_condition():
            print("恭喜你获胜！")
            print("Game Finish")
            running = False

        clock.tick(60)
    pygame.quit()
    sys.exit()

# 启动游戏
def start_game():
    screen, clock = init_game()
    main_loop(screen, clock)

# 运行游戏
if __name__ == "__main__":
    start_game()
