from user304_rsf8mD0BOQ_1 import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

WIDTH = 500
HEIGHT = 500


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
    def __init__(self , list_balls , list_radius):
        self.vel = Vector()
        self.colour = 'green'
        self.on = False
        self.list_balls = list_balls
        self.list_radius = list_radius


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
        for z , g in zip(self.list_balls , self.list_radius):
            if g > 10:
                self.colour = 'Blue'
            else:
                self.colour = 'Green'
            canvas.draw_circle(z.get_p(), g, 1, self.colour, self.colour)
            
#	def update(self):

                


class Keyboard:

    # Initialises right and left keys as false as they have not been pressed yet
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    # while the key indicated is pressed, it becomes true
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = True

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
balls = Balls(list_balls , list_radius)
inter = Interaction(wheel, kbd)




def draw(canvas):
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    balls.draw(canvas)


frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
