"""
    Importing the required libraries required for the execution of the game.
    pygame for pygame usage, and time for getting time of each run
"""
import pygame
import time

pygame.init()

"""
    Sets the base screen resolution variables and colour variables required
    globally through the program.
"""
display_width = 1000
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (150, 119, 91)
green = (50, 87, 27)

"""
    mine_x_pos[] and mine_y_pos[] stores the (x,y) coordinates of the
    mines, required for collision check
"""
mine_x_pos = [12, 82, 152, 152, 12, 222, 222, 292, 292, 362, 362, 432,
              502, 572, 572, 642, 782, 782, 712, 852, 852, 922, 922]

mine_y_pos = [440, 160, 300, 440, 580, 160, 580, 160, 300, 300, 580,
              440, 300, 160, 580, 440, 300, 440, 160, 160, 580, 440, 580]

"""
    missile_x_pos[], missile_y_pos[], and missile_orientation[] stores
    (x,y) coordinates and orientation of the moving objects required for
     collision check and motion. In missile_orientation[], 0 is left to
     right, while 1 is from right to left.
"""
missile_x_pos = [15, 200, 400, 500]
missile_y_pos = [525, 395, 395, 245]
missile_orientation = [0, 0, 1, 0]

"""
    Create multiple variables that load the required images and render
    the required fonts used in the program
"""
car_img_up = pygame.image.load('../img/tanku.png')
car_img_right = pygame.image.load('../img/tankr.png')
car_img_left = pygame.image.load('../img/tankl.png')
car_img_down = pygame.image.load('../img/tankd.png')
background_img = pygame.image.load('../img/back.jpg')
missile_img_left = pygame.image.load('../img/missilel.png')
missile_img_right = pygame.image.load('../img/missiler.png')
mine_img = pygame.image.load('../img/mine.png')
explosion_img = pygame.image.load('../img/exp.png')

font_small = pygame.font.SysFont(None, 35)
font_large = pygame.font.SysFont(None, 70)
title = font_large.render("TANK BLITZ", True, red)
text_player1_win = font_large.render("Player 1 WINS OVERALL!!!", True, red)
text_player2_win = font_large.render("Player 2 WINS OVERALL!!!", True, red)
text_players_tie = font_large.render("IT'S A TIE !!!", True, red)
text_start = font_small.render("Start", True, white)
text_finish = font_small.render("Finish", True, white)
text_player1 = font_small.render("Player 1", True, white)
text_player2 = font_small.render("Player 2", True, white)
text_round_player1 = font_small.render("Player 1 wins the round", True, white)
text_round_player2 = font_small.render("Player 2 wins the round", True, white)

"""
    Initializing screen, title, and frame clock
"""
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tank Blitz')


"""
    The following 8 functions are used to display the sprites used,
    including the 4 orientations of the tank, the mines, the explosions,
    and two orientaions of the missiles
"""


def move_car_up(x, y):
    game_display.blit(car_img_up, (x, y))


def move_car_right(x, y):
    game_display.blit(car_img_right, (x, y))


def move_car_left(x, y):
    game_display.blit(car_img_left, (x, y))


def move_car_down(x, y):
    game_display.blit(car_img_down, (x, y))


def deploy_mine(x, y):
    game_display.blit(mine_img, (x, y))


def deploy_explosion(x, y):
    game_display.blit(explosion_img, (x, y))


def move_missile_left(x, y):
    game_display.blit(missile_img_left, (x, y))


def move_missile_right(x, y):
    game_display.blit(missile_img_right, (x, y))


