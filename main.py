import pgzrun
import random


TITLE="Collecting Tomatoes from the Garden"
WIDTH=620
HEIGHT=413

START_SPEED=10
ITEMS = ["tomato","cucumber","carrot","cabbage"]
FINAL_LEVEL = 6
current_level = 1

#lose the game
game_over =False
#win the game
game_complete=False

items = []
animations = []

def draw():
    global items, game_over,game_complete,current_level
    screen.clear()
    screen.blit("bground",(0,0))

    if game_over:
        #Abstraction-Trying to call a user defined function before creating it
        display_message("GAME OVER","Try again")
    elif game_complete:
        display_message("GOOD JOB!","You won!")
    else:
        for item in items:
            item.draw()

def display_message(heading,sub_heading):
    screen.draw.text(heading,fontsize=60,center=(WIDTH // 2, HEIGHT // 2 - 30), color="white")
    screen.draw.text(sub_heading,fontsize=50,center=(WIDTH // 2, HEIGHT // 2 + 30),color="white")

def update():
    global items

    if len(items)==0:
        items= make_items(current_level)

#Decomposition: breaking down a problem into small chunks/portions and solving it seperately
#Make items
#1.get the options from ITEMS list- random
#2.Create actors and add it to items list
#3.Layout items-display them with equal spacing
#4.Animations-move objects down

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)

    return new_items


def get_option_to_create(number_of_extra_items):
    items_to_create=['tomato']
    non_tomato_items = [item for item in ITEMS if item != 'tomato']
    for i in range(0,number_of_extra_items):
        random_option=random.choice(non_tomato_items)
        items_to_create.append(random_option)
    return items_to_create


def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        item= Actor(i)
        new_items.append(item)
    return(new_items)

    
def layout_items(items_to_layout):
    number_of_gaps= len(items_to_layout) + 1
    gap_size= WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index +1) * gap_size
        item.x= new_x_pos

def animate_items(items_to_animate):
    global animations
    for items in items_to_animate:
        duration= START_SPEED - current_level
        animation= animate(items,duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if 'tomato' in item.image:
                handle_game_complete()
            else:
                handle_game_over() 

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    
    if current_level== FINAL_LEVEL:
        game_complete= True
    else:
        current_level=current_level+1
        items=[]
        animations=[] 

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()