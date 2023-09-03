import os
import pygame

from itertools import cycle

import time
import GamePlay
import Player


class glb:
    screen = None


class Menu:
    def __init__(self):
        init_path = 'game\\'

        files = os.listdir(init_path)

        # pygame setup

        screen = glb.screen
        pygame.display.set_caption('Origami Game')
        logo = pygame.image.load('game\\screen\\unnamed.jpg')
        pygame.display.set_icon(logo)

        clock = pygame.time.Clock()

        img = pygame.image.load('game\\screen\\intro.png')
        screenUpdate = pygame.transform.scale(img, (1280, 720))

        manga_logo = pygame.image.load('game\\screen\\manga_logo.png')
        screenUpdate1 = pygame.transform.scale(manga_logo,
                                               (screen.get_width() / 2 + 680, screen.get_height() / 2 - 215))

        play_bt = pygame.image.load('game\\screen\\play_button.png')
        screenUpdate2 = pygame.transform.scale(play_bt, (440, 77))

        quit_bt = pygame.image.load('game\\screen\\quit_button.png')
        screenUpdate3 = pygame.transform.scale(quit_bt, (440, 77))

        running = True

        screen.blit(screenUpdate, (0, 0))
        pygame.display.update()

        sur = manga_logo.get_rect()
        screen.blit(screenUpdate1, sur)
        pygame.display.update()

        manga_rec = pygame.Rect(screen.get_width() / 2 - 630, 5, screen.get_height() / 2 + 900, 160)

        pygame.draw.rect(screen, 'cyan',
                         pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100))
        play_rec = pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100)
        screen.blit(screenUpdate2, (400, 240))
        pygame.display.update()

        pygame.draw.rect(screen, 'cyan',
                         pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100))
        quit_rec = pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100)
        screen.blit(screenUpdate3, (400, 440))
        pygame.display.update()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                    running = False

            # pygame.draw.rect(screen, 'cyan', pygame.Rect(screen.get_width() / 2 - 630, 5, screen.get_height() / 2 + 900, 160))
            # flip() the display to put your work on screen

            mousePos = pygame.mouse.get_pos()
            ####################################################################
            if play_rec.collidepoint(mousePos):

                screen.blit(screenUpdate2, (400, 240))
                pygame.display.update()
                pygame.draw.rect(screen, 'blue',
                                 pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100))
                screen.blit(screenUpdate2, (400, 240))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    pygame.draw.rect(screen, 'green',
                                     pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100))
                    screen.blit(screenUpdate2, (400, 240))
                    pygame.display.update()
                    Select()
                    break
            else:
                pygame.draw.rect(screen, 'cyan',
                                 pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100))
                play_rec = pygame.Rect(screen.get_width() / 2 - 250, 225, screen.get_height() / 2 + 97, 100)
                screen.blit(screenUpdate2, (400, 240))
                pygame.display.update()

            ##############################################################

            if quit_rec.collidepoint(mousePos):

                screen.blit(screenUpdate3, (400, 440))
                pygame.display.update()
                pygame.draw.rect(screen, 'blue',
                                 pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100))
                screen.blit(screenUpdate3, (400, 440))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    pygame.draw.rect(screen, 'green',
                                     pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100))
                    screen.blit(screenUpdate3, (400, 440))
                    pygame.display.update()
                    pygame.quit()
                    exit(0)
            else:
                pygame.draw.rect(screen, 'cyan',
                                 pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100))
                quit_rec = pygame.Rect(screen.get_width() / 2 - 250, 425, screen.get_height() / 2 + 97, 100)
                screen.blit(screenUpdate3, (400, 440))
                pygame.display.update()

                #########################################################################
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.

        # pygame.quit()


