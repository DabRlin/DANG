import time

def start_game():
    print("欢迎来到神奇的冒险世界！")
    time.sleep(1)
    print("你将扮演一名年轻的冒险家，准备踏上一场惊险刺激的冒险！")
    time.sleep(2)
    print("你发现自己置身于一片森林中。")
    time.sleep(1)
    print("你的目标是找到失落的宝藏并带回家！")
    time.sleep(1)
    print("开始冒险吧！")
    time.sleep(1)
    start_forest()

def start_forest():
    print("你正站在森林的边缘。")
    time.sleep(1)
    print("你可以选择向左进入一个黑暗的洞穴，或者向右继续穿过森林。")
    choice = input("请选择左边（L）还是右边（R）：")
    if choice.lower() == "l":
        enter_cave()
    elif choice.lower() == "r":
        continue_forest()
    else:
        print("无效的选择！请重新选择。")
        start_forest()

def enter_cave():
    print("你进入了洞穴。")
    time.sleep(1)
    print("洞穴里充满了阴森恐怖的气氛。")
    time.sleep(1)
    print("你发现一个宝箱放在角落里。")
    time.sleep(1)
    print("你可以选择打开宝箱（O）或者返回森林（B）。")
    choice = input("请选择：")
    if choice.lower() == "o":
        open_chest()
    elif choice.lower() == "b":
        start_forest()
    else:
        print("无效的选择！请重新选择。")
        enter_cave()

def open_chest():
    print("你打开了宝箱。")
    time.sleep(1)
    print("一股毒气喷出来，你晕了过去...")
    time.sleep(2)
    print("你醒来时发现自己回到了森林边缘。")
    time.sleep(1)
    print("冒险还没有结束！继续努力吧！")
    time.sleep(1)
    start_forest()

def continue_forest():
    print("你继续穿过森林。")
    time.sleep(1)
    print("突然，一只巨大的熊出现在你面前！")
    time.sleep(1)
    print("你可以选择与熊战斗（F）或者逃跑（E）。")
    choice = input("请选择：")
    if choice.lower() == "f":
        fight_bear()
    elif choice.lower() == "e":
        run_away()
    else:
        print("无效的选择！请重新选择。")
        continue_forest()

def fight_bear():
    print("你决定与熊战斗！")
    time.sleep(1)
    print("你拿出你的剑，开始与熊搏斗。")
    time.sleep(2)
    print("你勇敢地与熊搏斗，最终击败了它！")
    time.sleep(2)
    print("你继续前进，继续寻找宝藏。")
    time.sleep(1)
    print("祝你好运！")
    time.sleep(1)
    end_game()

def run_away():
    print("你决定逃跑！")
    time.sleep(1)
    print("你尽力逃跑，但是熊追赶得更快。")
    time.sleep(2)
    print("熊追上了你，并且抓住了你...")
    time.sleep(2)
    print("很遗憾，冒险以失败告终。再接再厉吧！")
    time.sleep(1)
    end_game()

def end_game():
    print("游戏结束。谢谢你的参与！")

start_game()
