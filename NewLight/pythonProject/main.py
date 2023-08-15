import pygame as pg
from datetime import datetime
pg.init()

window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
W, H = window.get_size()

print(W, " ", H)
red, green, blue, dark_blue = (190, 0, 0), (0, 190, 0), (0, 0, 190), (0, 0, 50)
black, gray_10, gray_20, gray_30, gray_50, gray_70, gray_90, gray_110, gray_140, gray_160, gray_190, gray_220, white = \
    (0, 0, 0), (10, 10, 10),(20, 20, 20), (30, 30, 30), (50, 50, 50), (70, 70, 70), (90, 90, 90), (110, 110, 110), \
    (140, 140, 140), (160, 160, 160), (190, 190, 190), (220, 220, 220), (230, 230, 230)

font = pg.font.SysFont('microsofttaile', 72)
main_font = pg.font.SysFont('microsofttaile', 20)
Wallpaper_1 = pg.transform.scale(pg.image.load('Wallpaper_1.jpg'), (W, H))
Wallpaper_2 = pg.transform.scale(pg.image.load('Wallpaper_2.png'), (W, H))
Wallpaper_3 = pg.transform.scale(pg.image.load('Wallpaper_3.jpg'), (W, H))
Wallpaper_4 = pg.transform.scale(pg.image.load('Wallpaper_4.jpg'), (W, H))
Wallpaper_5 = pg.transform.scale(pg.image.load('Wallpaper_5.jpg'), (W, H))
Wallpaper_6 = pg.transform.scale(pg.image.load('Wallpaper_6.jpg'), (W, H))
Wallpaper_7 = pg.transform.scale(pg.image.load('Wallpaper_7.jpg'), (W, H))
Wallpaper_8 = pg.transform.scale(pg.image.load('Wallpaper_8.jpg'), (W, H))
Wallpaper_9 = pg.transform.scale(pg.image.load('Wallpaper_9.jpg'), (W, H))
Wallpaper_10 = pg.transform.scale(pg.image.load('Wallpaper_10.jpg'), (W, H))
wallpaper_num = 0
wallpapers_x = W // 2 - 300
wallpapers_y = H // 2 - 200
wallpapers = [Wallpaper_1, Wallpaper_2, Wallpaper_3, Wallpaper_4, Wallpaper_5, Wallpaper_6, Wallpaper_7, Wallpaper_8,
              Wallpaper_9, Wallpaper_10]
