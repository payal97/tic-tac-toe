import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (227,0,0)
green = (0,240,0)
blue = (0,0,240)

display_width = 500
display_hieght = 500

gameDisplay = pygame.display.set_mode((display_width, display_hieght))
pygame.display.set_caption("tic-tac-toe")

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
bigfont = pygame.font.SysFont("comicsansms", 50)
markerfont = pygame.font.SysFont(None, 100)

def text_objects(text, colour, size):
        if size == "small":
                textSurface = smallfont.render(text, True, colour)
        elif size == "big":
                textSurface = bigfont.render(text, True, colour)
        elif size == "marker":
                textSurface = markerfont.render(text, True, colour)
        return textSurface, textSurface.get_rect()
        
def message_on_screen(msg, colour, y_disp = 0, size = "small"):
        textSurf, textRect = text_objects(msg, colour, size)
        textRect.center = display_width / 2, (display_hieght / 2) + y_disp
        gameDisplay.blit(textSurf, textRect)

def place_x(cent):
        xSurf, xRect = text_objects("X", blue, 'marker')
        xRect.center = cent
        gameDisplay.blit(xSurf, xRect)

def place_o(cent):
        oSurf, oRect = text_objects("O", green, 'marker')
        oRect.center = cent
        gameDisplay.blit(oSurf, oRect)

def game_board():
        pygame.draw.line(gameDisplay, black, (100,200), (400,200))
        pygame.draw.line(gameDisplay, black, (100,300), (400,300))
        pygame.draw.line(gameDisplay, black, (200,100), (200,400))
        pygame.draw.line(gameDisplay, black, (300,100), (300,400))

def check_win(store):
        t = zip(*store)[0]
        winset = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
        win = True
        for i in winset:
                for j in i:
                        if j not in t:
                                win = False
                                break
                if win == True:
                        return win, i
                else:
                         win = True
        return False, None

def win_line(line):
        
        pos_and_cents = {1: (150,150), 2: (250,150), 3: (350,150), 4: (150,250), 5: (250,250), 6: (350,250), 7: (150,350), 8: (250,350), 9: (350,350)}
        
        horizontal = [(1,2,3), (4,5,6), (7,8,9)]
        vertical = [(1,4,7), (2,5,8), (3,6,9)]
        daigonal1 = (1,5,9)
        daigonal2 = (3,5,7)
        
        if line in horizontal:
                pt1 = (pos_and_cents[line[0]][0] - 50, pos_and_cents[line[0]][1])
                pt2 = (pos_and_cents[line[2]][0] + 50, pos_and_cents[line[2]][1])

        elif line in vertical:
                pt1 = (pos_and_cents[line[0]][0], pos_and_cents[line[0]][1] - 50)
                pt2 = (pos_and_cents[line[2]][0], pos_and_cents[line[2]][1] + 50)

        elif line == daigonal1:
                pt1 = (pos_and_cents[line[0]][0] - 50, pos_and_cents[line[0]][1] - 50)
                pt2 = (pos_and_cents[line[2]][0] + 50, pos_and_cents[line[2]][1] + 50)

        elif line == daigonal2:
                pt1 = (pos_and_cents[line[0]][0] - 50, pos_and_cents[line[0]][1] + 50)
                pt2 = (pos_and_cents[line[2]][0] + 50, pos_and_cents[line[2]][1] - 50)
        
        pygame.draw.line(gameDisplay, red, pt1, pt2, 5)
                

def start_screen():

        screen = True
        
        while screen:
                gameDisplay.fill(white)
                message_on_screen("Tic-Tac-Toe", red, y_disp = -100, size = "big")
                message_on_screen("Press C to continue and Q to quit", black)
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                        screen = False
                                if event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
                                        
                clock.tick(10)

def game_loop():

        fps = 15

        gameOver = False
        gameExit = False

        x_store = []
        o_store = []

        winner = "Draw"
        play_token = "X"

        pos_and_cents = {1: (150,150), 2: (250,150), 3: (350,150), 4: (150,250), 5: (250,250), 6: (350,250), 7: (150,350), 8: (250,350), 9: (350,350)}
        
        while not gameExit:
        
                while gameOver:
                        
                        gameDisplay.fill(white)
                        game_board()
                        
                        for k,i in x_store:
                                place_x(i)
                        for k,i in o_store:
                                place_o(i)
                        if winner != "Draw":
                                win_line(line)

                        message_on_screen(winner, red, -200, "big")
                        message_on_screen("Press P to play again and Q to quit", black, 200)
                        
                        pygame.display.update()
                        
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        gameExit = True
                                        gameOver = False
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                                gameExit = True
                                                gameOver = False
                                        elif event.key == pygame.K_p:
                                                game_loop()
        
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                x, y = event.pos
                                if y > 100 and y < 200:
                                        if x > 100 and x < 200:
                                                position = (1, pos_and_cents[1])
                                        elif x > 200 and x < 300:
                                                position = (2, pos_and_cents[2])
                                        elif x > 300 and x < 400:
                                                position = (3, pos_and_cents[3])
                                        else:
                                                position = -1
                                elif y > 200 and y < 300:
                                        if x > 100 and x < 200:
                                                position = (4, pos_and_cents[4])
                                        elif x > 200 and x < 300:
                                                position = (5, pos_and_cents[5])
                                        elif x > 300 and x < 400:
                                                position = (6, pos_and_cents[6])
                                        else:
                                                position = -1
                                elif y > 300 and y < 400:
                                        if x > 100 and x < 200:
                                                position = (7, pos_and_cents[7])
                                        elif x > 200 and x < 300:
                                                position = (8, pos_and_cents[8])
                                        elif x > 300 and x < 400:
                                                position = (9, pos_and_cents[9])
                                        else:
                                                position = -1
                                else:
                                        position = -1
                                
                                if play_token == "X" and position != -1:
                                        if position[1] not in o_store:
                                                x_store.append(position)
                                                linemade, line = check_win(x_store)
                                                if linemade:
                                                        winner = "Player 1 wins!!!"
                                                        gameOver = True
                                                play_token = "O"
                                                
                                elif play_token == "O" and position != -1:
                                        if position[1] not in x_store:
                                                o_store.append(position)
                                                linemade, line = check_win(o_store)
                                                if linemade:
                                                        winner = "Player 2 wins!!!"
                                                        gameOver = True
                                                play_token = "X"

                gameDisplay.fill(white)
                game_board()
                
                for k,i in x_store:
                        place_x(i)
                for k,i in o_store:
                        place_o(i)

                if play_token == "X" and len(x_store) + len(o_store) < 9:
                        message_on_screen("Player 1", black, y_disp = -200)
                elif play_token == "O" and len(x_store) + len(o_store) < 9:
                        message_on_screen("Player 2", black, y_disp = -200)
                elif len(x_store) + len(o_store) > 9:
                        winner = "Draw"
                        gameOver = True
                
                pygame.display.update()

                clock.tick(fps)

                        
        pygame.quit()
        quit()

start_screen()
game_loop()