class Select:
    def __init__(self):
        init_path = 'game\\'
        screen = glb.screen
        img = pygame.image.load('game\\screen\\player_menu.png')
        screenUpdate = pygame.transform.scale(img, (1280, 720))
        screen.blit(screenUpdate, (0, 0))
        # pygame.display.update()

        files = os.listdir(init_path + 'players\\')
        files2 = files.copy()
        pl_list0 = cycle(files)
        pl_list1 = cycle(files2)
        # initialize both players
        current = [files[0], files[0]]

        # activate cycle
        next(pl_list0)
        next(pl_list1)

        stats_l, change_l, ready_l = self.player_panel('left', current[0], 1)
        stats_r, change_r, ready_r = self.player_panel('right', current[1], 1)
        # pygame.display.update()

        ready = [False, False]

        back_bt = pygame.Rect(1000, 661, 100, 35)
        battle_bt = pygame.Rect(1130, 661, 100, 35)
        pygame.draw.rect(glb.screen, 'grey', (1000, 661, 100, 35))
        # pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
        pygame.display.update()

        check = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                    running = False

            mousePos = pygame.mouse.get_pos()
            if stats_l.collidepoint(mousePos):
                pygame.draw.rect(screen, 'green', (140 + 0, 600, 105, 40))
                img1 = pygame.image.load(init_path + '\\screen\\' + 'stats_button.png')
                screenUpdate1 = pygame.transform.scale(img1, (img1.get_width(), img1.get_height()))
                glb.screen.blit(screenUpdate1, (142.5 + 0, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.player_panel('left', current[0], 2)
                    pygame.display.update()

            elif change_l.collidepoint(mousePos):
                pygame.draw.rect(glb.screen, 'green', (250 + 0, 600, 102, 40))
                img2 = pygame.image.load(init_path + '\\screen\\' + 'change_button.png')
                screenUpdate2 = pygame.transform.scale(img2, (img2.get_width(), img2.get_height()))
                glb.screen.blit(screenUpdate2, (252.5 + 0, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    check = 1

                if event.type == pygame.MOUSEBUTTONUP:
                    if check == 1:
                        check = 2
                if check == 2:
                    check = 0
                    ready[0] = False
                    current[0] = next(pl_list0)
                    screen.blit(screenUpdate, (0, 0))
                    pygame.draw.rect(glb.screen, 'grey', (1000, 661, 100, 35))
                    img4 = pygame.image.load(init_path + '\\screen\\' + 'back_button.png')
                    screenUpdate4 = pygame.transform.scale(img4, (img4.get_width(), img4.get_height()))
                    glb.screen.blit(screenUpdate4, (1000.25, 660))
                    # pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                    self.player_panel('left', current[0], 1)
                    self.player_panel('right', current[1], 1)

                    if ready[1]:
                        ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                        ready_up = pygame.transform.scale(ready_bt,
                                                          (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                        glb.screen.blit(ready_up, (430, 0))
                    if ready[0] and ready[1]:
                        pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                        battle_b = pygame.image.load(init_path + '\\screen\\' + 'battle_button.png')
                        battle_up = pygame.transform.scale(battle_b, (90, 32))
                        glb.screen.blit(battle_up, (1130.25, 660))
                    pygame.display.update()

            elif ready_l.collidepoint(mousePos):
                pygame.draw.rect(glb.screen, 'green', (360 + 0, 600, 102, 40))
                img3 = pygame.image.load(init_path + '\\screen\\' + 'ready_button.png')
                screenUpdate3 = pygame.transform.scale(img3, (img3.get_width(), img3.get_height()))
                glb.screen.blit(screenUpdate3, (362.5 + 0, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    ready[0] = True
                    ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                    ready_up = pygame.transform.scale(ready_bt,
                                                      (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                    glb.screen.blit(ready_up, (-210, 0))
                    if ready[0] and ready[1]:
                        pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                    pygame.display.update()

            elif stats_r.collidepoint(mousePos):
                pygame.draw.rect(screen, 'green', (140 + 640, 600, 105, 40))
                img1 = pygame.image.load(init_path + '\\screen\\' + 'stats_button.png')
                screenUpdate1 = pygame.transform.scale(img1, (img1.get_width(), img1.get_height()))
                glb.screen.blit(screenUpdate1, (142.5 + 640, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.player_panel('right', current[1], 2)
                    pygame.display.update()

            elif change_r.collidepoint(mousePos):
                pygame.draw.rect(glb.screen, 'green', (250 + 640, 600, 102, 40))
                img2 = pygame.image.load(init_path + '\\screen\\' + 'change_button.png')
                screenUpdate2 = pygame.transform.scale(img2, (img2.get_width(), img2.get_height()))
                glb.screen.blit(screenUpdate2, (252.5 + 640, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    check = 1

                if event.type == pygame.MOUSEBUTTONUP:
                    if check == 1:
                        check = 2
                if check == 2:
                    check = 0
                    ready[1] = False
                    current[1] = next(pl_list1)
                    screen.blit(screenUpdate, (0, 0))
                    pygame.draw.rect(glb.screen, 'grey', (1000, 661, 100, 35))
                    img4 = pygame.image.load(init_path + '\\screen\\' + 'back_button.png')
                    screenUpdate4 = pygame.transform.scale(img4, (img4.get_width(), img4.get_height()))
                    glb.screen.blit(screenUpdate4, (1000.25, 660))
                    # pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                    self.player_panel('left', current[0], 1)
                    self.player_panel('right', current[1], 1)

                    if ready[0]:
                        ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                        ready_up = pygame.transform.scale(ready_bt,
                                                          (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                        glb.screen.blit(ready_up, (-210, 0))
                    if ready[0] and ready[1]:
                        pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                    pygame.display.update()

            elif ready_r.collidepoint(mousePos):
                pygame.draw.rect(glb.screen, 'green', (360 + 640, 600, 102, 40))
                img3 = pygame.image.load(init_path + '\\screen\\' + 'ready_button.png')
                screenUpdate3 = pygame.transform.scale(img3, (img3.get_width(), img3.get_height()))
                glb.screen.blit(screenUpdate3, (362.5 + 640, 602))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    ready[1] = True
                    ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                    ready_up = pygame.transform.scale(ready_bt,
                                                      (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                    glb.screen.blit(ready_up, (430, 0))
                    if ready[0] and ready[1]:
                        pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                        battle_b = pygame.image.load(init_path + '\\screen\\' + 'battle_button.png')
                        battle_up = pygame.transform.scale(battle_b, (90, 32))
                        glb.screen.blit(battle_up, (1130.25, 660))
                    pygame.display.update()

            elif back_bt.collidepoint(mousePos):
                pygame.draw.rect(glb.screen, 'green', (1000, 661, 100, 35))
                img4 = pygame.image.load(init_path + '\\screen\\' + 'back_button.png')
                screenUpdate4 = pygame.transform.scale(img4, (img4.get_width(), img4.get_height()))
                glb.screen.blit(screenUpdate4, (1000.25, 660))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    Menu()

            elif battle_bt.collidepoint(mousePos):
                if ready[0] and ready[1]:
                    pygame.draw.rect(glb.screen, 'green', (1130, 661, 100, 35))
                    battle_b = pygame.image.load(init_path + '\\screen\\' + 'battle_button.png')
                    battle_up = pygame.transform.scale(battle_b, (90, 32))
                    glb.screen.blit(battle_up, (1130.25, 660))
                    pygame.display.update()
                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        Battle(current[0], current[1])
                        break

            else:
                screen.blit(screenUpdate, (0, 0))
                pygame.draw.rect(glb.screen, 'grey', (1000, 661, 100, 35))
                img4 = pygame.image.load(init_path + '\\screen\\' + 'back_button.png')
                screenUpdate4 = pygame.transform.scale(img4, (img4.get_width(), img4.get_height()))
                glb.screen.blit(screenUpdate4, (1000.25, 660))
                self.player_panel('left', current[0], 1)
                self.player_panel('right', current[1], 1)

                if ready[0]:
                    ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                    ready_up = pygame.transform.scale(ready_bt,
                                                      (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                    glb.screen.blit(ready_up, (-210, 0))

                if ready[1]:
                    ready_bt = pygame.image.load(init_path + '\\screen\\' + 'ready_stamp.png')
                    ready_up = pygame.transform.scale(ready_bt,
                                                      (ready_bt.get_width() - 400, ready_bt.get_height() - 400))
                    glb.screen.blit(ready_up, (430, 0))

                if ready[0] and ready[1]:
                    pygame.draw.rect(glb.screen, 'black', (1130, 661, 100, 35))
                    battle_b = pygame.image.load(init_path + '\\screen\\' + 'battle_button.png')
                    battle_up = pygame.transform.scale(battle_b, (90, 32))
                    glb.screen.blit(battle_up, (1130.25, 660))

                pygame.display.update()

        pygame.display.update()

    def player_panel(self, side, name, menu):
        if side == 'left':
            offset = 0
        else:
            offset = 640
        init_path = 'game\\'
        path = init_path + 'players\\' + name + '\\menu_' + str(menu) + '.png'
        img = pygame.image.load(path)
        screenUpdate = pygame.transform.scale(img, (img.get_width(), img.get_height()))
        glb.screen.blit(screenUpdate, (80 + offset, 80))

        name = pygame.image.load(init_path + 'players\\' + name + '\\name_label.png')
        name_up = pygame.transform.scale(name, (name.get_width(), name.get_height()))
        glb.screen.blit(name_up, (40 + offset, 40))

        stats_bt = pygame.Rect(140 + offset, 600, 102, 40)
        change_bt = pygame.Rect(250 + offset, 600, 102, 40)
        ready_bt = pygame.Rect(360 + offset, 600, 102, 40)

        if menu == 1:
            pygame.draw.rect(glb.screen, 'white', (140 + offset, 600, 105, 40))
            pygame.draw.rect(glb.screen, 'white', (250 + offset, 600, 102, 40))
            pygame.draw.rect(glb.screen, 'white', (360 + offset, 600, 102, 40))

        img1 = pygame.image.load(init_path + '\\screen\\' + 'stats_button.png')
        screenUpdate1 = pygame.transform.scale(img1, (img1.get_width(), img1.get_height()))
        glb.screen.blit(screenUpdate1, (142.5 + offset, 602))

        img2 = pygame.image.load(init_path + '\\screen\\' + 'change_button.png')
        screenUpdate2 = pygame.transform.scale(img2, (img2.get_width(), img2.get_height()))
        glb.screen.blit(screenUpdate2, (252.5 + offset, 602))

        img3 = pygame.image.load(init_path + '\\screen\\' + 'ready_button.png')
        screenUpdate3 = pygame.transform.scale(img3, (img3.get_width(), img3.get_height()))
        glb.screen.blit(screenUpdate3, (362.5 + offset, 602))

        return (stats_bt, change_bt, ready_bt)


class Battle:

    def __init__(self, player0, player1):
        self.player0 = player0
        self.player1 = player1
        self.read_players()

        self.dir0 = player0
        self.dir1 = player1

        # controller of graphics and game:
        self.gc = GamePlay.Game(self.player0, self.player1, self)

        self.health0 = self.player0.health
        self.health1 = self.player1.health

        screen = glb.screen
        self.battle_start()
        pygame.display.update()

        self.text = None
        self.running = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                    running = False

            mousePos = pygame.mouse.get_pos()

            if self.home_rec.collidepoint(mousePos):
                pygame.draw.rect(screen, 'green', (1200, 350, 50, 50))
                home_bt = img = pygame.image.load('game\\screen\\home_button.png')
                home_up = pygame.transform.scale(home_bt, (50, 50))
                screen.blit(home_up, (1190, 350))
                pygame.display.update()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    Menu()
                    break

            else:
                self.background()
                self.health_meter()
                self.move_panel('left')
                self.move_panel('right')
                # self.attack_pointer(1)
                # pygame.display.update()
                if self.running:
                    (move0, move1) = self.key_listener('attack', 'none')
                    self.attack_process(move0, move1)
                pygame.display.update()

    def background(self):
        img = pygame.image.load('game\\screen\\arena.png')
        screenUpdate = pygame.transform.scale(img, (1280, 720))
        glb.screen.blit(screenUpdate, (0, 0))

        pygame.draw.rect(glb.screen, 'orange', (1200, 350, 50, 50))
        home_rec = pygame.Rect((1200, 350, 50, 50))
        home_bt = img = pygame.image.load('game\\screen\\home_button.png')
        home_up = pygame.transform.scale(home_bt, (50, 50))
        glb.screen.blit(home_up, (1190, 350))

        img1 = pygame.image.load('game\\players\\' + self.dir1 + '\\battle_1.png')
        up1 = pygame.transform.scale(img1, (img1.get_width(), img1.get_height()))
        glb.screen.blit(up1, (950, 0))

        img0 = pygame.image.load('game\\players\\' + self.dir0 + '\\battle_0.png')
        up0 = pygame.transform.scale(img0, (img0.get_width(), img0.get_height()))
        glb.screen.blit(up0, (0, 400))

        self.home_rec = home_rec

    def read_players(self):
        self.player0 = Player.Player(self.player0)
        self.player1 = Player.Player(self.player1)

    def health_meter(self):
        width = self.calc_health()

        pygame.font.init()
        font = pygame.font.SysFont("Grobold", 30)
        pygame.draw.rect(glb.screen, 'aliceblue', (20, 280, 310, 140))
        # right player
        text = font.render(self.player1.name, True, 'darkslategrey')
        glb.screen.blit(text, (35, 290))
        text = font.render('HP', True, 'darkslategrey')
        glb.screen.blit(text, (35, 310))
        pygame.draw.rect(glb.screen, 'chartreuse4', (70, 312, 240, 15))

        # calculate remaining health
        pygame.draw.rect(glb.screen, 'chartreuse', (70, 312, width[1], 15))
        ##############################################################
        # left player
        text = font.render(self.player0.name, True, 'darkslategrey')
        glb.screen.blit(text, (35, 360))
        text = font.render('HP', True, 'darkslategrey')
        glb.screen.blit(text, (35, 380))
        pygame.draw.rect(glb.screen, 'chartreuse4', (70, 382, 240, 15))

        # calculate remaining health
        pygame.draw.rect(glb.screen, 'chartreuse', (70, 382, width[0], 15))

        # pygame.display.update()

    def calc_health(self):
        width = 240
        remaining = [self.player0.health / self.health0, self.player1.health / self.health1]

        return [int(width * remaining[0]), int(width * remaining[1])]

    def move_panel(self, side):
        if side == 'left':
            offset1 = 0
            offset2 = 0
            player = self.player1
        else:
            offset1 = 850
            offset2 = 500
            player = self.player0

        move = pygame.image.load('game\\screen\\move_panel.png')
        move_up = pygame.transform.scale(move, (400, 200))
        glb.screen.blit(move_up, (0 + offset1, 0 + offset2))

        pygame.font.init()
        font = pygame.font.SysFont("Grobold", 28)

        if len(player.moves) >= 2:
            string1 = player.moves[0]['name'] + ' |' + str(player.moves[0]['size']) + '   ' + player.moves[1][
                'name'] + ' |' + str(player.moves[1]['size'])
        elif len(player.moves) == 1:
            string1 = player.moves[0]['name'] + ' |' + str(player.moves[0]['size'])
        text = font.render(string1, True, 'cornsilk')
        glb.screen.blit(text, (20 + offset1, 30 + offset2))

        if len(player.moves) == 4:
            string2 = player.moves[2]['name'] + ' |' + str(player.moves[2]['size']) + '   ' + player.moves[3][
                'name'] + ' |' + str(player.moves[3]['size'])
        if len(player.moves) == 3:
            string2 = player.moves[2]['name'] + ' |' + str(player.moves[2]['size'])
        text = font.render(string2, True, 'cornsilk')
        glb.screen.blit(text, (20 + offset1, 100 + offset2))

        n = ' '
        if len(player.moves) == 4 and player.moves[3]['type'] == 'Neutral':
            n = '(Neutral)'
        string3 = '(Defense)' + '                    ' + n
        text = font.render(string3, True, 'cornsilk')
        glb.screen.blit(text, (20 + offset1, 130 + offset2))

    def shield_pointer(self, side):
        if side == 'left':
            offset1 = 0
            offset2 = 0
        else:
            offset1 = 850
            offset2 = 500
        arrow = pygame.image.load('game\\screen\\arrow.png')
        arrow_up = pygame.transform.scale(arrow, (30, 30))
        glb.screen.blit(arrow_up, (50 + offset1, 150 + offset2))

    def attack_pointer(self, index, side):
        if side == 'left':
            offset1 = 0
            offset2 = 0
            player = self.player1
        else:
            offset1 = 850
            offset2 = 500
            player = self.player0

        if index == 0:
            arrow = pygame.image.load('game\\screen\\arrow.png')
            arrow_up = pygame.transform.scale(arrow, (30, 30))
            glb.screen.blit(arrow_up, (50 + offset1, 55 + offset2))
        elif index == 1:
            arrow = pygame.image.load('game\\screen\\arrow.png')
            arrow_up = pygame.transform.scale(arrow, (30, 30))
            glb.screen.blit(arrow_up, (240 + offset1, 55 + offset2))
        elif index == 3:
            arrow = pygame.image.load('game\\screen\\arrow.png')
            arrow_up = pygame.transform.scale(arrow, (30, 30))
            glb.screen.blit(arrow_up, (240 + offset1, 150 + offset2))

    def key_listener(self, mode, side):
        if side == 'left':
            ok = pygame.K_KP_ENTER
            player = self.player1
        else:
            ok = pygame.K_SPACE
            player = self.player0

        if mode == 'attack':
            indexl = 0
            indexr = 0

            ready1 = False
            ready0 = False
            while True:
                self.attack_pointer(indexl, 'left')
                self.attack_pointer(indexr, 'right')
                if ready1:
                    lock = pygame.image.load('game\\screen\\lock.png')
                    lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                    glb.screen.blit(lock_up, (130 + 850, 25 + 500))
                if ready0:
                    lock = pygame.image.load('game\\screen\\lock.png')
                    lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                    glb.screen.blit(lock_up, (130, 25))
                pygame.display.update()
                self.move_panel('left')
                self.move_panel('right')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)

                    if event.type == pygame.KEYDOWN:
                        if not ready0:
                            if event.key == pygame.K_RIGHT and indexl == 0 and len(self.player1.moves) > 1:
                                #index = 1
                                indexl = 1
                            if event.key == pygame.K_LEFT and indexl == 1:
                                #index = 0
                                indexl = 0
                            if event.key == pygame.K_DOWN and indexl == 1 and len(self.player1.moves) > 3:
                                #index += 2
                                indexl += 2
                            if event.key == pygame.K_UP and indexl > 1:
                                indexl -= 2
                        if not ready1:
                            if event.key == pygame.K_d and indexr == 0 and len(self.player0.moves) > 1:
                                # index = 1
                                indexr = 1
                            if event.key == pygame.K_a and indexr == 1:
                                # index = 0
                                indexr = 0
                            if event.key == pygame.K_s and indexr == 1 and len(self.player0.moves) > 3:
                                #index += 2
                                indexr += 2
                            if event.key == pygame.K_w and indexr > 1:
                                indexr -= 2

                        if event.key == pygame.K_SPACE:
                            ready1 = True
                            #self.move_panel('left')
                            self.move_panel('right')
                            lock = pygame.image.load('game\\screen\\lock.png')
                            lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                            glb.screen.blit(lock_up, (130 + 850, 25 + 500))
                            pygame.display.update()
                            #self.text = player.name + ' used ' + player.moves[index]['name']
                            #return self.text
                        if event.key == pygame.K_RETURN:
                            ready0 = True
                            lock = pygame.image.load('game\\screen\\lock.png')
                            lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                            self.move_panel('left')
                            glb.screen.blit(lock_up, (130, 25))
                            #self.move_panel('right')
                            pygame.display.update()
                            # self.text = player.name + ' used ' + player.moves[index]['name']
                            #return self.text
                        if ready0 and ready1:
                            lock = pygame.image.load('game\\screen\\lock.png')
                            lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                            self.move_panel('left')
                            glb.screen.blit(lock_up, (130, 25))
                            self.move_panel('right')
                            lock = pygame.image.load('game\\screen\\lock.png')
                            lock_up = pygame.transform.scale(lock, (lock.get_width(), lock.get_height()))
                            glb.screen.blit(lock_up, (130 + 850, 25 + 500))
                            pygame.display.update()
                            pygame.time.wait(800)

                            return (indexr, indexl)

        else:
            self.move_panel(side)
            self.shield_pointer(side)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == ok:
                        text = player.name + ' used ' + player.moves[2]['name'] + ' and avoided the attack'
                        return text

    def slow_text(self, text):
        # text = '123456789012345678901234567890'
        pygame.font.init()
        font = pygame.font.SysFont("Grobold", 70)
        words = text.split()
        count = 0
        push = 0
        for word in words:
            word += ' '
            count += len(word)
            for i, letter in enumerate(word):
                pygame.time.wait(60)
                text = font.render(letter, True, 'black')
                if count <= 25:
                    glb.screen.blit(text, (350 + (push + i) * 32, 330))
                else:
                    j = i - 25
                    glb.screen.blit(text, (350 + (push + j) * 32, 330 + 80))
                pygame.display.update()
            push += len(word)
        pygame.time.wait(700)

    def battle_start(self):
        self.background()
        self.health_meter()
        self.move_panel('left')
        self.move_panel('right')
        pygame.display.update()
        title = self.player0.name + ' vs ' + self.player1.name
        self.slow_text(title)
        pygame.time.wait(200)
        self.background()
        self.health_meter()
        self.move_panel('left')
        self.move_panel('right')
        pygame.display.update()
        title = 'BATTLE START !'
        self.slow_text(title)
        pygame.time.wait(500)

    def battle_end(self, title):
        self.running = False
        self.background()
        self.health_meter()
        self.move_panel('left')
        self.move_panel('right')
        pygame.display.update()
        self.slow_text(title)
        pygame.time.wait(200)
        self.background()
        self.health_meter()
        self.move_panel('left')
        self.move_panel('right')
        pygame.display.update()
        self.slow_text('PRESS HOME BUTTON')
        pygame.time.wait(300)

    def attack_process(self, move0, move1):
        self.player0.moves[move0]['size'] -= 1
        self.player1.moves[move1]['size'] -= 1

        self.background()
        self.health_meter()

        pygame.display.update()
        self.gc.check_turn(move0, move1)
        message = f"{self.gc.attacker.name} used {self.gc.attacker.moves[self.gc.attack_move]['name']}"
        self.slow_text(message)

        self.defense_process()
        if self.gc.damage():
            return 1
        self.background()
        self.health_meter()
        pygame.display.update()
        self.gc.pending()
        message = f"{self.gc.attacker.name} used {self.gc.attacker.moves[self.gc.attack_move]['name']}"
        self.slow_text(message)
        self.defense_process()
        if self.gc.damage():
            return 1
        self.background()
        self.health_meter()
        pygame.display.update()
        self.gc.check_moves(move0, move1)

    def defense_process(self):
        self.background()
        self.health_meter()

        pygame.display.update()
        message = f"{self.gc.opponent.name} defend ? [Press ENTER] "
        self.slow_text(message)
        pygame.time.wait(700)

        side = ''
        if self.gc.opponent == self.player1:
            side = 'left'
        else:
            side = 'right'

        self.background()
        self.health_meter()
        text = self.key_listener('defense', side)
        pygame.display.update()
        for i in ['3', '2', '1']:
            t_end = time.time() + 0.4
            while time.time() < t_end:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            text = self.gc.use_shield('y')
                            self.slow_text(text)
                            return True
            self.slow_text(i)
            #pygame.time.wait(300)
            self.background()
            self.health_meter()
            text = self.key_listener('defense', side)
            #pygame.display.update()
            #pygame.time.wait(300)

        self.gc.use_shield('n')
        return False




class Screen:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    glb.screen = screen
