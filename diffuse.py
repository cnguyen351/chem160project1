import random
from random import choice

npart=500
side=49  #Should be an odd number
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
density=float(input("density"))
maxsteps=10000
perc=0

for ipart in range(npart):
    # Start particle at center
    x = side//2
    y = side//2
    for x in range(side):
        for y in range(side):
            grid[x][y]=random.randint(0,100)
            if grid[x][y] <= (density*100):
                grid[x][y] = 1
            else:
                grid[x][y] = 0
            # perform the random walk until particle departs
    x = side//2
    y = side//2
    for i in range(maxsteps):
        #Remove particle from current spot
        grid[x][y] = 0
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            perc += 1
            break
        #Put particle in new location
        if grid[x][y] == 1 :
            x -= sx
            y -= sy
        continue

print(perc/npart)