def game_loop():
    """
        Defining various variables in game_loop() scope that
        are used later
    """
    start_time_player1 = time.time()
    start_time_player2 = time.time()
    game_exit = False
    current_player = 1
    x = 500
    y = display_height - 5
    x_change = 0
    y_change = 0
    tank_orientation_flag = 3
    round_counter = 2
    missile_speed = int(round_counter / 2) * 3
    player1_score = 0
    player2_score = 0
    player1_total_win = 0
    player2_total_win = 0
    player1_max_distance = 0
    player2_max_distance = 0
    while not game_exit:

        """
            increments missile_speed based on current round, and also
            on which current_player is winning
        """
        if current_player == 1:
            missile_speed = int(round_counter / 2) * 3 * \
                (player1_total_win + 1)
        else:
            missile_speed = int(round_counter / 2) * 3 * \
                (player2_total_win + 1)

        """
            Sets the background images, bars, and text
        """
        game_display.blit(background_img, (0, 90))
        text_current_round = font_small.render(
            "Round:  " + str(int(round_counter / 2)), True, white)
        text_player1_wins = font_small.render(
            "P-1:  " + str(player1_total_win), True, white)
        text_player2_wins = font_small.render(
            "P-2:  " + str(player2_total_win), True, white)
        pygame.draw.rect(game_display, black, (0, 0, display_width, 90))
        pygame.draw.rect(game_display, brown, (0, 227, display_width, 70))
        pygame.draw.rect(game_display, brown, (0, 367, display_width, 70))
        pygame.draw.rect(game_display, brown, (0, 507, display_width, 70))
        pygame.draw.rect(game_display, green, (0, 647, display_width, 73))
        pygame.draw.rect(game_display, green, (0, 90, display_width, 70))
        game_display.blit(text_player1_wins, (885, 15))
        game_display.blit(text_player2_wins, (885, 57))
        game_display.blit(title, (325, 20))
        game_display.blit(text_current_round, (70, 57))

        """
            Controls the movement of the tank using key events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -70
                tank_orientation_flag = 1
            if event.key == pygame.K_RIGHT:
                x_change = 70
                tank_orientation_flag = 2
            if event.key == pygame.K_UP:
                y_change = -70
                tank_orientation_flag = 3
            if event.key == pygame.K_DOWN:
                y_change = 70
                tank_orientation_flag = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_change = 0
                y_change = 0
        time.sleep(0.12)

        """
            This if statement is used to alternate between player 1 and 2, and
            thus updates the sprite location, calculates the score, and
            displays it
        """
        if current_player == 1:
            game_display.blit(text_start, (480, 669.5))
            game_display.blit(text_finish, (480, 112.5))
            game_display.blit(text_player1, (70, 15))
            temp_score = int((display_height - 25 - y) / 70)
            if temp_score > player1_max_distance:
                player1_max_distance = temp_score
            temp_score_a = int(player1_max_distance / 2)
            temp_score_b = player1_max_distance - temp_score_a
            player1_score = (temp_score_b * 10) + (temp_score_a * 20)
            text_score_player1 = font_small.render(
                "Score: " + str(player1_score), True, white)
            game_display.blit(text_score_player1, (710, 36))
        else:
            game_display.blit(text_finish, (480, 669.5))
            game_display.blit(text_start, (480, 112.5))
            game_display.blit(text_player2, (70, 15))
            temp_score = int((y - 90) / 70)
            if temp_score > player2_max_distance:
                player2_max_distance = temp_score
            temp_score_a = int(player2_max_distance / 2)
            temp_score_b = player2_max_distance - temp_score_a
            player2_score = (temp_score_b * 10) + (temp_score_a * 20)
            text_score_player2 = font_small.render(
                "Score: " + str(player2_score), True, white)
            game_display.blit(text_score_player2, (710, 36))

        """
            Deploys the  stationary and moving obstacles on the screen, and
            updates location and orientation for moving obstacles
        """
        for i in range(0, 23):
            deploy_mine(mine_x_pos[i], mine_y_pos[i])

        for i in range(0, 4):
            if missile_orientation[i] == 0:
                move_missile_right(missile_x_pos[i], missile_y_pos[i])
                missile_x_pos[i] += missile_speed
            else:
                move_missile_left(missile_x_pos[i], missile_y_pos[i])
                missile_x_pos[i] -= missile_speed
            if missile_x_pos[i] > display_width - 77:
                missile_x_pos[i] = display_width - 77
                missile_orientation[i] = 1
            elif missile_x_pos[i] < 12:
                missile_x_pos[i] = 12
                missile_orientation[i] = 0

        """
            Updates the value of x and y for the tank based on the key
            input values
        """
        x += x_change
        y += y_change
        if tank_orientation_flag == 1:
            move_car_left(x, y)
        elif tank_orientation_flag == 2:
            move_car_right(x, y)
        elif tank_orientation_flag == 3:
            move_car_up(x, y)
        elif tank_orientation_flag == 4:
            move_car_down(x, y)

        """
            Prevents the tank sprite from going out of defined resolution
        """
        if x > display_width - 77:
            x = display_width - 77
        if x < 12:
            x = 12
        if y > display_height - 70:
            y = display_height - 70
        if y < 91:
            y = 91

        """
            Loop to check for collision of tank with stationary objects. If
            collided,  it checks for who won first based on score, then time,
            and then resets game for other player
        """
        for i in range(0, 23):
            if mine_x_pos[i] - 35 < x < mine_x_pos[i] +\
                    35 and mine_y_pos[i] - 35 < y < mine_y_pos[i] + 35:
                deploy_explosion(mine_x_pos[i], mine_y_pos[i])
                if current_player == 1:
                    current_player = 2
                    x = 500
                    y = 91
                    tank_orientation_flag = 4
                    final_time_player1 = time.time() - start_time_player1
                    pygame.display.update()
                    time.sleep(0.4)
                    start_time_player2 = time.time()
                else:
                    current_player = 1
                    x = 500
                    y = display_height - 5
                    tank_orientation_flag = 3
                    final_time_player2 = time.time() - start_time_player2
                round_counter += 1
                if round_counter % 2 == 0:
                    pygame.draw.rect(
                        game_display, black, (0, 0, display_width, 90))
                    if player1_score > player2_score:
                        player1_total_win += 1
                        game_display.blit(text_round_player1, (375, 36))
                    elif player2_score > player1_score:
                        player2_total_win += 1
                        game_display.blit(text_round_player2, (375, 36))
                    else:
                        if final_time_player1 < final_time_player2:
                            player1_total_win += 1
                            game_display.blit(text_round_player1, (375, 36))
                        else:
                            player2_total_win += 1
                            game_display.blit(text_round_player2, (375, 36))
                    pygame.display.update()
                    time.sleep(1)
                    player1_score = 0
                    player2_score = 0
                    player1_max_distance = 0
                    player2_max_distance = 0
                    start_time_player1 = time.time()

        """
            Loop to check for collision of tank with moving objects. If
            collided,  it checks for who won first based on score, then time,
            and then resets game for other player
        """
        for i in range(0, 4):
            if missile_x_pos[i] - 60 < x < missile_x_pos[i] +\
                    60 and missile_y_pos[i] - 50 < y < missile_y_pos[i] + 10:
                deploy_explosion(x, y)
                if current_player == 1:
                    current_player = 2
                    x = 500
                    y = 91
                    tank_orientation_flag = 4
                    final_time_player1 = time.time() - start_time_player1
                    pygame.display.update()
                    time.sleep(0.4)
                    start_time_player2 = time.time()
                else:
                    current_player = 1
                    x = 500
                    y = display_height - 5
                    tank_orientation_flag = 3
                    final_time_player2 = time.time() - start_time_player2
                round_counter += 1
                if round_counter % 2 == 0:
                    pygame.draw.rect(
                        game_display, black, (0, 0, display_width, 90))
                    if player1_score > player2_score:
                        player1_total_win += 1
                        game_display.blit(text_round_player1, (375, 36))
                    elif player2_score > player1_score:
                        player2_total_win += 1
                        game_display.blit(text_round_player2, (375, 36))
                    else:
                        if final_time_player1 < final_time_player2:
                            player1_total_win += 1
                            game_display.blit(text_round_player1, (375, 36))
                        else:
                            player2_total_win += 1
                            game_display.blit(text_round_player2, (375, 36))
                    pygame.display.update()
                    time.sleep(1)
                    player1_score = 0
                    player2_score = 0
                    player1_max_distance = 0
                    player2_max_distance = 0
                    start_time_player1 = time.time()

        """
            Executes once 10 rounds are completed. Compares the number of
            victories of player 1 and player 2, and declares the overall
            winner or if it is a tie
        """
        if round_counter >= 22:
            pygame.draw.rect(game_display, black, (0, 0, display_width, 90))
            if player1_total_win > player2_total_win:
                game_display.blit(text_player1_win, (250, 20))
            elif player2_total_win > player1_total_win:
                game_display.blit(text_player2_win, (250, 20))
            else:
                game_display.blit(text_players_tie, (375, 20))
            game_exit = True

        """
            Check if player 1 or 2 completes the path, and if completed,
            either resets to next player directly, or calculates,
            compares, and displays score for that round.
        """
        if current_player == 1 and y < 160:
            current_player = 2
            x = 500
            y = 91
            tank_orientation_flag = 4
            round_counter += 1
            final_time_player1 = time.time() - start_time_player1
            start_time_player2 = time.time()
        elif current_player == 2 and y > display_height - 95:
            current_player = 1
            x = 500
            y = display_height - 5
            tank_orientation_flag = 3
            round_counter += 1
            pygame.draw.rect(game_display, black, (0, 0, display_width, 90))
            final_time_player2 = time.time() - start_time_player2
            if player1_score > player2_score:
                player1_total_win += 1
                game_display.blit(text_round_player1, (375, 36))
            elif player2_score > player1_score:
                player2_total_win += 1
                game_display.blit(text_round_player2, (375, 36))
            else:
                if final_time_player2 > final_time_player1:
                    player1_total_win += 1
                    game_display.blit(text_round_player1, (375, 36))
                else:
                    player2_total_win += 1
                    game_display.blit(text_round_player2, (375, 36))
            player1_score = 0
            player2_score = 0
            player1_max_distance = 0
            player2_max_distance = 0
            pygame.display.update()
            time.sleep(1)
            start_time_player1 = time.time()
        pygame.display.update()
        clock.tick(60)


game_loop()
time.sleep(2)
pygame.quit()
quit()
