from user304_rsf8mD0BOQ_1 import Vector
from user304_rsf8mD0BOQ_1 import Vector
from user304_rsf8mD0BOQ_1 import Vector

try:
    import simplegui
    import math
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import time
import codeskulptor

WIDTH = 800
HEIGHT = 600

MAPWIDTH = 2500
MAPHEIGHT = 2500

MODE_INTRO = 0
MODE_GAME = 1
MODE_DEATH = 2
game_mode = MODE_INTRO
dead = False
lives = 3

player = simplegui.load_image('https://i.ibb.co/X4dgVbS/player.png')
death = simplegui.load_sound('https://www.mboxdrive.com/Shenmue%20Original%20Sound%20Track%20A%20New%20Departure%20(128%20kbps).mp3')
#eat = simplegui.load_sound('')
music = simplegui.load_sound('https://www.mboxdrive.com/Shenmue%20Original%20Sound%20Track%20A%20New%20Departure%20(128%20kbps).mp3')

class Wheel:
    def __init__(self, pos, radius):
        self.pos = pos
        self.vel = Vector()
        self.radius = radius
        self.colour = 'Green'


    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)
        #canvas.draw_image(player, ...)

    def update(self):
        self.pos.add(self.vel)
        print(self.vel)
        self.vel.multiply(0)

        # Made by Ade
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
    global list_balls
    def __init__(self, list_balls):
        self.vel = Vector()
        self.on = False
        #self.list_of_ball = list_balls


    def draw (self, canvas):
        #number_balls = random.randint(0, 10)
        #pos = Vector(0, 0)
        #if self.on == False:
            #ball_list = []
            #for i in range(0 , number_balls):
               # X = random.randint(0, WIDTH)
               # Y = random.randint(0, HEIGHT)
               # pos = Vector(X, Y)
               # ball_list.append(pos)
        #self.on = True
        for ball in (list_balls):
            self.colour = ball['colour']
            canvas.draw_circle(ball['pos'].get_p(), ball['radius'], 1 ,self.colour, self.colour)

#	def update(self):

class Keyboard:

    # Initialises right and left keys as false as they have not been pressed yet
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False

    # while the key indicated is pressed, it becomes true
    # Made by Ade
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['space']:
            print("Start")
            init_game()
            self.space = True

    # When the key previously pressed is released, it becomes false
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['D']:
            self.right = False
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['A']:
            self.left = False
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['W']:
            self.up = False
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = False
        #if key == simplegui.KEY_MAP['space']:
            #print("End")
            #self.space = False

class Interaction:
    def __init__(self, wheel, keyboard, list_balls):
        self.wheel = wheel
        self.keyboard = keyboard
        self.list_balls = list_balls

    def update(self):
        scale = math.floor(self.wheel.radius)
        positive_calc = (1/(scale-5))**.05
        negative_calc = -(1/(scale-5))**.05
        if self.keyboard.right:
            self.wheel.vel.add(Vector(positive_calc, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(negative_calc, 0))
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, negative_calc))
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, positive_calc))
            #print(int(self.wheel.pos.get_p()[0]))

        for i in list_balls:
            x_position = math.floor(self.wheel.pos.get_p()[0])
            y_position = math.floor(self.wheel.pos.get_p()[1])
            hitbox = int(self.wheel.radius)

            if i['radius'] < self.wheel.radius:
                i['colour'] = 'Blue'

            for i in list_balls:
                x_position = math.floor(self.wheel.pos.get_p()[0])
                y_position = math.floor(self.wheel.pos.get_p()[1])

                distance = i['pos'].copy().subtract(self.wheel.pos).length()
                edge = i['radius'] + self.wheel.radius
                if distance <= edge:
                    if self.wheel.radius > i['radius']:
                        self.wheel.radius += i['radius']
                        i['radius'] = 0.00000000000000001
                        i['colour'] = 'Black'
                        music.play()
                    else:
                        print ("dead")
                        init_death()

            for b in list_balls:
                if self.wheel.radius > b['radius']:
                    b['colour'] = 'Blue'
list_balls = []
def generate():
    global list_balls
    count = 0
    number_balls = random.randint(10, 30)
    for i in range(0 , number_balls):
        count+=1
        if i<=5:
            radius = random.randint(4 , 5)
        elif i<=8:
            radius = random.randint(5,12)
        else:
            radius = random.randint(12, 20)
        velocity_x = random.randint(-20,20)
        velocity_y = random.randint(-20,20)
        xAxis = random.randint(20, WIDTH - 20)
        yAxis = random.randint(20, HEIGHT - 20)
        if yAxis in range(450,470):
                yAxis -= 50
        if xAxis in range(240,260):
                xAxis -= 50
        pos = Vector(xAxis, yAxis)
        speed = Vector(velocity_x, velocity_y)
        if radius >= 6:
            colour_of_ball = 'Red'
        else:
            colour_of_ball = 'Blue'
        ball_attributes = {'pos': pos,
                           'speed': speed,
                           'radius': radius,
                           'colour': colour_of_ball,
                            'id': count}
        list_balls.append(ball_attributes)

kbd = Keyboard()
wheel = Wheel(Vector(WIDTH / 2, HEIGHT - 40), 6)
balls = Balls(list_balls)
inter = Interaction(wheel, kbd, list_balls)
message1 = "CS1812 - Osmos"
message2 = "Press Space to begin"
message3 = "Use Cursor Keys or WASD to Move"
message4 = "By Igli, Belal, Ade, Yassir, Einsten, Mithril"
death_message1 = "GAME OVER"

def init_intro():
    global game_mode
    game_mode = MODE_INTRO

def init_game():
    global game_mode
    game_mode = MODE_GAME

def init_death():
    global game_mode
    game_mode = MODE_DEATH

def render_game(canvas):
    global game_mode

    inter.update()
    wheel.update()
    wheel.draw(canvas)
    balls.draw(canvas)

def render_intro(canvas):
    global game_mode
    global message1
    global message2
    global message3
    global message4

    INTRO_TEXT_COLOUR = "Yellow"
    canvas.draw_text(message1, [260,172], 30, INTRO_TEXT_COLOUR)
    canvas.draw_text(message2, [235, 300], 30,INTRO_TEXT_COLOUR)
    canvas.draw_text(message3, [127, 220], 30,INTRO_TEXT_COLOUR)
    canvas.draw_text(message4, [180, 450], 20 ,INTRO_TEXT_COLOUR)

def render_death(canvas):
    global game_mode
    global death_message1

    INTRO_TEXT_COLOUR = "Red"
    canvas.draw_text(death_message1, [160,172], 80, INTRO_TEXT_COLOUR)

def draw(canvas):
    global list_balls
    if game_mode == MODE_GAME:
        music.play()
        render_game(canvas)
    elif game_mode == MODE_INTRO:
        render_intro(canvas)
    elif game_mode == MODE_DEATH:
        death.play()
        render_death(canvas)
        music.rewind()
        #time.sleep(5)
        list_balls = []
        generate()
        render_intro(canvas)

generate()
frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
