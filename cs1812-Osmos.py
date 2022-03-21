from user304_rsf8mD0BOQ_1 import Vector

try:
    import simplegui
    import math
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import time

WIDTH = 500
HEIGHT = 500

MAPWIDTH = 2500
MAPHEIGHT = 2500

VERSION = "v1.5"
FONT_STYLE = "sans-serif"

# Game State
MODE_INTRO = 0
MODE_GAME = 1
MODE_DEATH = 2
game_mode = MODE_INTRO
dead = False

def init_game():
    global game_mode
    game_mode = MODE_GAME

class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = 10
        self.colour = 'Red'

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        
        if self.pos.x >= (WIDTH):
            self.pos.x = 0
        elif self.pos.x <= 0:
            self.pos.x = WIDTH
            
        elif self.pos.y >= HEIGHT:
            self.pos.y = 0
        elif self.pos.y <= 0:
            self.pos.y = HEIGHT
        else:
            pass
                    
class Balls:
    def __init__(self , list_balls , list_radius , wheel):
        self.vel = Vector()
        self.colour = 'green'
        self.on = False
        self.list_balls = list_balls
        self.list_radius = list_radius
        self.wheel = wheel
        self.track = -1
        self.in_collision = False

    def draw (self, canvas):
 
        for z , g in zip(self.list_balls , self.list_radius):
            if g > 10:
                self.colour = 'Blue'
            else:
                self.colour = 'Green'
            canvas.draw_circle(z.get_p(), g, 1, self.colour, self.colour)

    def outside(self , track):
        for i , s in zip(self.list_balls , self.list_radius):
            distance = i.copy().subtract(self.wheel.pos).length()
            track = self.track + 1
        #distance = self.pos.copy().subtract(ball.pos).length()
            edge = s + self.wheel.radius
            if distance < edge :
                self.list_balls.pop(track)
                self.list_radius.pop(track)
                self.wheel.radius = self.wheel.radius + 5
                time.sleep(1)

    def update(self , track):
        Balls.outside(self , track)

class Keyboard:

    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = True
        if key and game_mode == MODE_INTRO:
            if key == simplegui.KEY_MAP['space']:
                init_game()

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['D']:
            self.right = False
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['A']:
            self.left = False
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['W']:
            self.up = False
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = False

class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, -1))
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, 1))
            
list_balls = []
list_radius= []
number_balls = random.randint(5, 10)
for i in range(0 , number_balls):
    radius = random.randint(8 , 20)
    X = random.randint(20, WIDTH - 20)
    Y = random.randint(20, HEIGHT - 20)
    pos = Vector(X, Y)
    list_radius.append(radius)
    list_balls.append(pos)
    
kbd = Keyboard()
wheel = Wheel(Vector(WIDTH / 2, HEIGHT - 40), 40)
balls = Balls(list_balls , list_radius , wheel)
inter = Interaction(wheel, kbd)
track = -1

def get_canvas_centre():
    return ( WIDTH // 2, HEIGHT // 2 )

def draw_text_centre( canvas, text, y, size, colour ):
    centre = get_canvas_centre()
    pos = ( centre[ 0 ] - frame.get_canvas_textwidth( text, size, FONT_STYLE ) // 2, y )
    canvas.draw_text( text, pos, size, colour, FONT_STYLE )
    
def draw_text_right( canvas, text, x, y, size, colour ):
    pos = ( x - frame.get_canvas_textwidth( text, size, FONT_STYLE ), y )
    canvas.draw_text( text, pos, size, colour, FONT_STYLE )
    
def render_intro(canvas):
    INTRO_TEXT_COLOUR = "Yellow"
    centre = get_canvas_centre()    
    draw_text_centre( canvas, "CS1812 - Osmos", 190, 58, INTRO_TEXT_COLOUR )
    draw_text_centre( canvas, "Press Space to begin", 340, 24, INTRO_TEXT_COLOUR )
    draw_text_centre( canvas, "Use Cursor Keys OR WASD to move", 420, 19, INTRO_TEXT_COLOUR )
    draw_text_centre( canvas, "By Igli, Belal, Ade, Yassir, Einsten, Mithril", 450, 16, INTRO_TEXT_COLOUR )
    draw_text_right( canvas, VERSION, WIDTH - 16, 14, 14, INTRO_TEXT_COLOUR )

def render_game(canvas):
    global game_mode
    
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    balls.draw(canvas)
    balls.update(track)
    
def draw(canvas):
    if game_mode == MODE_GAME:
        render_game(canvas)
    elif game_mode == MODE_INTRO:
        render_intro(canvas)

frame = simplegui.create_frame('CS1812 - Osmos', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
