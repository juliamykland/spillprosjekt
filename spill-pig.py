import pygame
from pylab import *
import random
import time
pygame.init()
random.seed(1)
pygame.mixer.init()

#variabler
white = (255,255,255)
red = ((255,0,0))
svart = ((0, 0, 0))
bredde = 1200
hoyde = 700
spillerbredde = 100
spillerhoyde = 70
redballbredde = 40
redballhoyde = 40
poeng = 0
font = pygame.font.SysFont("comicsansms", 50)
clock = pygame.time.Clock()
greenballbredde = 40
greenballhoyde = 40
blueballbredde = 50
blueballhoyde = 50
crash_sound = pygame.mixer.Sound("pig_oink.wav") 
gametime = 30
gameover=False



size = (bredde,hoyde)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")   
done = False


bg = pygame.image.load("bg.png")
bg_tilpasset = pygame.transform.scale(bg,(size))
screen.blit(bg_tilpasset, (0, 0))


spiller = pygame.image.load("pig.png")
spiller_size = pygame.transform.scale(spiller, (spillerbredde,spillerhoyde))
spillerx = 300
spillery = 300
dx = dy = 30
screen.blit(spiller_size, (spillerx, spillery))

redball = pygame.image.load("red.png")
redball_size = pygame.transform.scale(redball, (redballbredde, redballhoyde))
redx = randint(25, bredde-25)
redy = randint (25, hoyde-25)
drx=10
dry=10
screen.blit(redball_size, (redx, redy))

greenball = pygame.image.load("green.png")
greenball_size = pygame.transform.scale(greenball, (greenballbredde, greenballhoyde))
greenx = randint (25, bredde-25)
greeny = randint (25, hoyde-25)
dgx = 15
dgy = 15
screen.blit(greenball_size, (dgx, dgy))

blueball = pygame.image.load("blue.png")
blueball_size = pygame.transform.scale(blueball, (blueballbredde, blueballhoyde))
bluex = 400
bluey = 500
dbx = 20
dby = 20
screen.blit(blueball_size, (dbx, dby))

def wait_for_keypressed():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            

def gamewindow (x0, y0, xr, yr, text1, x1, y1, text2, x2, y2, text3, x3, y3):
    global screen
    pygame.draw.rect(screen, svart, (x0, y0, xr, yr), 0)
    font_1 = pygame.font.SysFont("comicsansms", 30)
    screen.blit(font_1.render(text1, 1, red), (x0+x1, y0+y1))
    screen.blit(font_1.render(text2, 1, red), (x0+x2, y0+y2))
    screen.blit(font_1.render(text3, 1, red), (x0+x3, y0+y3))
    pygame.display.update()
    wait_for_keypressed()
    return()


fil = open("highscore.txt", "r")
old_highscore = int(fil.read())
fil.close()


gamewindow((bredde/4), (hoyde/4), (bredde/3), (hoyde/3), "Welcome", 30, 30, "Current highscore: "+str(old_highscore), 30, 60, "Hit any key to stat", 30, 90)
starttime = time.time()

while not done:
    actualtime = time.time() - starttime
    remainingtime = gametime - actualtime
    timetxt = "Time: "+str(int(remainingtime))
    timetext = font.render(timetxt, 1, red)
    if remainingtime < 0:
        done = True
        gameover = True
    redx = redx + drx
    redy = redy + dry
    if redx<0 or redx>bredde-redballbredde:
        drx = -drx
    if redy<0 or redy>hoyde-redballhoyde:
        dry = -dry
    greenx = greenx + dgx
    greeny = greeny + dgy
    if greenx < 0 or greenx > bredde - greenballbredde:
        dgx = -dgx
    if greeny < 0 or greeny > hoyde - greenballhoyde:
        dgy = -dgy
    bluex = bluex + dbx
    bluey = bluey + dby
    if bluex < 0 or bluex > bredde - blueballbredde:
        dbx = -dbx
    if bluey < 0 or bluey > hoyde - blueballhoyde:
        dby = -dby
    score = "Score: "+str(poeng)
    scoretext = font.render(score, 1, red)
    if abs (redx - spillerx) < spillerbredde  and abs (redy - spillery) < spillerhoyde:
        poeng = poeng + 1
        redx = randint(redballbredde, bredde-redballbredde)
        redy = randint (redballhoyde, hoyde-redballhoyde)
        crash_sound.play()
        pygame.mixer.music.stop()
    if abs (greenx - spillerx) < 20 and abs (greeny - spillery) < 20:
        poeng = poeng + 2
        greenx = randint (greenballbredde, bredde-greenballbredde)
        greeny = randint (greenballhoyde, hoyde-greenballhoyde)
        crash_sound.play()
        pygame.mixer.music.stop()
    if abs (bluex - spillerx) < 30 and abs (bluey - spillery) < 30:
        poeng = poeng + 2
        bluex = randint (blueballbredde, bredde-blueballbredde)
        bluey = randint (blueballhoyde, hoyde-blueballhoyde)
        crash_sound.play()
        pygame.mixer.music.stop()

#piltaster        
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            tmpspillerx=spillerx
            tmpspillery=spillery
            
        if e.type == pygame.QUIT:
                done = True 
                
    keys = pygame.key.get_pressed()
                
    if keys[pygame.K_LEFT]:
        tmpspillerx = spillerx - dx   
                    
        if tmpspillerx >0 and tmpspillerx < bredde-spillerbredde:
            spillerx=tmpspillerx
            
    if keys[pygame.K_RIGHT]:
        tmpspillerx = spillerx + dx
                    
        if tmpspillerx >0 and tmpspillerx < bredde-spillerbredde:
            spillerx=tmpspillerx
            
    if keys[pygame.K_DOWN]:
        tmpspillery = spillery + dy
        
        if tmpspillery >0 and tmpspillery < hoyde-spillerhoyde:
            spillery=tmpspillery
        
    if keys[pygame.K_UP]:
        tmpspillery = spillery - dy

        if tmpspillery >0 and tmpspillery < hoyde-spillerhoyde:
            spillery=tmpspillery

            
    
    
    clock.tick(30)        
    screen.blit(bg_tilpasset, (0, 0))        
    screen.blit(spiller_size, (spillerx, spillery))
    screen.blit(redball_size, (redx, redy))
    screen.blit(scoretext, (20, 20))
    screen.blit(timetext, (800,20))
    screen.blit(greenball_size, (greenx, greeny))
    screen.blit (blueball_size, (bluex, bluey))
    pygame.display.update()
    
    



if poeng > old_highscore:     
    gamewindow ((bredde/4), (hoyde/4), (bredde/3), (hoyde/3), "Score: "+str(poeng), 30, 30, "Congratulations! New highscore!: "+str(poeng), 30, 60, "Old highscore: "+str(old_highscore), 30, 90) 
    fil = open("highscore.txt", "w")
    fil.write(str(poeng))
    fil.close()



if poeng <= old_highscore:
    gamewindow ((bredde/4), (hoyde/4), (bredde/3), (hoyde/3), "Score: "+str(poeng), 30, 30, "Highscore: "+str(old_highscore), 30, 60, "No new highscore", 30, 90)


     
pygame.quit()
quit()