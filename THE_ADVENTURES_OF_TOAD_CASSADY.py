'''
LEWIS ADKINS PYGAME: THE ADVENTURES OF TOAD CASSADY!

'''
### PACKAGES ### --------------------------------------------------------------

import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join
import numpy as np
import time
from sys import exit

path='/Users/Lewis/OneDrive/Documents/PyGames/TAOTC/'

pygame.init()
WIDTH             = 1000
HEIGHT            = 800

screen            = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('For Hope')
clock             = pygame.time.Clock()

#Music#

bg_music          = pygame.mixer.Sound(path+'Sounds/Background_Music.mp3')
bg_music.play(loops = -1)

###Inserting Background###--------------------------------------

Background_1      = pygame.image.load(path+'Background_Image/Background_Image_3.png').convert_alpha()
Background_2      = pygame.image.load(path+'Background_Image/Background_Image_4.png').convert_alpha()

Skyline_Size      = (1000,500)
Skyline_Location  = (0,250)
Skyline = pygame.image.load(path+'Skylines/Skyline_1.png').convert_alpha()
Skyline = pygame.transform.scale(Skyline, Skyline_Size)

###Level Starts###--------------------------------------------

level_1_start     = False

###Inserting Ground###------------------------------------------

Ground_Size       = (1000,100)
Ground_Location   = (500,750)
Ground            = pygame.Surface(Ground_Size)
Ground_Rect       = Ground.get_rect(midtop = Ground_Location)
Ground.fill('Brown')

###Start Text###------------------------------------------------

test_font         = pygame.font.Font(path+'Font/Pixeltype.ttf', 70)
text_surface      = test_font.render('Press Space to Start',False,'Green')

###Characters###------------------------------------------------

Character_Size    = (100,100)

Hope_Location     = (550,650)

