import argparse

import os.path

import subjunctive

from subjunctive.grid import Grid, left, right, up, down

import random

#from . import generate_algorithm

subjunctive.resource.add_path(os.path.dirname(__file__))

class Player(subjunctive.entity.Entity):
    image = subjunctive.resource.image('images/player.png')

class Block(subjunctive.entity.Entity):
    image = subjunctive.resource.image('images/block.png')

class Paint(subjunctive.entity.Entity):
    image = subjunctive.resource.image('images/paint.png')

class World(subjunctive.world.World):
    tile_size = (16, 16)
    window_caption = "Floorpaint"
    grid = subjunctive.grid.Grid(25, 25)
    
    def setup(self, player):
        #self.place(player, self.center)
        pass
        
def generate_level(width, height):
    spaces = {(x, y): False for x in range(width)
                                    for y in range(height)}
 
    # algorithm blah blah
    x, y = 0, 0
    spaces[x, y] = True
    keepgoing = True
    num_steps = 0
    s = set()
    while keepgoing:
        choice_dir = random.choice(['down','up','right','left'])
        old_num_steps = num_steps
        s.add(choice_dir)
        if choice_dir == 'down':
            for i in range(random.randint(1,height/2)):
                if y+1<height and spaces[x, y+1]==False:
                    num_steps+=1
                    y+=1
                    spaces[x, y] = True
        elif choice_dir == 'up':
            for i in range(random.randint(1,height/2)):
                if y-1>0 and spaces[x, y-1]==False:
                    num_steps+=1
                    y-=1
                    spaces[x, y] = True
        elif choice_dir == 'right':
            for i in range(random.randint(1,width/2)):
                if x+1<width and spaces[x+1, y]==False:
                    num_steps+=1
                    x+=1
                    spaces[x, y] = True
        elif choice_dir == 'left':
            for i in range(random.randint(1,width/2)):
                if x-1>0 and spaces[x-1, y]==False:
                    num_steps+=1
                    x-=1
                    spaces[x, y] = True
        if old_num_steps != num_steps:
            s.clear()
        elif len(s) == 4:
            keepgoing =  False
            
        
        if num_steps>(width*height-20):
            keepgoing = False
 
    return spaces
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    grid = Grid(10, 10)
    world = World(grid)
    d = generate_level(10, 10)
    for (x, y), value in d.items():
        if not value:
            world.place(Block(world), grid.Location(x, y))
    #player = Player(world)
    #world.setup(player)

    #def move_player(direction):
        #player.move(direction, orient=True)
    subjunctive.run(world)