DESKTOP_wallpaper = Wallpaper_1
JPB_wallpaper = pg.transform.scale(pg.image.load('games_wallpaper.png'), (W, H))
main_menu_table = main_font.render('NL', 2, white, black)
clock = pg.time.Clock()
FPS = 120
Working_apps_set = set()
Player_1_arm_hit_right = pg.transform.scale(pg.image.load('Player_1_arm_hit_right.png'), (W // 5, W // 5))
Player_1_arm_hit_left = pg.transform.scale(pg.image.load('Player_1_arm_hit_left.png'), (W // 5, W // 5))
Player_1_leg_hit_right = pg.transform.scale(pg.image.load('Player_1_leg_hit_right.png'), (W // 5, W // 5))
Player_1_leg_hit_left = pg.transform.scale(pg.image.load('Player_1_leg_hit_left.png'), (W // 5, W // 5))
Player_1_neutral_right = pg.transform.scale(pg.image.load('Player_1_neutral_right.png'), (W // 5, W // 5))
Player_1_neutral_left = pg.transform.scale(pg.image.load('Player_1_neutral_left.png'), (W // 5, W // 5))
Player_1_jump_right = pg.transform.scale(pg.image.load('Player_1_jump_right.png'), (W // 5, W // 5))
Player_1_jump_left = pg.transform.scale(pg.image.load('Player_1_jump_left.png'), (W // 5, W // 5))
Player_1_duck_bend_right = pg.transform.scale(pg.image.load('Player_1_duck_bend_right.png'), (W // 5, W // 5))
Player_1_duck_bend_left = pg.transform.scale(pg.image.load('Player_1_duck_bend_left.png'), (W // 5, W // 5))

Player_2_arm_hit_right = pg.transform.scale(pg.image.load('Player_2_arm_hit_right.png'), (W // 5, W // 5))
Player_2_arm_hit_left = pg.transform.scale(pg.image.load('Player_2_arm_hit_left.png'), (W // 5, W // 5))
Player_2_leg_hit_right = pg.transform.scale(pg.image.load('Player_2_leg_hit_right.png'), (W // 5, W // 5))
Player_2_leg_hit_left = pg.transform.scale(pg.image.load('Player_2_leg_hit_left.png'), (W // 5, W // 5))
Player_2_neutral_right = pg.transform.scale(pg.image.load('Player_2_neutral_right.png'), (W // 5, W // 5))
Player_2_neutral_left = pg.transform.scale(pg.image.load('Player_2_neutral_left.png'), (W // 5, W // 5))
Player_2_jump_right = pg.transform.scale(pg.image.load('Player_2_jump_right.png'), (W // 5, W // 5))
Player_2_jump_left = pg.transform.scale(pg.image.load('Player_2_jump_left.png'), (W // 5, W // 5))
Player_2_duck_bend_right = pg.transform.scale(pg.image.load('Player_2_duck_bend_right.png'), (W // 5, W // 5))
Player_2_duck_bend_left = pg.transform.scale(pg.image.load('Player_2_duck_bend_left.png'), (W // 5, W // 5))

Player_1_forward = pg.transform.scale(pg.image.load('Green_tank_forward.png'), (W // 5, W // 5))
Player_1_back = pg.transform.scale(pg.image.load('Green_tank_back.png'), (W // 5, W // 5))
Player_1_left = pg.transform.scale(pg.image.load('Green_tank_left.png'), (W // 5, W // 5))
Player_1_right = pg.transform.scale(pg.image.load('Green_tank_right.png'), (W // 5, W // 5))
Player_2_forward = pg.transform.scale(pg.image.load('Red_tank_forward.png'), (W // 5, W // 5))
Player_2_back = pg.transform.scale(pg.image.load('Red_tank_back.png'), (W // 5, W // 5))
Player_2_left = pg.transform.scale(pg.image.load('Red_tank_left.png'), (W // 5, W // 5))
Player_2_right = pg.transform.scale(pg.image.load('Red_tank_right.png'), (W // 5, W // 5))

bitva_logo = pg.transform.scale(pg.image.load('bitva_za_padik_logo.png'), (250, 250))
hallway = pg.transform.scale(pg.image.load('hallway.png'), (W, H))
tanks_logo = pg.transform.scale(pg.image.load('tanks_logo.png'), (250, 250))

paint_table = main_font.render('Paint 2.6', 2, white, black)
word_table = main_font.render('Text R beta', 2, white, black)
calculator_table = main_font.render('Calculator beta', 2, white, black)
games_table = main_font.render('Games / JPB console', 2, white, black)
Settings_table = main_font.render('Settings', 2, white, black)
Settings_logo = pg.transform.scale(pg.image.load('settings_logo.png'), (50, 50))
games_logo = pg.transform.scale(pg.image.load('games_logo.png'), (50, 50))
paint_logo = pg.transform.scale(pg.image.load('paint_icon.png'), (50, 50))
word_logo = pg.transform.scale(pg.image.load('word_icon.png'), (50, 50))
calculator_logo = pg.transform.scale(pg.image.load('calculator_icon.png'), (50, 50))
pg.display.set_caption('"New light" OS')
Paint_working_check = 'False'
Text_R_working_check = 'false'

def OS_FUNCTION_Sys_Starting():
    open_color, window_color, z = (230, 230, 230), black, 0
    for a in range(230):
        present_table = font.render("JACKEY PRESENTS", 2, open_color, window_color)
        vers = main_font.render('New Light OS beta', 2, open_color, window_color)
        window.fill(window_color)
        pg.draw.rect(window, gray_50, (W/2 - 230, H - 300, 460, 20))
        pg.draw.rect(window, white, (W/2 - 227, H - 297, (z * 4.54), 14))
        window.blit(vers, (W - 240, H - 30))
        window.blit(present_table, (W/2 - 300, 500))
        window_color = ((0 + a), (0 + a), (0 + a))
        open_color = ((230 - a), (230 - a), (230 - a))
        pg.time.delay(23)
        pg.display.update()
        if a >= 129:
            z += 1
    pg.time.delay(1000)
    OS_FUNCTION_work_space()


def APPS_FUNCTION_opening(enter_text, app):
    pg.draw.rect(window, gray_50, (W // 2 - 205, H // 2 - 105, 410, 210))
    pg.draw.rect(window, gray_70, (W // 2 - 200, H // 2 - 100, 400, 200))
    window.blit(main_font.render(enter_text, 2, white, gray_70), (W // 2 - 195, H // 2 - 95))
    pg.display.update()
    pg.time.delay(2500)
    if app == 'Paint':
        Working_apps_set.add('Paint 2.6')
        Paint_working_check = 'True'
        MENU_FUNCTION_Paint()
    if app == 'Text R':
        Working_apps_set.add('Text R')
        Text_R_working_check = 'True'
        MENU_FUNCTION_Text_R()
    if app == 'Games':
        OS_FUNCTION_JPB_Starting()


def play_mortal_humans(A, B):
    global H
    window.fill(black)
    window.blit((pg.transform.scale(bitva_logo, (H - 100, H - 100))), (H // 2 - 50, 50))
    pg.display.update()
    pg.time.delay(1000)
    Playing = 1
    Players_Position = 1
    Player_1 = [100, 30, 0, 0] #Heartpoints, Position, Pose(0-3 ; neutral, duck_down, leg_hit, jump), Attack type(0-2 ; neutral, arm_hit, leg_hit)
    Player_2 = [100, 70, 0, 0]

    while Playing == 1:
        Player_1_HP_table = main_font.render('Player 1  -- ' + str(Player_1[0]), 2, white, gray_190)
        Player_2_HP_table = main_font.render('Player 2  -- ' + str(Player_2[0]), 2, white, gray_190)

        window.blit(hallway, (0, 0))
        pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
        pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
        window.blit(Player_1_HP_table, (50, 80))
        window.blit(Player_2_HP_table, (W - 250, 80))
        for a in range(A):
            pg.draw.circle(window, red, (57 + a * 17, 115), 7)
        for b in range(B):
            pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)

        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    OS_FUNCTION_Jackey_Play_Box()

                Player_1[2] = 0
                if i.key == pg.K_q: #Player 1
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    if Players_Position == 1:
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_1_arm_hit_right, (Player_1[1] * (W // 150) + 130, (H // 2) + 40))
                        if Player_2[1] - Player_1[1] <= 10 and Player_2[2] == 0:
                            Player_2[0] -= 5
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        window.blit(Player_1_arm_hit_left, (Player_1[1] * (W // 150), (H // 2) + 40))
                        if Player_1[1] - Player_2[1] <= 10 and Player_2[2] == 0:
                            Player_2[0] -= 5
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_a:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[2] = 2
                    if Players_Position == 1:
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[1] - Player_1[1] <= 15 and Player_2[2] != 3:
                            Player_2[0] -= 3
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[1] - Player_2[1] <= 15 and Player_2[2] != 3:
                            Player_2[0] -= 3
                    pg.display.update()
                    pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_s and Player_1[1] > 0:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[1] -= 5
                    if Player_1[1] < Player_2[1]:        # 2 - Player 1 righter than Player 2; 1 - Player 1 lefter than Player 2
                        window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                    if Player_1[1] >= Player_2[1]:
                        window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                    pg.display.update()
                    pg.time.delay(25)
                pg.display.update()

                if i.key == pg.K_e:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[2] = 3
                    if Players_Position == 1:
                        window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_d:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[2] = 1
                    if Players_Position == 1:
                        window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_f and Player_1[1] < 100:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[1] += 5
                    if Player_1[1] < Player_2[1]: #2 - Player 1 righter than Player 2; 1 - Player 1 lefter than Player 2
                        window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                    if Player_1[1] >= Player_2[1]:
                        window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 0:
                            window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 1:
                            window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_2[2] == 2:
                            window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[2] == 3:
                            window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                    pg.display.update()
                    pg.time.delay(25)
                pg.display.update()

#Heartpoints, Position, Pose(0-3 ; neutral, duck_bend, leg_hit, jump), Attack type(0-2 ; neutral, arm_hit, leg_hit)

                Player_2[2] = 0
                if i.key == pg.K_y:   #Player 2
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    if Players_Position == 1:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_arm_hit_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 40))
                        if Player_2[1] - Player_1[1] <= 10 and Player_1[2] == 0:
                            Player_1[0] -= 5
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_arm_hit_right, (Player_2[1] * (W // 150) + 130, (H // 2) + 40))
                        if Player_1[1] - Player_2[1] <= 10 and Player_1[2] == 0:
                            Player_1[0] -= 5
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_h:
                    Player_2[2] = 2
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    if Players_Position == 1:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_2[1] - Player_1[1] <= 15 and Player_1[2] != 3:
                            Player_1[0] -= 3
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[1] - Player_2[1] <= 15 and Player_1[2] != 3:
                            Player_1[0] -= 3
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_j and Player_2[1] > 0:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_2[1] -= 5
                    if Player_1[1] < Player_2[1]:        # 2 - Player 1 righter than Player 2; 1 - Player 1 lefter than Player 2
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                    if Player_1[1] >= Player_2[1]:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                    pg.display.update()
                    pg.time.delay(25)
                pg.display.update()

                if i.key == pg.K_i:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_2[2] = 3
                    if Players_Position == 1:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                    if Players_Position == 2:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                    pg.display.update()
                    pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_k:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_1[2] = 1
                    if Players_Position == 1:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                    if Players_Position == 2:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
                        pg.display.update()
                        pg.time.delay(50)
                pg.display.update()

                if i.key == pg.K_l and Player_2[1] < 100:
                    window.blit(hallway, (0, 0))
                    pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
                    pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
                    window.blit(Player_1_HP_table, (50, 80))
                    window.blit(Player_2_HP_table, (W - 250, 80))
                    for a in range(A):
                        pg.draw.circle(window, red, (57 + a * 17, 115), 7)
                    for b in range(B):
                        pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)
                    Player_2[1] += 5
                    if Player_1[1] < Player_2[1]:        # 2 - Player 1 righter than Player 2; 1 - Player 1 lefter than Player 2
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
                        window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                    if Player_1[1] >= Player_2[1]:
                        if Player_1[2] == 0:
                            window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 1:
                            window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        if Player_1[2] == 2:
                            window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
                        if Player_1[2] == 3:
                            window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
                        window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
                    pg.display.update()
                    pg.time.delay(25)

                Player_1[2] = 0
                pg.display.update()

        window.blit(hallway, (0, 0))
        pg.draw.rect(window, red, (50, 50, Player_1[0] * 2, 20))
        pg.draw.rect(window, blue, (W - 250, 50, Player_2[0] * 2, 20))
        window.blit(Player_1_HP_table, (50, 80))
        window.blit(Player_2_HP_table, (W - 250, 80))
        for a in range(A):
            pg.draw.circle(window, red, (57 + a * 17, 115), 7)
        for b in range(B):
            pg.draw.circle(window, blue, (W - 57 - 17 * b, 115), 7)

# Heartpoints, Position, Pose(0-3 ; neutral, duck_bend, leg_hit, jump), Attack type(0-2 ; neutral, arm_hit, leg_hit)

        if Players_Position == 1:
            if Player_1[2] == 0:
                window.blit(Player_1_neutral_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_1[2] == 1:
                window.blit(Player_1_duck_bend_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))
            if Player_1[2] == 2:
                window.blit(Player_1_leg_hit_right, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_1[2] == 3:
                window.blit(Player_1_jump_right, (Player_1[1] * (W // 150) + 110, (H // 2) + 30))

            if Player_2[2] == 0:
                window.blit(Player_2_neutral_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_2[2] == 1:
                window.blit(Player_2_duck_bend_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))
            if Player_2[2] == 2:
                window.blit(Player_2_leg_hit_left, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_2[2] == 3:
                window.blit(Player_2_jump_left, (Player_2[1] * (W // 150) + 10, (H // 2) + 30))

        if Players_Position == 2:
            if Player_2[2] == 0:
                window.blit(Player_2_neutral_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_2[2] == 1:
                window.blit(Player_2_duck_bend_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))
            if Player_2[2] == 2:
                window.blit(Player_2_leg_hit_right, (Player_2[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_2[2] == 3:
                window.blit(Player_2_jump_right, (Player_2[1] * (W // 150) + 110, (H // 2) + 30))

            if Player_1[2] == 0:
                window.blit(Player_1_neutral_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_1[2] == 1:
                window.blit(Player_1_duck_bend_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))
            if Player_1[2] == 2:
                window.blit(Player_1_leg_hit_left, (Player_1[1] * (W // 150) + 70, (H // 2) + 30))
            if Player_1[2] == 3:
                window.blit(Player_1_jump_left, (Player_1[1] * (W // 150) + 10, (H // 2) + 30))

        pg.display.update()

        if Player_1[0] < 1:
            Player_1[0] = 0
            play_mortal_humans(A, B + 1)

        if Player_2[0] < 1:
            Player_2[0] = 0
            play_mortal_humans(A + 1, B)


def World_of_tanks(A, B):
    global H
    window.fill(black)
    window.blit((pg.transform.scale(tanks_logo, (H - 100, H - 100))), (H // 2 - 50, 50))
    pg.display.update()
    pg.time.delay(1000)
    Player_1 = [100, 90, 90, 1]  #Heartpoints, Position X, Position Y, side (1 - Forward, 2 - Back, 3 - left, 4 - Right)
    Player_2 = [100, 10, 10, 2]

    while 1:
        window.fill(gray_50)
        pg.draw.rect(window, black, (W // 2 - (H // 2 - 50), H // 2 - (H // 2 - 50), H - 100, H - 160))
        pg.draw.rect(window, green, (50, 50, Player_1[0] * 2, 20))
        pg.draw.rect(window, red, (W - 250, 50, Player_2[0] * 2, 20))
        Player_1_HP_table = main_font.render('Player 1  -- ' + str(Player_1[0]), 2, white, gray_50)
        Player_2_HP_table = main_font.render('Player 2  -- ' + str(Player_2[0]), 2, white, gray_50)
        window.blit(Player_1_HP_table, (50, 80))
        window.blit(Player_2_HP_table, (W - 250, 80))
        for a in range(A):
            pg.draw.circle(window, green, (57 + a * 17, 115), 7)
        for b in range(B):
            pg.draw.circle(window, red, (W - 57 - 17 * b, 115), 7)
                                #Players tanks visualization
        if Player_1[3] == 1:
            window.blit(Player_1_forward, (W // 2 - (H // 2 - 20) + (7 * Player_1[1]), H // 2 - (H // 2) + (7 * Player_1[2])))
        if Player_1[3] == 2:
            window.blit(Player_1_back, (W // 2 - (H // 2 - 20) + (7 * Player_1[1]), H // 2 - (H // 2) + (7 * Player_1[2])))
        if Player_1[3] == 3:
            window.blit(Player_1_left, (W // 2 - (H // 2 - 20) + (7 * Player_1[1]), H // 2 - (H // 2) + (7 * Player_1[2])))
        if Player_1[3] == 4:
            window.blit(Player_1_right, (W // 2 - (H // 2 - 20) + (7 * Player_1[1]), H // 2 - (H // 2) + (7 * Player_1[2])))

        if Player_2[3] == 1:
            window.blit(Player_2_forward, (W // 2 - (H // 2 - 20) + (7 * Player_2[1]), H // 2 - (H // 2) + (7 * Player_2[2])))
        if Player_2[3] == 2:
            window.blit(Player_2_back, (W // 2 - (H // 2 - 20) + (7 * Player_2[1]), H // 2 - (H // 2) + (7 * Player_2[2])))
        if Player_2[3] == 3:
            window.blit(Player_2_left, (W // 2 - (H // 2 - 20) + (7 * Player_2[1]), H // 2 - (H // 2) + (7 * Player_2[2])))
        if Player_2[3] == 4:
            window.blit(Player_2_right, (W // 2 - (H // 2 - 20) + (7 * Player_2[1]), H // 2 - (H // 2) + (7 * Player_2[2])))

        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    OS_FUNCTION_Jackey_Play_Box()
                if i.key == pg.K_q:         #Player 1
                    if Player_1[3] == 1 and Player_1[2] > -10:
                        Player_1[2] -= 10
                    if Player_1[3] == 2 and Player_1[2] < 110:
                        Player_1[2] += 10
                    if Player_1[3] == 3 and Player_1[1] > -10:
                        Player_1[1] -= 10
                    if Player_1[3] == 4 and Player_1[1] < 110:
                        Player_1[1] += 10
                    pg.time.delay(50)

                if i.key == pg.K_a:
                    if Player_1[3] == 1:
                        if Player_1[2] > Player_2[2] and Player_1[1] == Player_2[1]:
                            Player_2[0] -= 10
                            print('Player 2 was shot')
                    if Player_1[3] == 2:
                        if Player_1[2] < Player_2[2] and Player_1[1] == Player_2[1]:
                            Player_2[0] -= 10
                            print('Player 2 was shot')
                    if Player_1[3] == 3:
                        if Player_1[2] == Player_2[2] and Player_1[1] > Player_2[1]:
                            Player_2[0] -= 10
                            print('Player 2 was shot')
                    if Player_1[3] == 4:
                        if Player_1[2] == Player_2[2] and Player_1[1] < Player_2[1]:
                            Player_2[0] -= 10
                            print('Player 2 was shot')
                    pg.time.delay(50)

                if i.key == pg.K_s:
                    Player_1[3] = 3
                if i.key == pg.K_e:
                    Player_1[3] = 1
                if i.key == pg.K_d:
                    Player_1[3] = 2
                if i.key == pg.K_f:
                    Player_1[3] = 4

                if i.key == pg.K_y:         #Player 2
                    if Player_2[3] == 1 and Player_2[2] > -10:
                        Player_2[2] = Player_2[2] - 10
                    if Player_2[3] == 2 and Player_2[2] < 110:
                        Player_2[2] = Player_2[2] + 10
                    if Player_2[3] == 3 and Player_2[1] > -10:
                        Player_2[1] = Player_2[1] - 10
                    if Player_2[3] == 4 and Player_2[1] < 110:
                        Player_2[1] = Player_2[1] + 10
                    pg.time.delay(50)

                if i.key == pg.K_h:
                    if Player_2[3] == 1:
                        if Player_2[2] > Player_1[2] and Player_1[1] == Player_2[1]:
                            Player_1[0] -= 10
                            print('Player 2 was shot')
                    if Player_2[3] == 2:
                        if Player_2[2] < Player_1[2] and Player_1[1] == Player_2[1]:
                            Player_1[0] -= 10
                            print('Player 2 was shot')
                    if Player_2[3] == 3:
                        if Player_1[2] == Player_2[2] and Player_2[1] > Player_1[1]:
                            Player_1[0] -= 10
                            print('Player 2 was shot')
                    if Player_2[3] == 4:
                        if Player_1[2] == Player_2[2] and Player_2[1] < Player_1[1]:
                            Player_1[0] -= 10
                            print('Player 2 was shot')
                    pg.time.delay(50)

                if i.key == pg.K_j:
                    Player_2[3] = 3
                if i.key == pg.K_i:
                    Player_2[3] = 1
                if i.key == pg.K_k:
                    Player_2[3] = 2
                if i.key == pg.K_l:
                    Player_2[3] = 4

        pg.display.update()

        if Player_1[0] < 1:
            Player_1[0] = 0
            print('Player 2 won')
            World_of_tanks(A, B + 1)

        if Player_2[0] < 1:
            Player_2[0] = 0
            print('Player 1 won')
            World_of_tanks(A + 1, B)


def APPS_FUNCTION_end(exit_text, app):
    exit_table = main_font.render(exit_text, 2, white, gray_70)
    pg.draw.rect(window, gray_50, (W // 2 - 205, H // 2 - 105, 410, 210))
    pg.draw.rect(window, gray_70, (W // 2 - 200, H // 2 - 100, 400, 200))
    window.blit(exit_table, (W // 2 - 195, H // 2 - 95))
    pg.display.update()
    pg.time.delay(2500)
    if app == 'Paint':
        Working_apps_set.discard('Paint 2.6')
        Paint_working_check = 'False'
        OS_FUNCTION_work_space()
    if app == 'Text R':
        Working_apps_set.discard('Text R')
        Text_R_working_check = 'false'
        OS_FUNCTION_work_space()
    if app == 'Games':
        OS_FUNCTION_work_space()


def OS_FUNCTION_JPB_Starting():
    open_color, window_color, z = (230, 230, 230), black, 0
    for a in range(230):
        present_table = font.render("JACKEY PLAY BOX", 2, open_color, window_color)
        vers = main_font.render('Jackey play box beta', 2, open_color, window_color)
        window.fill(window_color)
        pg.draw.rect(window, gray_50, (W/2 - 230, H - 300, 460, 20))
        pg.draw.rect(window, white, (W/2 - 227, H - 297, (z * 4.54), 14))
        window.blit(vers, (W - 240, H - 30))
        window.blit(present_table, (W/2 - 280, H // 2))
        window_color = ((230 - a), (230 - a), (230 - a))
        open_color = (a, a, a)
        pg.time.delay(23)
        pg.display.update()
        if a >= 129:
            z += 1
    pg.time.delay(1000)
    OS_FUNCTION_Jackey_Play_Box()


def MENU_FUNCTION_Paint():
    global red, green, blue, white, black, gray_90, gray_50, gray_160, W, H

    yellow = (230, 230, 0)
    pink = (230, 70, 150)
    light_purple = (170, 0, 170)
    purple = (120, 0, 120)
    orange = (230, 110, 0)
    brown = (185, 70, 0)
    color = black
    window_color = white
    size = 10
    col = 'black'
    paint_window = window
    mini_font = pg.font.SysFont('microsofttaile', 12)

    pg.display.set_caption('Paint 2.6')
    paint_window.fill(window_color)
    while 1:
        time = str(datetime.now().isoformat())
        main_time = (time[0] + time[1] + time[2] + time[3] + '.' + time[5] + time[6] + '.' + time[8] + time[9] +
                     '  ' + time[11] + time[12] + ':' + time[14] + time[15])
        time_table = main_font.render(main_time, 2, white, gray_50)
        draw_size_table = mini_font.render('draw size : ' + str(size), 1, gray_50, gray_160)
        color_table = mini_font.render('color : ' + col, 1, gray_50, gray_160)
        pressed = pg.mouse.get_pressed()
        x, y = pg.mouse.get_pos()
        pg.draw.rect(paint_window, (170, 170, 170), (0, 0, W, 100))
        pg.draw.rect(paint_window, (190, 190, 190), (0, 100, 100, H))
        pg.draw.rect(window, gray_50, (0, H - 40, W, 40))
        pg.draw.rect(window, black, (7, H - 33, 36, 26))
        window.blit(main_menu_table, (10, H - 33))
        window.blit(time_table, (W - 170, H - 30))
        for i in range (len(Working_apps_set)):
            if 'Paint 2.6' in Working_apps_set:
                window.blit(paint_logo, (50 + (i * 50), H - 50))
            if 'Text R' in Working_apps_set:
                window.blit(word_logo, (50 + (i * 50), H - 40))
        pg.draw.line(paint_window, gray_50, (230, 50), (270, 50), 5)
        pg.draw.line(paint_window, gray_50, (250, 30), (250, 70), 5)
        pg.draw.line(paint_window, gray_50, (330, 50), (370, 50), 5)
        pg.draw.rect(paint_window, red, (400, 20, 30, 30))
        pg.draw.rect(paint_window, orange, (435, 20, 30, 30))
        pg.draw.rect(paint_window, yellow, (470, 20, 30, 30))
        pg.draw.rect(paint_window, green, (505, 20, 30, 30))
        pg.draw.rect(paint_window, blue, (540, 20, 30, 30))
        pg.draw.rect(paint_window, pink, (400, 55, 30, 30))
        pg.draw.rect(paint_window, light_purple, (435, 55, 30, 30))
        pg.draw.rect(paint_window, purple, (470, 55, 30, 30))
        pg.draw.rect(paint_window, black, (505, 55, 30, 30))
        pg.draw.rect(paint_window, brown, (540, 55, 30, 30))
        paint_window.blit(draw_size_table, (220, 2))
        paint_window.blit(color_table, (400, 2))
        for e in range(0, 25, 1):
            pg.draw.line(paint_window, gray_90, (89, 100 + 37 * e), (100, 100 + 37 * e), 2 + 1 // 2)
        for u in range(0, 45, 1):
            pg.draw.line(paint_window, gray_90, (100 + 37 * u, 89), (100 + 37 * u, 100), 2 + 1 // 2)
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    APPS_FUNCTION_end('Exiting from Paint...', 'Paint')
                if i.key == pg.K_1:
                    color = black
                    col = 'black'
                if i.key == pg.K_2:
                    color = green
                    col = 'green'
                if i.key == pg.K_3:
                    color = red
                    col = 'red'
                if i.key == pg.K_4:
                    color = yellow
                    col = 'yellow'
                if i.key == pg.K_5:
                    color = blue
                    col = 'blue'
                if i.key == pg.K_6:
                    color = pink
                    col = 'pink'
                if i.key == pg.K_7:
                    color = light_purple
                    col = 'light-purple'
                if i.key == pg.K_8:
                    color = purple
                    col = 'purple'
                if i.key == pg.K_9:
                    color = orange
                    col = 'orange'
                if i.key == pg.K_0:
                    color = brown
                    col = 'brown'
                if i.key == pg.K_SPACE:
                    window_color = (230, 230, 230)
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_q:
                    window_color = black
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_w:
                    window_color = green
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_e:
                    window_color = red
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_r:
                    window_color = yellow
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_t:
                    window_color = blue
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_y:
                    window_color = pink
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_u:
                    window_color = light_purple
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_i:
                    window_color = purple
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_o:
                    window_color = orange
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))
                if i.key == pg.K_p:
                    window_color = brown
                    pg.draw.rect(paint_window, window_color, (100, 100, W, H))

        if pressed[0]:
            if x > 100 and y > 100:
                pg.draw.circle(paint_window, color, (x, y), size // 2)
            if 400 < x < 430 and 10 < y < 40:
                color = red
                col = 'red'
            if 435 < x < 465 and 10 < y < 40:
                color = orange
                col = 'orange'
            if 470 < x < 500 and 10 < y < 40:
                color = yellow
                col = 'yellow'
            if 505 < x < 535 and 10 < y < 40:
                color = green
                col = 'green'
            if 540 < x < 570 and 10 < y < 40:
                color = blue
                col = 'blue'
            if 400 < x < 430 and 45 < y < 75:
                color = pink
                col = 'pink'
            if 435 < x < 465 and 45 < y < 75:
                color = light_purple
                col = 'light-purple'
            if 470 < x < 500 and 45 < y < 75:
                color = purple
                col = 'purple'
            if 505 < x < 535 and 45 < y < 75:
                color = black
                col = 'black'
            if 540 < x < 570 and 45 < y < 75:
                color = brown
                col = 'brown'

        if 220 < x < 280 and 20 < y < 80:
            pg.draw.rect(paint_window, (90, 90, 220), (220, 20, 60, 60))
            pg.draw.line(paint_window, gray_50, (230, 50), (270, 50), 5)
            pg.draw.line(paint_window, gray_50, (250, 30), (250, 70), 5)
            if size < 20 and pressed[0]:
                size += 1
                pg.time.delay(100)
        if 320 < x < 380 and 20 < y < 80:
            pg.draw.rect(paint_window, (90, 90, 220), (320, 20, 60, 60))
            pg.draw.line(paint_window, gray_50, (330, 50), (370, 50), 5)
            if size > 2 and pressed[0]:
                size -= 1
                pg.time.delay(100)

        if pressed[1]:
            pg.draw.rect(paint_window, color, (x - size // 2, y - size // 2, size, size))
        if pressed[2]:
            pg.draw.rect(paint_window, window_color, (x - 20 // 2, y - 20 // 2, 20, 20))

        pg.display.update()
        pg.time.delay(1)


def MENU_FUNCTION_Text_R():
    x, y = W // 2 - 550, H // 2 - 350
    message = 'hello world|'
    window.blit(DESKTOP_wallpaper, (0, 0))
    pg.draw.rect(window, gray_50, (0, H - 40, W, 40))
    pg.draw.rect(window, black, (7, H - 33, 36, 26))
    window.blit(main_menu_table, (10, H - 33))
    pg.draw.rect(window, white, (x, y, 1100, 700))
    pg.draw.rect(window, gray_90, (x, y, 1100, 40))
    pg.draw.rect(window, gray_160, (x, y + 40, 40, 660))
    while 1:
        time = str(datetime.now().isoformat())
        main_time = (time[0] + time[1] + time[2] + time[3] + '.' + time[5] + time[6] + '.' + time[8] + time[9] +
                     '  ' + time[11] + time[12] + ':' + time[14] + time[15])
        time_table = main_font.render(main_time, 2, white, gray_50)
        window.blit(time_table, (W - 170, H - 30))
        for i in range (len(Working_apps_set)):
            if 'Paint 2.6' in Working_apps_set:
                window.blit(paint_logo, (50 + (i * 50), H - 50))
            if 'Text R' in Working_apps_set:
                window.blit(word_logo, (50 + (i * 50), H - 45))
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    APPS_FUNCTION_end('Exiting from Text R...', 'Text R')
                if i.key == pg.K_q:
                    message = message[0: -1]
                    message = message + 'q'
                    message = message + '|'
                if i.key == pg.K_w:
                    message = message[0: -1]
                    message = message + 'w'
                    message = message + '|'
                if i.key == pg.K_e:
                    message = message[0: -1]
                    message = message + 'e'
                    message = message + '|'
                if i.key == pg.K_r:
                    message = message[0: -1]
                    message = message + 'r'
                    message = message + '|'
                if i.key == pg.K_t:
                    message = message[0: -1]
                    message = message + 't'
                    message = message + '|'
                if i.key == pg.K_y:
                    message = message[0: -1]
                    message = message + 'y'
                    message = message + '|'
                if i.key == pg.K_u:
                    message = message[0: -1]
                    message = message + 'u'
                    message = message + '|'
                if i.key == pg.K_i:
                    message = message[0: -1]
                    message = message + 'i'
                    message = message + '|'
                if i.key == pg.K_o:
                    message = message[0: -1]
                    message = message + 'o'
                    message = message + '|'
                if i.key == pg.K_p:
                    message = message[0: -1]
                    message = message + 'p'
                    message = message + '|'
                if i.key == pg.K_a:
                    message = message[0: -1]
                    message = message + 'a'
                    message = message + '|'
                if i.key == pg.K_s:
                    message = message[0: -1]
                    message = message + 's'
                    message = message + '|'
                if i.key == pg.K_d:
                    message = message[0: -1]
                    message = message + 'd'
                    message = message + '|'
                if i.key == pg.K_f:
                    message = message[0: -1]
                    message = message + 'f'
                    message = message + '|'
                if i.key == pg.K_g:
                    message = message[0: -1]
                    message = message + 'g'
                    message = message + '|'
                if i.key == pg.K_h:
                    message = message[0: -1]
                    message = message + 'h'
                    message = message + '|'
                if i.key == pg.K_j:
                    message = message[0: -1]
                    message = message + 'j'
                    message = message + '|'
                if i.key == pg.K_k:
                    message = message[0: -1]
                    message = message + 'k'
                    message = message + '|'
                if i.key == pg.K_l:
                    message = message[0: -1]
                    message = message + 'l'
                    message = message + '|'
                if i.key == pg.K_z:
                    message = message[0: -1]
                    message = message + 'z'
                    message = message + '|'
                if i.key == pg.K_x:
                    message = message[0: -1]
                    message = message + 'x'
                    message = message + '|'
                if i.key == pg.K_c:
                    message = message[0: -1]
                    message = message + 'c'
                    message = message + '|'
                if i.key == pg.K_v:
                    message = message[0: -1]
                    message = message + 'v'
                    message = message + '|'
                if i.key == pg.K_b:
                    message = message[0: -1]
                    message = message + 'b'
                    message = message + '|'
                if i.key == pg.K_n:
                    message = message[0: -1]
                    message = message + 'n'
                    message = message + '|'
                if i.key == pg.K_m:
                    message = message[0: -1]
                    message = message + 'm'
                    message = message + '|'
                if i.key == pg.K_SPACE:
                    message = message[0: -1]
                    message = message + ' '
                    message = message + '|'
                if i.key == pg.K_1:
                    message = message[0: -1]
                    message = message + '1'
                    message = message + '|'
                if i.key == pg.K_2:
                    message = message[0: -1]
                    message = message + '2'
                    message = message + '|'
                if i.key == pg.K_3:
                    message = message[0: -1]
                    message = message + '3'
                    message = message + '|'
                if i.key == pg.K_4:
                    message = message[0: -1]
                    message = message + '4'
                    message = message + '|'
                if i.key == pg.K_5:
                    message = message[0: -1]
                    message = message + '5'
                    message = message + '|'
                if i.key == pg.K_6:
                    message = message[0: -1]
                    message = message + '6'
                    message = message + '|'
                if i.key == pg.K_7:
                    message = message[0: -1]
                    message = message + '7'
                    message = message + '|'
                if i.key == pg.K_8:
                    message = message[0: -1]
                    message = message + '8'
                    message = message + '|'
                if i.key == pg.K_9:
                    message = message[0: -1]
                    message = message + '9'
                    message = message + '|'
                if i.key == pg.K_0:
                    message = message[0: -1]
                    message = message + '0'
                    message = message + '|'
                if i.key == pg.K_COMMA:
                    message = message[0: -1]
                    message = message + ','
                    message = message + '|'
                if i.key == pg.K_PERIOD:
                    message = message[0: -1]
                    message = message + '.'
                    message = message + '|'
                if i.key == pg.K_BACKSPACE and len(message) > 0:
                    message = message[0: -2]
                    message = message + '|'

        pg.draw.rect(window, white, (x + 40, y + 40, 1060, 660))
        line_1 = main_font.render(message[0: 74], 2, black, white)
        line_2 = main_font.render(message[75: 149], 2, black, white)
        line_3 = main_font.render(message[150: 224], 2, black, white)
        line_4 = main_font.render(message[225: 299], 2, black, white)
        line_5 = main_font.render(message[300: 374], 2, black, white)
        line_6 = main_font.render(message[375: 449], 2, black, white)
        line_7 = main_font.render(message[450: 524], 2, black, white)
        line_8 = main_font.render(message[525: 599], 2, black, white)
        line_9 = main_font.render(message[600: 674], 2, black, white)
        line_10 = main_font.render(message[675: 749], 2, black, white)
        line_11 = main_font.render(message[750: 824], 2, black, white)
        line_12 = main_font.render(message[825: 899], 2, black, white)

        window.blit(line_1, (x + 50, y + 45))
        window.blit(line_2, (x + 50, y + 68))
        window.blit(line_3, (x + 50, y + 91))
        window.blit(line_4, (x + 50, y + 118))
        window.blit(line_5, (x + 50, y + 141))
        window.blit(line_6, (x + 50, y + 164))
        window.blit(line_7, (x + 50, y + 187))
        window.blit(line_8, (x + 50, y + 210))
        window.blit(line_9, (x + 50, y + 233))
        window.blit(line_10, (x + 50, y + 256))
        window.blit(line_11, (x + 50, y + 279))
        window.blit(line_12, (x + 50, y + 302))
        window.blit(time_table, (W - 170, H - 30))

        pg.display.update()


def MENU_FUNCTION_Settings():
    global DESKTOP_wallpaper, wallpaper_num, wallpapers_x, wallpapers_y, wallpapers
    Wallapper_choose_table = main_font.render('Wallpaper', 2, white, dark_blue)
    settings_x = 50
    settings_y = H // 2 - 200
    setting_num = 0
    settings = ['Wallpaper']
    wallpapers_y = settings_y
    while 1:
        window.fill(gray_50)
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    OS_FUNCTION_work_space()
                if i.key == pg.K_UP and setting_num > 0:
                    setting_num -= 1
                if i.key == pg.K_DOWN and setting_num < 0:
                    setting_num += 1
                if i.key == pg.K_RIGHT:
                    if setting_num == 0 and wallpaper_num < 9:
                        wallpaper_num += 1
                        wallpapers_x_1 = wallpapers_x
                        wallpapers_x_2 = wallpapers_x - 164
                        for wallpapers_x in range(wallpapers_x_1, wallpapers_x_2, -3):
                            window.fill(gray_50)
                            pg.draw.rect(window, gray_30, (W // 2 - 138, H // 2 - 217, 150, 124))
                            pg.draw.rect(window, gray_20, (W // 2 - 138, H // 2 - 217, 150, 124), 2)
                            window.blit((pg.transform.scale(Wallpaper_1, (150, 84))),
                                        (wallpapers_x + 162, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_2, (150, 84))),
                                        (wallpapers_x + 324, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_3, (150, 84))),
                                        (wallpapers_x + 486, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_4, (150, 84))),
                                        (wallpapers_x + 648, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_5, (150, 84))),
                                        (wallpapers_x + 810, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_6, (150, 84))),
                                        (wallpapers_x + 972, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_7, (150, 84))),
                                        (wallpapers_x + 1134, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_8, (150, 84))),
                                        (wallpapers_x + 1296, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_9, (150, 84))),
                                        (wallpapers_x + 1458, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_10, (150, 84))),
                                        (wallpapers_x + 1620, wallpapers_y + 5))
                            pg.draw.rect(window, dark_blue, (0, 0, 230, H + 20))
                            pg.draw.rect(window, gray_10, (0, 0, W, 70))
                            window.blit(Settings_logo, (10, 10))
                            window.blit(Wallapper_choose_table, (63, settings_y + 25))
                            pg.display.update()
                if i.key == pg.K_LEFT:
                    if setting_num == 0 and wallpaper_num > 0:
                        wallpaper_num -= 1
                        wallpapers_x_1 = wallpapers_x
                        wallpapers_x_2 = wallpapers_x + 164
                        for wallpapers_x in range(wallpapers_x_1, wallpapers_x_2, 3):
                            window.fill(gray_50)
                            pg.draw.rect(window, gray_30, (W // 2 - 138, H // 2 - 217, 150, 124))
                            pg.draw.rect(window, gray_20, (W // 2 - 138, H // 2 - 217, 150, 124), 2)
                            window.blit((pg.transform.scale(Wallpaper_1, (150, 84))),
                                        (wallpapers_x + 162, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_2, (150, 84))),
                                        (wallpapers_x + 324, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_3, (150, 84))),
                                        (wallpapers_x + 486, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_4, (150, 84))),
                                        (wallpapers_x + 648, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_5, (150, 84))),
                                        (wallpapers_x + 810, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_6, (150, 84))),
                                        (wallpapers_x + 972, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_7, (150, 84))),
                                        (wallpapers_x + 1134, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_8, (150, 84))),
                                        (wallpapers_x + 1296, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_9, (150, 84))),
                                        (wallpapers_x + 1458, wallpapers_y + 5))
                            window.blit((pg.transform.scale(Wallpaper_10, (150, 84))),
                                        (wallpapers_x + 1620, wallpapers_y + 5))
                            pg.draw.rect(window, dark_blue, (0, 0, 230, H + 20))
                            pg.draw.rect(window, gray_10, (0, 0, W, 70))
                            window.blit(Settings_logo, (10, 10))
                            window.blit(Wallapper_choose_table, (63, settings_y + 25))
                            pg.display.update()

        if setting_num == 0:
            pg.draw.rect(window, gray_20, (W // 2 - 138, H // 2 - 217, 150, 124))
            window.blit((pg.transform.scale(Wallpaper_1, (150, 84))),
                        (wallpapers_x + 162, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_2, (150, 84))),
                        (wallpapers_x + 324, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_3, (150, 84))),
                        (wallpapers_x + 486, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_4, (150, 84))),
                        (wallpapers_x + 648, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_5, (150, 84))),
                        (wallpapers_x + 810, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_6, (150, 84))),
                        (wallpapers_x + 972, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_7, (150, 84))),
                        (wallpapers_x + 1134, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_8, (150, 84))),
                        (wallpapers_x + 1296, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_9, (150, 84))),
                        (wallpapers_x + 1458, wallpapers_y + 5))
            window.blit((pg.transform.scale(Wallpaper_10, (150, 84))),
                        (wallpapers_x + 1620, wallpapers_y + 5))

        if wallpaper_num == 0:
            DESKTOP_wallpaper = Wallpaper_1
        if wallpaper_num == 1:
            DESKTOP_wallpaper = Wallpaper_2
        if wallpaper_num == 2:
            DESKTOP_wallpaper = Wallpaper_3
        if wallpaper_num == 3:
            DESKTOP_wallpaper = Wallpaper_4
        if wallpaper_num == 4:
            DESKTOP_wallpaper = Wallpaper_5
        if wallpaper_num == 5:
            DESKTOP_wallpaper = Wallpaper_6
        if wallpaper_num == 6:
            DESKTOP_wallpaper = Wallpaper_7
        if wallpaper_num == 7:
            DESKTOP_wallpaper = Wallpaper_8
        if wallpaper_num == 8:
            DESKTOP_wallpaper = Wallpaper_9
        if wallpaper_num == 9:
            DESKTOP_wallpaper = Wallpaper_10

        pg.draw.rect(window, dark_blue, (0, 0, 230, H + 20))
        pg.draw.rect(window, gray_10, (0, 0, W, 70))
        window.blit(Settings_logo, (10, 10))
        window.blit(Wallapper_choose_table, (63, settings_y + 25))
        pg.display.update()
        clock.tick(FPS)


def OS_FUNCTION_menu(time_table):
    window.fill(black)
    window.blit(DESKTOP_wallpaper, (0, 0))
    pg.draw.rect(window, gray_50, (0, H - 40, W, 40))
    pg.draw.rect(window, black, (7, H - 33, 36, 26))
    window.blit(main_menu_table, (10, H - 33))
    pg.draw.rect(window, black, (10, H - 280, 280, 230))
    window.blit(Settings_logo, (13, H - 105))
    window.blit(Settings_table, (73, H - 95))
    window.blit(paint_logo, (13, H - 218))
    window.blit(paint_table, (73, H - 200))
    window.blit(word_logo, (17, H - 162))
    window.blit(word_table, (73, H - 145))
    window.blit(games_logo, (14, H - 265))
    window.blit(games_table, (73, H - 250))
    while 1:
        time = str(datetime.now().isoformat())
        main_time = (time[0] + time[1] + time[2] + time[3] + '.' + time[5] + time[6] + '.' + time[8] + time[9] +
                     '  ' + time[11] + time[12] + ':' + time[14] + time[15])
        time_table = main_font.render(main_time, 2, white, gray_50)
        window.blit(time_table, (W - 170, H - 30))
        x, y = pg.mouse.get_pos()
        mouse_press = pg.mouse.get_pressed()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    OS_FUNCTION_work_space()

        if mouse_press[0]:
            if x < 10 and y < H - 40 or 10 < x < 210 and y < H - 260 or x > 210 and y < H - 40:
                OS_FUNCTION_work_space()
            if 13 < x < 63 and H - 225 < y < H - 175:
                APPS_FUNCTION_opening('Welcome to Paint', 'Paint')
            if 17 < x < 67 and H - 170 < y < H - 120:
                APPS_FUNCTION_opening('Welcome to Text R', 'Text R')
            if 14 < x < 64 and H - 280 < y < H - 230:
                APPS_FUNCTION_opening('JPB presents', 'Games')
            if 17 < x < 67 and H - 115 < y < H - 65:
                MENU_FUNCTION_Settings()

        pg.display.update()
        clock.tick(FPS)


def OS_FUNCTION_work_space():
    window.fill(black)
    window.blit(DESKTOP_wallpaper, (0, 0))
    pg.draw.rect(window, gray_50, (0, H - 40, W, 40))
    pg.draw.rect(window, black, (7, H - 33, 36, 26))
    window.blit(main_menu_table, (10, H - 33))
    for i in range (len(Working_apps_set)):
        if 'Paint 2.6' in Working_apps_set and Paint_working_check == 'False':
            Paint_working_check = 'True'
            window.blit(paint_logo, (50 + (i * 50), H - 50))
        if 'Text R' in Working_apps_set and Text_R_working_check == 'False':
            Text_R_working_check = 'True'
            window.blit(word_logo, (50 + (i * 50), H - 45))

    while 1:
        time = str(datetime.now().isoformat())
        main_time = (time[0] + time[1] + time[2] + time[3] + '.' + time[5] + time[6] + '.' + time[8] + time[9] +
            '  '+ time[11] + time[12] + ':' + time[14] + time[15])
        time_table = main_font.render(main_time, 2, white, gray_50)
        window.blit(time_table, (W - 170, H - 30))
        x, y = pg.mouse.get_pos()
        mouse_press = pg.mouse.get_pressed()
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        if mouse_press[0]:
            if 7 < x < 69 and H - 37 < y < H - 7:
                OS_FUNCTION_menu(time_table)

        pg.display.update()
        clock.tick(FPS)


def OS_FUNCTION_Jackey_Play_Box():
    window.blit(JPB_wallpaper, (0, 0))
    pg.draw.rect(window, black, (0, 0, W, 40))
    game_num = 1
    games_x = 100
    games_y = 150
    games = ['Hallway fight', 'Pixel tanks']
    while 1:
        time = str(datetime.now().isoformat())
        main_time = (time[0] + time[1] + time[2] + time[3] + '.' + time[5] + time[6] + '.' + time[8] + time[9] +
                     '  ' + time[11] + time[12] + ':' + time[14] + time[15])
        time_table = main_font.render(main_time, 2, white, black)
        window.blit(time_table, (W - 170, 10))
        pg.draw.rect(window, gray_50, (100, 150, 250, 290))
        window.blit(bitva_logo, (games_x, games_y))
        window.blit(tanks_logo, (games_x + 270, games_y))
        game_name_table = main_font.render(games[game_num - 1], 2, white, gray_50)
        window.blit(game_name_table, (102, 402))

        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    OS_FUNCTION_Sys_Starting()
                if i.key == pg.K_SPACE and game_num == 1:
                    play_mortal_humans(0, 0)
                if i.key == pg.K_SPACE and game_num == 2:
                    World_of_tanks(0, 0)

                if i.key == pg.K_RIGHT and game_num < 2:
                    games_x_1 = games_x
                    games_x_2 = games_x - 272
                    game_num += 1
                    for games_x in range (games_x_1, games_x_2, -2):
                        window.blit(JPB_wallpaper, (0, 0))
                        pg.draw.rect(window, black, (0, 0, W, 40))
                        pg.draw.rect(window, gray_50, (100, 150, 250, 290))
                        window.blit(time_table, (W - 170, 10))
                        window.blit(bitva_logo, (games_x, games_y))
                        window.blit(tanks_logo, (games_x + 270, games_y))
                        pg.display.update()
                if i.key == pg.K_LEFT and game_num > 1:
                    games_x_1 = games_x
                    games_x_2 = games_x + 272
                    game_num -= 1
                    for games_x in range (games_x_1, games_x_2, 2):
                        window.blit(JPB_wallpaper, (0, 0))
                        pg.draw.rect(window, black, (0, 0, W, 40))
                        pg.draw.rect(window, gray_50, (100, 150, 250, 290))
                        window.blit(time_table, (W - 170, 10))
                        window.blit(bitva_logo, (games_x, games_y))
                        window.blit(tanks_logo, (games_x + 270, games_y))
                        pg.display.update()

        pg.display.update()
        clock.tick(FPS)


OS_FUNCTION_Sys_Starting()