class Hope(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path+'Characters/Hope_Model.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, Character_Size)
        self.rect  = self.image.get_rect(midbottom = Hope_Location)

hope_gravity       = 0
hope               = Hope()


Lewis_Location     = (300,650)
Lewis              = pygame.image.load(path+'Characters/Lewis_Character.png').convert_alpha()
Lewis              = pygame.transform.scale(Lewis, Character_Size)

###Sprites###----------------------------------------------------

Radio_Size         = (60,50)
Radio_Location     = (200,700)

Radio              = pygame.image.load(path+'/Sprites/Radio_Sprite.png').convert_alpha()
Radio              = pygame.transform.scale(Radio, Radio_Size)

###Campire Fire### ----------------------------------------------

fire_size          = (50,50)

Fire_Sprites       = [path+'Sprites/Fire_Sprite_1.png',path+'Sprites/Fire_Sprite_2.png',path+'Sprites/Fire_Sprite_3.png',path+'/Sprites/Fire_Sprite_4.png']

fire_images        = [pygame.image.load(Fire_Sprites[0]).convert_alpha(),
    pygame.image.load(Fire_Sprites[1]).convert_alpha(),
    pygame.image.load(Fire_Sprites[2]).convert_alpha(),
    pygame.image.load(Fire_Sprites[3]).convert_alpha(),
]

current_fire_image = 0
fire_animation_delay = 100

fire_images[0]       = pygame.transform.scale(fire_images[0], fire_size)
fire_images[1]       = pygame.transform.scale(fire_images[1], fire_size) 
fire_images[2]       = pygame.transform.scale(fire_images[2], fire_size) 
fire_images[3]       = pygame.transform.scale(fire_images[3], fire_size) 

Campfire_Log_Sprite=pygame.image.load(path+'Sprites/Campfire_Log.png').convert_alpha() 
Campfire_Log_Sprite  = pygame.transform.scale(Campfire_Log_Sprite,(210,50))

###Red Arrow### ---------------------------------------------

red_arrow            = pygame.image.load(path+'Sprites/Red_Arrow_Sprite.png').convert_alpha()
red_arrow_delay      = 10
red_arrow_location   = (500,500)
red_arrow_size       = (150,150)
red_arrow            = pygame.transform.scale(red_arrow, red_arrow_size)

###Game Menu ###--------------------------------------------------

game_menu            = True

animation_start      = False
animation_end        = False
game_start           = False
character_active     = False

while game_menu:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not animation_start:
                animation_start = True
                
    if animation_start:
        break
      
#Art-Work#       
     
    screen.blit(Background_1,(0,0))
    screen.blit(Ground, Ground_Rect)
    screen.blit(text_surface,(320,120))
    screen.blit(Skyline,Skyline_Location)

#Characters#

    screen.blit(hope.image,Hope_Location)
    
    screen.blit(Lewis,Lewis_Location)
        
#Sprites#

    screen.blit(Radio, Radio_Location)

#Fire#

    screen.blit(fire_images[current_fire_image],(450,690))
    screen.blit(Campfire_Log_Sprite,(380,725))
    
    if pygame.time.get_ticks()% fire_animation_delay==0:
        current_fire_image =(current_fire_image+1)%len(fire_images)
            
    pygame.display.flip()

#Music#

    bg_music.set_volume(.1)
    
#Clock#

    pygame.display.update()
    clock.tick(60)

###Animation###-----------------------------------------------------------------

#Character#

Kermit_Size               =(300,300)
Kermit_x_position         = 0
Kermit_y_position         = Ground_Location[1]
Kermit_Location           = (Kermit_x_position,Kermit_y_position)

lewis_scream              = pygame.mixer.Sound(path+'Sounds/Lewis_Screaming_1.mp3')
lewis_scream.set_volume(.2)

#CutScene#

cutscene_surface          = pygame.Surface((WIDTH,HEIGHT))
Cutscene_timer            = 0
cutscene_duration         = 6000
cutscene_active           = False

exit_active               = False
BLACK                     = (0, 0, 0)


class Kermit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image        = pygame.image.load(path+'Characters/Kermit.png').convert_alpha()
        self.image        = pygame.transform.scale(self.image, Kermit_Size)
        self.image        = pygame.transform.flip(self.image, True,False)
        self.rect         = self.image.get_rect(midbottom = Kermit_Location)
        self.growl_sound  = pygame.mixer.Sound(path+'Sounds/Kermit_Growl.mp3')
        self.growl_sound.set_volume(.2)

kermit = Kermit()

#Main Game Loop#

while animation_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(Background_1, (0,0))
    screen.blit(Ground, Ground_Rect) 
    screen.blit(Skyline,Skyline_Location)
    screen.blit(Radio, Radio_Location)
    screen.blit(kermit.image, kermit.rect)
    screen.blit(Lewis,Lewis_Location)
    screen.blit(hope.image,Hope_Location)
    
    screen.blit(fire_images[current_fire_image],(450,690))
    screen.blit(Campfire_Log_Sprite,(380,725))
    
    if pygame.time.get_ticks()% fire_animation_delay==0:
        current_fire_image =(current_fire_image+1)%len(fire_images)
    
    if Kermit_x_position < Lewis_Location[0]:
        Kermit_x_position +=3
        kermit.rect.midbottom = (Kermit_x_position,Kermit_y_position)
        kermit.growl_sound.play()
                
    if Kermit_x_position == Lewis_Location[0]:
        cutscene_active = True
                
        if cutscene_active:            
            cutscene_surface.fill(BLACK)
                        
            font = pygame.font.Font(path+'Font/Pixeltype.ttf', 36)
            text = font.render("OH NO! THAT BASTARD KERMIT IS STEALING MY HANDSOM BOYFRIEND LEWIS FROGSKIN!", False,'pink')
            text_rect = text.get_rect(center=cutscene_surface.get_rect().center)
            cutscene_surface.blit(text, text_rect)
                                    
            screen.blit(cutscene_surface, (0, 0))
            pygame.display.flip()
            
        if pygame.time.get_ticks() - Cutscene_timer > cutscene_duration:            
            Kermit_x_position = Kermit_x_position + 5            
            cutscene_surface.set_alpha(0)
                        
    if Kermit_x_position > Lewis_Location[0]:
        Kermit_x_position+=3
        kermit.rect.midbottom = (Kermit_x_position,Kermit_y_position)
        Lewis.set_alpha(0)
        lewis_scream.play()
                        
    if Kermit_x_position > WIDTH + 200:
        Kermit_x_position += -3
        game_start = True
                        
        break

    #Clock#     
    
    pygame.display.update()
    clock.tick(60)
    
###Game Active###-----------------------------------------------------------------

#Character#

Character_Size=(100,100)

Hope_Location = (550,Ground_Location[1])
hope_gravity = 0
hope_x_direction = 0
hope_y_direction = 0
hope_speed = 3

flipped = False

class Hope(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image         = pygame.image.load(path+'Characters/Hope_Model.png').convert_alpha()
        self.image         = pygame.transform.scale(self.image, Character_Size)
        self.image         = pygame.transform.flip(hope.image, True,False)
        self.rect          = self.image.get_rect(midbottom = Hope_Location)
        self.jump_sound    = pygame.mixer.Sound(path+'Sounds/Jump_sound.mp3')
        self.jump_sound.set_volume(.2)
        
hope = Hope()
        
#Main Game Loop#

while game_start:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hope.rect.bottom >= Ground_Location[1]:
                hope_gravity = -20
                hope.jump_sound.play()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and hope.rect.bottom >= Ground_Location[1]:
                hope_gravity = -20
                hope.jump_sound.play()
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w') and hope.rect.bottom >= Ground_Location[1]:
                hope_gravity = -20
                hope.jump_sound.play()
            
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                hope_x_direction = -1
                if not flipped:
                    hope.image = pygame.transform.flip(hope.image,True,False)
                    flipped = True
                      
            
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                hope_x_direction = 1
                if flipped:
                    hope.image = pygame.transform.flip(hope.image, True, False)
                    flipped = False
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                hope_x_direction = 0
                                   
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                hope_x_direction = 0 
             
    # Player
    hope_gravity += 1
    hope.rect.y += hope_gravity    
    hope.rect.x += hope_x_direction * hope_speed

    if hope.rect.bottom >= Ground_Location[1]:
        hope.rect.bottom = Ground_Location[1]
        hope_gravity = 0
        
    # Drawing
    screen.blit(Background_1, (0,0))
    screen.blit(Ground, Ground_Rect) 
    screen.blit(Skyline,Skyline_Location)
    screen.blit(Radio, Radio_Location)
    screen.blit(red_arrow,red_arrow_location)
    screen.blit(hope.image, hope.rect)
    
    screen.blit(fire_images[current_fire_image],(450,690))
    screen.blit(Campfire_Log_Sprite,(380,725))
    
    if pygame.time.get_ticks()% fire_animation_delay==0:
        current_fire_image =(current_fire_image+1)%len(fire_images)
                
#Music#    
    bg_music.set_volume(.2)
    
#Transition#

    if hope.rect.right > WIDTH+100:
        level_1_start = True
        game_menu = False
        
        break
            
 #Clock#       
    pygame.display.update()
    clock.tick(60)



#--------------------------------------### MAIN GAME LEVEL ### ---------------------------------------------------------#



### INITIALIZATION ### --------------------------------------------------------

pygame.init()
WIDTH = 1000
HEIGHT = 800
BLACK = (0, 0, 0)
FPS = 60
PLAYER_VEL = 6.2
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('THE ADVENTURES OF TOAD CASSADY')
clock = pygame.time.Clock()

### SOUNDS ### ----------------------------------------------------------------

def get_sounds(dir1, vol, loop):
    sound = pygame.mixer.Sound(path + 'Sounds/' + dir1)
    sound.set_volume(vol)
    
    return sound.play(loop)



### LOADING SPRITES ### -------------------------------------------------------

    # BACKGROUND SPRITE # -----------------------------------------------------

def get_background(name):
    image               = pygame.image.load(join(path,"Background_Image",name)).convert_alpha() # RETRIEVES IMAGE
    _, _, width, height = image.get_rect()                                                      # DEFINES DIMENSIONS
    return image, width, height
    
    # SPRITES # ---------------------------------------------------------------

def get_sprite(dir1, dir2, x_start, y_start, x_length, y_length, width, height):
    path_sprite         = join(path, dir1, dir2)                                     # PATH FOR SPRITES
    image               = pygame.image.load(path_sprite).convert_alpha()             # LOAD SPRITE
    surface             = pygame.Surface((x_length, y_length), pygame.SRCALPHA, 32)  # DEFINE SURFACE SIZE
    rect                = pygame.Rect(x_start, y_start, x_length, y_length)          # DEFINE RECTANGLE SIZE
    surface.blit(image,(0,0), rect)                                                  # DISPLAY IMAGE
    return pygame.transform.scale(surface,(width, height))                           # SPRITE SIZE
    
### DEFINING PLAYER ### -------------------------------------------------------
       
class Player(pygame.sprite.Sprite):
    GRAVITY             = 1.35                                                                             # DEFINES DOWNWARD ACCELERATION
    SPRITE              = get_sprite("Characters", "Hope_Model.png", 260, 100, 600, 880, 75, 110)          # SPRITES PLAYER FUNCTION
    SPRITE_DAMAGED      = get_sprite("Characters", "hope_damaged.png", 260, 100, 600, 880, 75, 110)        # DAMAGED PLAYER SPRITE
    SPRITE_HEALTHY      = get_sprite("Characters", "Hope_Model.png", 260, 100, 600, 880, 75, 110) 
    
    def __init__(self, x, y, width, height):
        super().__init__()
        
    # PLATER CHARACTERISTICS # ------------------------------------------------   
    
        self.rect       = pygame.Rect(x, y, width, height)
        self.x_vel      = 0                                                   # INITIAL X VELOCITY
        self.y_vel      = 0                                                   # INITIAL Y VELOCITY
        self.mask       = None                                                # NO MASK 
        self.direction  = "left"                                              # FACES LEFT WHEN PLAYER SPAWNS
        self.fall_count = 0                                                   # INITAL TIMING OF FALLING
        self.flipped    = False                                               # DIRECTION BOOLEAN
        self.jump_count = 0                                                   # INITIAL JUMP COUNT
        
        
        self.invincible = False                                               # INVINCIBLE FRAMES
        self.health = 5                                                       # PLAYER HEALTH
        self.damage     = 1                                                   # HOW MUCH DAMAGE THE PLAYER TAKES
        self.animation_switch = 1
        self.hit        = False
        self.hit_count  = 0
        self.dampener   = 0
        # HEALTH BAR #
        
        self.max_health = 5
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        
        
                
    # JUMP FUNCTION # ---------------------------------------------------------  
        
    def jump(self):
        self.y_vel       = -self.GRAVITY *10                                  # JUMP POWER
        self.jump_count +=1                                                   # ADDS TO JUMP COUNTER
    
    # LATERAL MOVE FUNCTIONS # -------------------------------------------------    
    
    def move(self, dx, dy):
        self.rect.x     +=dx                                                  # MOVE LEFT
        self.rect.y     +=dy                                                  # MOVE RIGHT
        
    def move_left(self, vel):
        self.x_vel         = -vel                                             # MOVE LEFT WITH X VELOCITY
        if self.direction != "left": 
            self.direction = "left"                                           # FACING LEFT
            self.flipped   = False                                            # DIRECTION BOOLEAN

    def move_right(self, vel):
        self.x_vel      = vel                                                 # MOVE RIGHT WITH X VELOCITY
        if self.direction != "right":
            self.direction = "right"                                          # FACING RIGHT 
            self.flipped   = True                                             # DIRECTION BOOLEAN

    def make_hit(self):
        self.hit           = True
        self.hit_count     = 0
        get_sounds('damage_sound.mp3', .1, 0)                                     

    # CHECK FUNCTIONS # -------------------------------------------------------
    
    def loop(self,fps):
        self.y_vel      += min(1, (self.fall_count / fps)*self.GRAVITY)       # FALLING PHYSICS
        self.move(self.x_vel, self.y_vel)                                     # LATERAL PHYSICS     
        self.fall_count += 1  

        if self.hit:            
            self.dampener -=.6
            self.hit_count += 1
            self.damage_animation()
            self.health -= self.damage
            self.invincible = True
            
        if self.invincible:
            self.damage  = 0                 
        
        if self.hit_count > fps * .48:
            
            self.hit = False
            self.SPRITE  = self.SPRITE_HEALTHY
            self.dampene = 0
            
            self.invincible = False
            self.damage  = 1
                                                                                                                                                                        
        self.update()                                                         # UPDATES PLAYER
    
    # VERTICLE COLLISION FUNCTIONS # ------------------------------------------    
    
    def landed(self):
        self.fall_count  = 0                                                   # FALL COUNT RESETS AFTER LANDING
        self.y_vel       = 0                                                   # Y VELOCITY RESETS AFTER LANDING
        self.jump_count  = 0                                                   # JUMP COUND RESETS AFTER LANDING
        
    def hit_head(self):
        self.count       = 0 
        self.y_vel      *= -1                                                  # INITIAL PUSH DOWN FROM COLLISION
    
    # CHARACTER FLIP FUNCTION # -----------------------------------------------
    
    def draw(self,win, offset_x, offset_y):                                   
        if self.flipped:                                                      # FLIPS PLAYER TO RIGHT IF MOVING RIGHT
            sprite       = pygame.transform.flip(self.SPRITE, True, False)
        else:                                                                 # FLIPS PLAYER TO LEFT IF MOVING LEFT
            sprite       = self.SPRITE
        screen.blit(sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
        
    # DAMAGE ANIMATION # ------------------------------------------------------
    
    def damage_animation(self):
        a = self.SPRITE_HEALTHY                                               # NORMAL SPRITE
        b = self.SPRITE_DAMAGED                                               # DAMAGED SPRITE
        
        amplitude       = 1                                                   # DETERMINES HOW FAST SPRITES SWITCH
        period          = 240 + self.dampener
        frequency       = 2 * math.pi/period
        
        self.animation_switch     = amplitude * math.sin(frequency * (pygame.time.get_ticks()))
        
        if self.animation_switch > 0 :
            self.SPRITE  = a
            
        if self.animation_switch < 0 :
            self.SPRITE  = b
            
    def basic_health(self):                                                            # DRAW HEALTH BAR                
        pygame.draw.rect(screen, (255,0,0), (50,50,self.health / self.health_ratio,25)) 
        pygame.draw.rect(screen, (255,255,255), (50,50,self.health_bar_length,25),4)                        
    # UPDATE FUNCTION # ------------------------------------------------------    
    
    def update(self):                                                         
        self.sprite     = self.SPRITE
        self.rect       = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask       = pygame.mask.from_surface(self.sprite)
        self.basic_health()
        
### DEFINING OBJECTS ### ------------------------------------------------------
        
class Object(pygame.sprite.Sprite):                                           # BASIC INFORMATION FOR EACH OBJECT
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        self.rect       = pygame.Rect(x, y, width, height)
        self.image      = pygame.Surface((width, height),pygame.SRCALPHA)
        self.width      = width
        self.height     = height
        self.name       = name
        
    # DRAWING OBJECT # --------------------------------------------------------
    
    def draw(self, win, offset_x, offset_y): 
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))

    ### BLOCKS ### ------------------------------------------------------------
        
class Block(Object):                                                          # RETRIEVES BLOCK INFORMATION
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block           = get_sprite("Sprites", "ground_1.png", 15, 140, 32, 32, 80, 80)                                   # SPRITE BLOCK FUNCTION
        self.image.blit(block, (0,0))                                         # DISPLAYS BLOCK
        self.mask       = pygame.mask.from_surface(self.image)                # SETS BLOCK MASK
        
class Tunnel(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        tunnel          = get_sprite("Sprites", "tunnel.png", 15, 140, 32, 32, 80, 80)
        self.image.blit(tunnel,(0,0))
        self.mask       = pygame.mask.from_surface(self.image)
            
    ### LEMONS ###-------------------------------------------------------------
            
class Lemon(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        
        lemon          = get_sprite("Sprites", "Lemon.png", 200, 150, 1000, 1000, 50, 50)                                      # SPRITES LEMON FUNCTION
        self.image.blit(lemon,(0,0)) 
        self.mask      = pygame.mask.from_surface(self.image)        
        self.time      = 0                                                    # TIMER SET TO ZERO
        self.collide_time = 0                                                 # COLLIDE TIMER 
        self.collision_cooldown = 0                                           # COLLISION COOL DOWN TIMER
        self.Opaqueness = 255                                                 # IMAGE OPAQUENESS
        self.orig_mask  = pygame.mask.from_surface(self.image)                # ALTERNATIVE MASK
    
        # LEMON FLOAT ANIMATION # ---------------------------------------------    
    
    def floating(self):                                                       
        amplitude      = 1                                                    # FLOATING PHYSICS
        period         = 25 
        frequency      = 2 * math.pi/period
        
        self.y_vel     = amplitude * math.sin(frequency * self.time)
        self.time     += 1
    
        # UPDATES LEMON IMAGE # -----------------------------------------------
                        
    def update(self):                                                         # UPDATE FLOATING PHYSICS                                        
        self.floating()
        self.rect.y   += self.y_vel
        
        # FUNCTION WHEN PLAYER FIRST COLLIDES WITH LEMON # --------------------
        
    def interaction(self):                                                    # LEMON INTERACTION
        self.Opaqueness = 158                                                 # HALVES OPAQUENESS             
        self.image.set_alpha(self.Opaqueness)                                 
        self.mask       = self.orig_mask                                      # REPLACE MASK 
        
        # FUNCTION WHEN ANIMATION AND COLLISION ARE OVER # --------------------
                    
    def reset_transparency(self): 
        self.Opaqueness = 255                                                 # RESET OPAQUENESS     
        self.image.set_alpha(self.Opaqueness)
        self.mask       = pygame.mask.from_surface(self.image)                # RESETS MASK
    
        # FUNCTION COLLISION AND ANIMATION # ----------------------------------
                    
    def lemon_collision(self, player): 
        current_time         = pygame.time.get_ticks()                        # TIME SINCE GAME INTIALIZED
        time_since_collision = current_time - self.collide_time               # TIME ELAPED FROM FIRST COLLSION AND GAME INTIALIZTION
        
        if self.collision_cooldown == 0:                                      # PLAYER FIRST COLLIDES WITH LEMON
            if pygame.sprite.collide_mask(player, self):
                self.interaction()                                            # SEMI TRANSPARENT & MASK SWITCHING
                get_sounds('crunch.mp3', .2, 0)
                self.collide_time       = current_time                        # TRACKS HOW LONG SINCE COLLISION
                self.collision_cooldown = 180  
        else:
            if time_since_collision > 1500:                                   # COUNTS FOR THREE SECONDS
                self.reset_transparency()                                     # ANIMATION RESETS
                self.collision_cooldown = 0
                
    ### SPIKES ### ------------------------------------------------------------
                
class Spikes(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        spike          = get_sprite("Sprites", "SpikesAnim.png", 0, 0, 32, 32, 32, 32)  # LOAD IMAGE
        self.image.blit(spike,(0,0))                                                    # BLIT IMAGE
        self.mask      = pygame.mask.from_surface(self.image)                           # GENERATE MASK
   
    ### HEALTH ### ------------------------------------------------------------
    
class Health(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        health_bar       = get_sprite("Sprites", "health_head.png", 0, 0, 800, 800, 100, 100) # LOAD IMAGE
        self.image.blit(health_bar, (0,0))                                                    # BLIT IMAGE
        self.mask        = pygame.mask.from_surface(self.image)                               # GENERATE MASK
        self.amount      = 1                                                                  # HEALTH AMOUNT
        
class Head_2(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        health_bar       = get_sprite("Sprites", "health_head.png", 0, 0, 800, 800, 400, 400) # LOAD HEALTH BAR
        self.image.blit(health_bar, (0,0))                                                    # IMAGE MASK
        self.mask        = pygame.mask.from_surface(self.image)                               # GENERATE MASK
        
        
class Heart(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        health_bar       = get_sprite("Sprites", "heart.png", 0, 0, 1000, 1000, 400, 400) # LOAD HEART
        self.image.blit(health_bar, (0,0))                                                # IMAGE MASK
        self.mask        = pygame.mask.from_surface(self.image)                           # GENERATE MASK
        
        
class Head(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        frog_head     = get_sprite("Sprites", "frog_head.png", 50, 50, 800, 800, 400, 400)
        self.image.blit(frog_head, (0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        

class Bee(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        bee              = get_sprite("Sprites", "bee_sprite.png", 0, 0, 1000, 1000, 75, 75)
        self.time        = 0
        self.image.blit(bee,(0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        
        
    def bee_animation(self):
        
        amplitude        = 1
        period           = 20
        frequency        = 2 * math.pi/period
        
        self.y_vel       = amplitude * math.sin(frequency * self.time)
        
        self.time        += 1
        
    def update(self):
        self.bee_animation()
        self.rect.y      += self.y_vel
        
        
class Mosquito(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        mosquito         = get_sprite("Sprites", "mosquito_sprite.png", 0, 0, 1000, 1000, 75, 75) 
        self.sprite      = get_sprite("Sprites", "mosquito_sprite.png", 0, 0, 1000, 1000, 75, 75)        
        self.time        = 0
        self.image.blit(mosquito,(0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        self.flip        = False
        
    def mosquito_animation(self):
        
        amplitude_x      = 4
        period_x         = 250
        frequency_x      = 2 * math.pi / period_x
                
        self.x_vel       = amplitude_x * math.sin(frequency_x * self.time)
         
        amplitude_y      = 10
        period_y         = period_x / 2
        frequency_y      = 2 * math.pi / period_y
        
        self.y_vel       = amplitude_y * math.sin(frequency_y * self.time )
        
        self.time        += 1
        
        if self.x_vel    > 0:
            self.flip    = True
            
        if self.x_vel    < 0:
            self.flip    = False
            
        if self.flip:
            self.image   = pygame.transform.flip(self.sprite, True, False)
        
        else:
            self.image   = self.sprite
        
    def update(self):
        self.mosquito_animation()        
        self.rect.x      += self.x_vel
        self.rect.y      += self.y_vel
                
    ### GRASSHOPPER ### -------------------------------------------------------
    
class Grasshopper(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        grasshopper      = get_sprite("Sprites", "grasshopper.png", 0, 0, 1000, 1000, 110, 110)
        self.sprite      = get_sprite("Sprites", "grasshopper.png", 0, 0, 1000, 1000, 110, 110)
        self.image.blit(grasshopper,(0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        self.time        = 0
        self.flip        = False
        
    def grasshopper_animation(self):
        
        amplitude_x      = 4
        period_x         = 250
        frequency_x      = 2 * math.pi / period_x
                
        self.x_vel       = amplitude_x * math.sin(frequency_x * self.time)
         
        amplitude_y      = 7
        period_y         = period_x / 2
        frequency_y      = 2 * math.pi / period_y
        
        self.y_vel       =  - amplitude_y * math.sin(frequency_y * self.time )
        
        self.time        += 1
        
        if self.x_vel    > 0:
            self.flip    = False
            
        if self.x_vel    < 0:
            self.flip    = True
            
        if self.flip:
            self.image   = pygame.transform.flip(self.sprite, True, False)
        
        else:
            self.image   = self.sprite
        
    def update(self):
        self.grasshopper_animation()      
        self.rect.x      += self.x_vel
        self.rect.y      += self.y_vel
 
    ### LADYBUG ### -----------------------------------------------------------     
 
class Ladybug(Object):
    VELOCITY = 5
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        grasshopper      = get_sprite("Sprites", "ladybug.png", 0, 0, 1000, 1000, 125, 125)
        self.sprite      = get_sprite("Sprites", "ladybug.png", 0, 0, 1000, 1000, 125, 125)
        self.image.blit(grasshopper,(0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        self.time        = 0
        self.flip        = True
        
    def animation(self):
        
        amplitude_x      = 2.7
        period_x         = 400
        frequency_x      = 2 * math.pi / period_x
                
        self.x_vel       = amplitude_x * math.sin(frequency_x * self.time)
                 
        self.time        += 1
        
        if self.x_vel    > 0:
            self.flip    = True
            
        if self.x_vel    < 0:
            self.flip    = False
            
        if self.flip:
            self.image   = pygame.transform.flip(self.sprite, True, False)
        
        else:
            self.image   = self.sprite
        
    def update(self):
        self.animation()      
        self.rect.x      += self.x_vel
        
class Gun(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        gun              = get_sprite("Sprites", "gun.png", 0, 0, 1000, 1000, 150, 150)
        self.time        = 0
        self.image.blit(gun,(0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        
        
    def gun_animation(self):
        
        amplitude        = 1
        period           = 25
        frequency        = 2 * math.pi/period
        
        self.y_vel       = amplitude * math.sin(frequency * self.time)
        
        self.time        += 1
                
    def update(self):
        self.gun_animation()
        self.rect.y      += self.y_vel

class Kermit(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        kermit           = get_sprite("Characters", "Kermit.png", 0, 0, 1000, 1000, 400, 400)
        self.image.blit(kermit, (0,0))
        self.mask        = pygame.mask.from_surface(self.image)
        
class Frog(Object):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        frog             = get_sprite("Characters", "frog.png", 0, 0, 1000, 1000, 120, 120)
        self.image.blit(frog, (0,0))
        self.mask        = pygame.mask.from_surface(self.image)

        
### CHARACTER PHYSICS ### -----------------------------------------------------
                
    # DOUBLE JUMP ABILITY FROM LEMON # ----------------------------------------

def double_jump(player,lemon): 
    for lem in lemon:
        if pygame.sprite.collide_mask(player,lem) and lem.Opaqueness == 255:
            player.jump_count = 0
            

def health_animation(player, health):
    health.amount = player.health
                    
    # CHARACTER DAMAGE / DEATH # ----------------------------------------------
       
def damage(player, spikes ,mosquitos, bees, grasshopper, ladybug):        
    
    grav_norm     = 1.35
    
    for spi in spikes:
            if pygame.sprite.collide_mask(player, spi): 
                player.GRAVITY = 2
                player.jump()
                player.make_hit()
                player.GRAVITY = grav_norm
                
    for mos in mosquitos:
            if pygame.sprite.collide_mask(player, mos): 
                player.GRAVITY = -.75
                player.jump()
                get_sounds('mosquito_sound.mp3', .2, 0)
                player.make_hit()
                player.GRAVITY = grav_norm

    for bee in bees:
        if pygame.sprite.collide_mask(player, bee):
            player.GRAVITY     = 2.2
            player.jump()
            get_sounds('bee_buzz.mp3', .5, 0)

            player.GRAVITY     = grav_norm 
            
    for grass in grasshopper:
        if pygame.sprite.collide_mask(player, grass):
            player.GRAVITY     = .90
            get_sounds('grasshopper.mp3', .2, 0)
            player.jump()
            player.make_hit()
            player.GRAVITY     = grav_norm
            
    for lady in ladybug:
        if pygame.sprite.collide_mask(player, lady):
            player.GRAVITY     = .90
            player.jump()
            get_sounds('ladybug.mp3', .3, 0)
            player.make_hit()
            player.GRAVITY     = grav_norm
            


    # HOW VERTICLE BLOCK AND PLAYER INTERACT # --------------------------------

def handle_vertical_collision(player, objects, dy): 
    collided_objects   = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj): 
            if dy > 0:                                                        # PLAYER COMING FROM ABOVE BLOCK
                player.rect.bottom = obj.rect.top
                player.landed()
                
            elif dy < 0:                                                      # PLAYER COMING FROM BELOW BLOCK
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)                                      # LISTING COLLIDED OBJECTS

    return collided_objects

    # HORIZONTAL COLLISION # --------------------------------------------------

def collide(player, objects, dx): 
    player.move(dx,0)                                                         # PLAYER MOVES TO RIGHT 
    player.update()
    collided_object = None
    
    for obj in objects:
        if pygame.sprite.collide_mask(player,obj):
            collided_object = obj
            break
        
    player.move(-dx,0)                                                        #PLAYER MOVES TO LEFT
    player.update()
    return collided_object

def handle_move(player, objects, lemon):                                      # PLAYER CONTROLS AND HORIZAONTAL COLLISION
    keys = pygame.key.get_pressed()
    
    player.x_vel       = 0
    collide_left       = collide(player,objects, -PLAYER_VEL*3)               # HORIZONTAL COLLISION FROM LEFT
    collide_right      = collide(player,objects,PLAYER_VEL*3)                 # HORIZONTAL COLLISION FROM RIGHT

    if keys[pygame.K_LEFT] and not collide_left:                              # PRESS a TO MOVE LEFT AND THERES NOTHING THERE
        player.move_left(PLAYER_VEL)

    if keys[pygame.K_RIGHT] and not collide_right:                            # PRESS d TO MOVE RIGHT AND THERES NOTHING THERE
        player.move_right(PLAYER_VEL)
        
    handle_vertical_collision(player, objects,player.y_vel)
    double_jump(player, lemon)  
    
### TEXT ### ------------------------------------------------------

def draw_text(surface, text, font, color, x, y):                              # RENDERING TEXT
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)
    
### ALTERNATIVE STATES ### ----------------------------------------------------

    # GAME OVER SCREEN #
    
def show_go_screen():                                     
    game_over_surface = pygame.Surface((WIDTH, HEIGHT))                                  # GAME OVER SURFACE
    game_over_surface.fill(BLACK)
    
    font = pygame.font.Font(path + 'Font/Pixeltype.ttf', 36)                             # TEXT FONT
    
    game_over_text  = "GAME OVER"                
    message_over_text = "YOUR LOVER STILL WAITS FOR YOU <3"                              # MESSAGES
    start_over_text = "PRESS 'SPACE' TO RETRY"
    
    screen.fill('pink')
    draw_text(game_over_surface, game_over_text, font, 'red', WIDTH//2, HEIGHT //3 )
    draw_text(game_over_surface, message_over_text, font, 'red', WIDTH//2, HEIGHT - 400) # MESSAGE POSITIONS/COLOR/ FONT
    draw_text(game_over_surface, start_over_text, font, 'red', WIDTH //2, HEIGHT - 340)
    
    pygame.display.flip()                                                                # UPDATE
    waiting = True
    
    while waiting:
        clock.tick(FPS)
        
        for event in pygame.event.get():                                                  
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYUP:                                               # SPACE TO CONTINUE
                if event.key == pygame.K_SPACE:  
                    waiting = False
                    
    # AMBUSH #

def ambush_screen():
    ambush_surface = pygame.Surface((WIDTH, HEIGHT))                          # CUTSCENE SURFACE
    ambush_surface.fill(BLACK)
    
    font = pygame.font.Font(path+'Font/Pixeltype.ttf', 36)                    # FONT
    
    ambush_text = "TOAD LOOK OUT! IT'S AN AMBUSH!"                            # MESSAGE
    screen.fill('blue')                                                       # SCREEN COLOR
    draw_text(ambush_surface, ambush_text, font, 'green', WIDTH // 2, HEIGHT // 2)
    
    pygame.display.flip()                                                     # UPDATE
    start_time = pygame.time.get_ticks()                                      # START TIMER
    waiting = True                                                            # CUTSCENE BOOLEAN
    
    while waiting:
        clock.tick(FPS)
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                        
        elapsed_time = pygame.time.get_ticks() - start_time                   # TIMER FOR 3 SECONDS
        if elapsed_time >= 3000: 
            waiting = False
                                 
            break

def end_screen_1():
    end_1_surface = pygame.Surface((WIDTH, HEIGHT))
    end_1_surface.fill(BLACK)
    
    get_sounds('Gunshot.mp3', .7, 0)                                          # GUNSHOT SOUND
    screen.fill('white')                                                      # INITIAL FLASH
    pygame.display.flip()
    start_time = pygame.time.get_ticks()
    flash                  = True
    black_screen           = False
    
    while flash:
        clock.tick(FPS)
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                        
        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time    >= 100:                                            # FLASH FOR 100 MILLISECONDS
            flash          = False
            black_screen   = True
                
    while black_screen:
        clock.tick(FPS)
        screen.fill('black')         
        pygame.display.flip()
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()  
                
        elapsed_time       = pygame.time.get_ticks() - start_time
        if elapsed_time    >= 5000:                                           # BLACK SCREEN FOR 5 SECONDS
            
            black_screen   = False
            
            break

def end_screen_2():
    end_2_surface = pygame.Surface((WIDTH, HEIGHT))                           # CUTSCENE SURFACE
    end_2_surface.fill(BLACK)

    victory_screen = True                                                     # CUTSCENE BOOLEAN
    get_sounds('victory.mp3', .5 , 0)                                         # CUTSCENE MUSIC
    color_1 = 'blue'                                                          # BACKGROUND COLORS
    color_2 = 'pink'
    font = pygame.font.Font(path+'Font/Pixeltype.ttf', 40)                    # FONT
    victory_text = "YOU DID IT YOU SAVED THE DAY!!!"                          # MESSAGE
    text_color = 'red'
    
    start_time = pygame.time.get_ticks()                                      # START TIMER
    
    while victory_screen:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        elapsed_time = pygame.time.get_ticks() - start_time                   # ELAPSED TIME
        
        if elapsed_time >= 8000:                                              # TIMER FOR 8 SECONDS
            screen.fill(color_2)
        elif elapsed_time % 500 >= 250:                                       # SWTICH BETWEEN COLORS EVERY 250 MILLISECONDS
            screen.fill(color_1)
        else:
            screen.fill(color_2)
        
        draw_text(end_2_surface, victory_text, font, text_color, WIDTH // 2, HEIGHT // 2)
        
        if elapsed_time >= 9000:                                              # NEXT CUTSCENE AFTER 9 SECONDS
            victory_screen = False
            break
        
        pygame.display.flip()
        
def end_screen_3():
    end_3_surface = pygame.Surface((WIDTH, HEIGHT))
    end_3_surface.fill(BLACK)

    kiss_screen = True                                                        # CUT SCENE BOOLEAN
    get_sounds('ending.mp3', .5 , 0)                                          # LOAD IN ENDING SONG
    color_3 = (255, 0, 0)                                                     # RED
    color_4 = (0, 255, 0)                                                     # GREEN
    
    start_kiss_time = pygame.time.get_ticks()                                 # START TIMER
    
    sprite_1 = Head_2(420, 350, 2000)                                         # LOAD IN SPRITES
    sprite_2 = Head(100, 400, 2000)
    sprite_3 = Heart(WIDTH / 2 - 110, 100, 2000)
    
    all_sprites = pygame.sprite.Group(sprite_1, sprite_2, sprite_3)           # SPRITE GROUP
    
    while kiss_screen:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        elapsed_kiss_time = pygame.time.get_ticks() - start_kiss_time         # ELAPSED TIME
        
            
        if elapsed_kiss_time >= 8000:                                         # TIMER FOR 8 SECONDS
            screen.fill(color_4)
        elif elapsed_kiss_time % 500 >= 250:                                  # TIMER FOR 250 MILLIESCONDS
            screen.fill(color_3)
        else:
            screen.fill(color_4)
       
        all_sprites.draw(screen) 
        
        if elapsed_kiss_time >= 9000:                                         # TIMER FOR 9 SECONDS
            kiss_screen = False                                               # CUTSCENE BOOLEAN
            break
        
        pygame.display.flip()                                                 # UPDATE
        
def end_screen_4():
    end_4_surface = pygame.Surface((WIDTH, HEIGHT))                           # CUTSCENE SURFACE
    end_4_surface.fill(BLACK)
    
    font = pygame.font.Font(path+'Font/Pixeltype.ttf', 36)                    # FONT
    
    end_4_text = "AND THEY LIVED HAPPILY EVER AFTER!"                         # MESSAGE
    screen.fill('pink')                                                       # SCREEN COLOR
    draw_text(end_4_surface, end_4_text, font, 'red', WIDTH // 2, HEIGHT// 2) # TEXT
    start_4_time = pygame.time.get_ticks() 
    pygame.display.flip()                                                     # UPDATE
    
    waiting = True                                                            # CUTSCENE BOOLEAN
    
    while waiting:                                                            # WAITS UNTIL QUIT GAME
        clock.tick(FPS)
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                
        elapsed_time = pygame.time.get_ticks() - start_4_time                 # TIMER FOR 5 SECONDS
        if elapsed_time >= 5000: 
            waiting = False

            break        
def end_screen_5():
    end_5_surface = pygame.Surface((WIDTH, HEIGHT))                           # CUTSCENE SURFACE
    end_5_surface.fill(BLACK)
    
    font = pygame.font.Font(path+'Font/Pixeltype.ttf', 36)                    # FONT
    
    end_5_text = "THANKS FOR PLAYING!!!"                                      # MESSAGE
    screen.fill('green')                                                      # SCREEN COLOR
    draw_text(end_5_surface, end_5_text, font, 'blue', WIDTH// 2, HEIGHT// 2) # TEXT
  
    pygame.display.flip()                                                     # UPDATE
    
    waiting = True                                                            # CUTSCENE BOOLEAN
    
    while waiting:                                                            # WAITS UNTIL QUIT GAME
        clock.tick(FPS)
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
### DRAWING ENVIROMENT ### ----------------------------------------------------
    
def draw(screen, background, tunnel, objects, lemons, spikes, bees, mosquitos, grasshopper, health_bar, player, ladybug, guns, kermit, frogs, offset_x, offset_y):
    
    screen.blit(background[0],(0,0))                                          # DRAW BACKGROUND

    for tun in tunnel:                                                        # DRAW TUNNEL
        tun.draw(screen, offset_x, offset_y)
                
    for obj in objects:                                                       # DRAWS ALL OBJECTS
        obj.draw(screen, offset_x, offset_y)
                
    for lem in lemons:                                                        # DRAWS ALL LEMONS
        lem.draw(screen, offset_x, offset_y)
        
    for spi in spikes:                                                        # DRAWS ALL SPIKES
        spi.draw(screen, offset_x, offset_y)
        
    for bee in bees:                                                          # DRAW BEES
        bee.draw(screen, offset_x, offset_y)
        
    for mos in mosquitos:                                                     # DRAW MOSQUITOS
        mos.draw(screen, offset_x, offset_y)
        
    for grass in grasshopper:                                                 # DRAW GRASSHOPPERS
        grass.draw(screen, offset_x, offset_y)
        
    for lady in ladybug:                                                      # DRAW LADYBUGS
        lady.draw(screen, offset_x, offset_y)
        
    for gun in guns:                                                          # DRAW GUNS
        gun.draw(screen, offset_x, offset_y)
        
    for kerm in kermit:                                                       # DRAW KERMIT
        kerm.draw(screen, offset_x, offset_y)
        
    for frog in frogs:                                                        # DRAW FORGS
        frog.draw(screen, offset_x, offset_y)
            
    player.basic_health()                                                     # DRAW PLAYER HEALTH
    
    for health in health_bar:                                                 # DRAW HEALTH BAR
        health.draw(screen, 0, 0)
           
    player.draw(screen, offset_x, offset_y)                                   # DRAW PLAYER
                
    pygame.display.update()                                                   # UPDATE IMAGES
    
def draw_box(x_arr, y_arr, length_arr, orientation):
    block_size = 80                                                           # BLOCK SIZE
    boxes = []                                                                # BLOCK LIST
    if orientation == 'horizontal':
        for x, y, length in zip(x_arr, y_arr, length_arr):
            boxes.extend([Block(block_size * i + block_size * x, HEIGHT - y * block_size, block_size) for i in range(length)])  # DRAWS HORIZONTAL LINE OF BOXES
    elif orientation == 'vertical':
        for x, y, length in zip(x_arr, y_arr, length_arr):
            boxes.extend([Block(block_size * x, HEIGHT - i * block_size - block_size * y, block_size) for i in range(length)])  # DRAWS VERTICLE LINE OF BOXES
    return boxes

def draw_ground_spikes(x_arr, y_arr, length_arr):
    block_size = 80
    spike_size = 32
    SBRatio = spike_size / block_size                                         # SPIKE SPACING
    
    spikes = []                                                               #SPIKE LIST
    for x, y, length in zip(x_arr, y_arr, length_arr):
        spikes.extend([Spikes((i * block_size * SBRatio) + x * block_size, HEIGHT - y * block_size - spike_size, 32) for i in range(length)]) # DRAWS HORIZONTAL SPIKES
    
    return spikes

def draw_graphic(Class, x_arr, y_arr):
    block_size = 80
    graphics = []                                                             # SPRITE LIST
    for x, y in zip(x_arr, y_arr):
        graphics.append(Class(x * block_size, HEIGHT - y * block_size, 1000)) # DRAWS SPRITE AT LOCATION
    return graphics

def draw_health_bar(x, y):
    space_size = 60
    
    return [Health( x * space_size, HEIGHT - y * space_size , 100) ]

def draw_tunnel(start_x, start_y, length_x, length_y):
    block_size = 80
    boxes = []

    for x in range(start_x, start_x + length_x):
        for y in range(start_y, start_y + length_y):
            box = Tunnel(block_size * x, HEIGHT - block_size * y - block_size, block_size * 2)  # DRAWS AREA OF BOXES
            boxes.append(box)

    return boxes
            
    
### GAME SETUP ### ------------------------------------------------------------

def main(screen):
    clock = pygame.time.Clock()
    background = get_background("Background_Image_4.png")
    
    tunnel = [*draw_tunnel(84, 0, 3, 12), *draw_tunnel(85,0,13,10), *draw_tunnel(98, 0 ,16, 26), *draw_tunnel(114, 20, 10, 6)]
    
### LEVEL 1 ###----------------------------------------------------------------
    
    block_size        = 80
    
    # DRAW PLAYER # -----------------------------------------------------------
    
    player            = Player( 2 * block_size , HEIGHT - 2 * block_size, 50, 50) # DRAW PLAYER
    
    # HEALTH BAR # ------------------------------------------------------------

    health_bar        = draw_health_bar(0, 13)                                # DRAW HEALTH BAR

    # BEES # ------------------------------------------------------------------
    
    bees_x            = [44.5, 68.5, 71.5, 103, 106, 109, 180]                # BEE X LOCATION LIST
    bees_y            = [2, 4, 4, 6, 5, 5.5, 24]                              # BEE Y LOCATION LIST
    
    bees              = draw_graphic(Bee, bees_x, bees_y)                     # DRAW BEES
    
    # MOSQUITOS # -------------------------------------------------------------
   
    mosquito_x        = [9, 75, 106.4, 147]                                   # MOSQUITO X LOCATION LIST
    mosquito_y        = [11, 14, 14.4, 21]                                    # MOSQUITO Y LOCATION LIST
        
    mosquitos         = draw_graphic(Mosquito, mosquito_x, mosquito_y)        # DRAW MOSQUITOS
    
    # LEMONS # ----------------------------------------------------------------
    
    lemon_x           = [53, 76.5, 79.7, 101, 117, 168.5]                     # LEMON X LOCATION LIST
    lemon_y           = [4, 7.3, 11.3, 5.3, 23, 22]                           # LEMON Y LOCATION LIST
        
    lemon             = draw_graphic(Lemon, lemon_x, lemon_y)                 # DRAW LEMON
    
    # GRASSHOPPERS # ----------------------------------------------------------
    
    grasshopper_x     = [35.5, 90, 125]                                       # GRASSHOPPER X LOCATION LIST
    grasshopper_y     = [2.3, 2.3, 21.3]                                      # GRASSHOPPER Y LOCATION LIST
        
    grasshopper       = draw_graphic(Grasshopper, grasshopper_x, grasshopper_y) # DRAW GRASSHOPPER
    
    # LADYBUGS # --------------------------------------------------------------
   
    ladybug_x         = [22, 48, 59, 100, 137]                                # LADYBUG X LOCATION LIST 
    ladybug_y         = [2.3, 2.3, 4.3, 1.3, 19.3]                            # LADYBUG Y LOCATION LIST
    
    ladybug           = draw_graphic(Ladybug, ladybug_x, ladybug_y)           # DRAW LADYBUG
    
    # SPIKES # ----------------------------------------------------------------
   
    spikes_x          = [16, 29, 77.2, 80, 88, 92, 96, 104.6, 107.6, 109, 113, 117, 145, 150, 166] # SPIKE X LOCATION LIST
    spikes_y          = [1, 0, 4, 7, 0, 0, 0, 7, 6, 21, 21, 21, 17, 17, 19]                        # SPIKE Y LOCATION LIST
    spikes_length     = [10, 10, 2, 5, 5, 5, 5, 2, 2, 5, 5, 10, 5, 5, 2]                           # SPIKE LENGTH LIST
    
    spikes            = draw_ground_spikes(spikes_x, spikes_y, spikes_length)                      # DRAW SPIKES
    
   
    # GUN # -------------------------------------------------------------------
   
    gun_x             = [223, 237]                                            # GUN X LOCATION LIST
    gun_y             = [24, 24]                                              # GUN Y LOCATION LIST
    
    guns              = draw_graphic(Gun, gun_x, gun_y)                       # DRAW GUN
    
    # KERMIT # ----------------------------------------------------------------
    
    kermit_x          = [241]                                                 # KERMIT X LOCATION
    kermit_y          = [28]                                                  # KERMIT Y LOCATION
    
    kermit            = draw_graphic(Kermit, kermit_x, kermit_y)              # DRAW KERMIT
    
    # FROG # ------------------------------------------------------------------
    
    frog_x            = [241]                                                 # FROG X LOCATION
    frog_y            = [24.5]                                                # FROG Y LOCATION
    
    frogs              = draw_graphic(Frog, frog_x, frog_y)                   # DRAW FROG
    
    # TERRAIN # ---------------------------------------------------------------

        # FLOOR # -------------------------------------------------------------

    box_h_x           = [1, 1 ,33, 47, 83, 90, 94, 98, 83, 135, 143, 14, 17, 20, 33, 42, 47, 107.7, 103, 105, 108, 109, 111, 113, 115, 117, 121, 125, 129, 158, 165, 170, 182, 186, 198, 202, 207, 211, 99] # H_BOX X LIST
    box_h_y           = [1, 0, 1, 1, 1, 1, 1, 1, 0, 18, 17, 2, 5, 2, 2, 2, 2, 13, 16, 19, 20, 21, 20, 21, 20, 21, 20, 20, 20, 18, 19, 23, 24, 27, 27, 26, 25, 23, 26]                                       # H_BOX Y LIST
    box_h_length      = [28, 42, 10, 10, 5, 2, 2, 2, 30, 10, 12, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 35, 25]                                                      # H_BOX LENGTH LIST
    
    box_v_x           = [113, -1, 0, 1, 7, 8, 28, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 65, 66, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 104.5, 107.5, 110.5, 113, 175, 193, 194, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 114, 123, 229] # V_BOX X LIST
    box_v_y           = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 5, 7, 10, 24, 24, 24, 7, 8, 9, 9, 9, 10, 10, 9, 9, 9, 8, 5, 0, 20, 23]                                                           # V_BOX Y LIST
    box_v_length      = [10, 5, 5, 5, 3, 3, 1, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 8, 8, 7, 7, 12, 12, 16, 2, 2, 2, 2, 2, 2, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 21, 2, 6]                                                  # V_BOX LENGTH LIST
    
    horizontal_boxes  = draw_box(box_h_x, box_h_y, box_h_length, 'horizontal') # DRAW H_BOX
    vertical_boxes    = draw_box(box_v_x, box_v_y, box_v_length, 'vertical')   # DRAW V_BOX
    
    terrain           = [*vertical_boxes, *horizontal_boxes]                   # H_BOX + V_BOX
       
    # CAMERA POSITION # -------------------------------------------------------     
    
    offset_x          = 0                                                     # CAMERA X POSITION
    offset_y          = 0                                                     # CAMERA Y POSTION
    scroll_area_width = 200                                                   # DISTANCE FROM CENTER TO SCROLL ACTIVATION
    
    
    # GAME STATES BOOLEANS # --------------------------------------------------
    end_scene         = False   
    ambush            = False
    display_gun_text  = False
    game_over         = False
    level_1_start     = True
    
### MAIN GAME LOOP ### --------------------------------------------------------    
    
    while level_1_start:
        clock.tick(FPS)                                                       # 60 FPS
        
        for event in pygame.event.get():                                      # QUIT BUTTON
            if event.type == pygame.QUIT: 
                level_1_start = False
                break
            
            if event.type == pygame.KEYDOWN:                                  # JUMP BUTTON
                if event.key == pygame.K_SPACE and player.jump_count < 1:
                    get_sounds('Jump_sound.mp3', .1, 0)
                    player.jump()
                    
        # UPDATING PLAYER # ---------------------------------------------------
        
        player.loop(FPS)                                                      # CHECK FOR PLAYER UPDATES
              
        # UPDATING PLAYER MOVEMENT # ------------------------------------------
        
        handle_move(player, terrain, lemon)                                   # PLAYER INTERACTIONS WITH OBJECTS
        
        # PLAYER HEALTH # -----------------------------------------------------
        
        damage(player, spikes, mosquitos, bees, grasshopper, ladybug)         # DAMAGE FUNCTION
        
        if player.health < 1 or player.rect.top > HEIGHT - 25:                # PLAYER FALL DEATH
            level_1_start = False
            game_over     = True
            
        if player.rect.x / 80 > 220 and player.rect.x / 80 < 225:             # PLAYER ADVANCMENT CUTSCENE ACTICATION
            level_1_start = False
            ambush        = True
            
        if pygame.sprite.collide_mask(player, guns[1]):                       # PLAYER PICKS UP GUN
            level_1_start = False
            end_scene = True
            
        # DRAWING SPRITES # ---------------------------------------------------
        
        draw(screen, background, tunnel, terrain, lemon, bees, spikes, mosquitos, grasshopper, health_bar, player, ladybug, guns, kermit, frogs, offset_x, offset_y)  # DRAW EVERYTHING
        
       # DETECTING COLLISIONS # ----------------------------------------- 

        for lem in lemon:                                                     # LEMON UPDATES
            lem.update()
            lem.lemon_collision(player)
            
        for bee in bees:                                                      # BEE UPDATES
            bee.update()
            
        for mos in mosquitos:                                                 # MOSQUITO UPDATES
            mos.update()
            
        for grass in grasshopper:                                             # GRASSHOPPER UPDATES
            grass.update()
            
        for lady in ladybug:                                                  # LADYBUG UPDATES
            lady.update()
            
        for gun in guns:                                                      # GUN UPDATES
            gun.update()

       # CUTSCENE TEXT DISPLAY # ----------------------------------------------        

        if display_gun_text: 
            gun_surface = pygame.Surface((WIDTH, HEIGHT))                           # DISPLAY GUN SURFACE
            gun_surface.fill(BLACK)                                                 
            font = pygame.font.Font(path + 'Font/Pixeltype.ttf', 36)                # FONT
            gun_text  = "GRAB THE GUN!"                                             # MESSAGE  
            draw_text(gun_surface, gun_text, font, 'red', WIDTH // 2, HEIGHT // 3 ) # DISPLAY TEXT
            pygame.display.flip()                                                   # UPDATE
                        
        # Y CAMERA MOVEMENT #--------------------------------------------------
        
        if ((player.rect.top - offset_y >= HEIGHT - scroll_area_width/1.25) and player.y_vel >0) or ((player.rect.bottom - offset_y <= scroll_area_width/1.25) and player.y_vel < 0):
            offset_y += player.y_vel 
        
        # X CAMERA MOVEMENT #--------------------------------------------------
        
        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width * 2.5) and player.x_vel >0) or ((player.rect.left - offset_x <= scroll_area_width * 2.5) and player.x_vel < 0):
            offset_x += player.x_vel
        
        # AMBUSH CUTSCENE # ---------------------------------------------------   
        
        while ambush:
            get_sounds('Lewis_Screaming_1.mp3', .5, 0)                              # LOAD SCREAMING SOUND                          
            bg_music.set_volume(0)                                                  # TURN OFF MUSIC
            bg_music_2       = get_sounds('intense_music.mp3', .3, 0)               # LOAD NEW MUSIC
            ambush_screen()                                                         # DISPLAY AMBUSH SCREEN
            ambush           = False                                                # DEACTIVATE CUTSCENE
            spawn_point_x    = [213 * block_size, 232 * block_size]                 # PLAYER X SPAWN POINT
            spawn_point_y    = [HEIGHT - 25 * block_size, HEIGHT - 25 * block_size] # PLAYER Y SPAWNPOINT
            player           = Player(spawn_point_x[1], spawn_point_y[1], 50, 50)   # SPAWN PLAYER AT X AND Y
            offset_y         = -22.371 * 80                                         # CAMERA X START
            offset_x         = 230.675 * 80                                         # CAMERA Y START
            display_gun_text = True                                                 # DISPLAY TEXT ACTIVATE
            level_1_start    = True                                                 # GAME ACTIVATE
        
        while end_scene:
            bg_music_2.set_volume(0)                                                # TURN OFF MUSIC
            end_screen_1()                                                          # SCENE 1
            end_screen_2()                                                          # SCENE 2
            end_screen_3()                                                          # SCENE 3 
            end_screen_4()                                                          # SCENE 4
            end_screen_5()
                        
### GAME OVER SCREEN ### ------------------------------------------------------
            
        while game_over:
            get_sounds('death.mp3', .5, 0)                                          # DEATH SOUND
            show_go_screen()                                                        # GAME OVER DISPLAY
            game_over      = False                                                  # DEACTIVATE GAME OVER
            spawn_point_x  = [2 * block_size, 230 * block_size]                   # PLAYER X SPAWN POINT
            spawn_point_y  = [HEIGHT - 2 * block_size, HEIGHT - 20 * block_size]   # PLAYER Y SPAWN POINT
            player         = Player(spawn_point_x[0], spawn_point_y[0], 50, 50)     # SPAWN PLAYER AT X AND Y 
            offset_y       = 0                                                      # CAMERA X RESET
            offset_x       = 0                                                      # CAMERA Y RESET
            player.health  = 5                                                      # PLAYER HEALTH RESET
            level_1_start  = True                                                   # ACTIVATE GAME
        
### QUIT ### ------------------------------------------------------------------
        
    pygame.quit()
    quit() 
    
if __name__ == '__main__':
    main(screen)