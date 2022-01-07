#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    counter = 1
    for row in grid:
        if 'p' in row:
            px = row.index('p') + 1
            py = m - counter + 1
#             print( f"Location of princess = ({px}, {py})" )
        if 'm' in row:
            mx = row.index('m') + 1
            my = m - counter + 1
#             print( f"Location of bot = ({mx}, {my})" )
        counter += 1
    dx = px - mx
    dy = py - my
    if dx > 0:
        for i in range(dx):
            print('RIGHT')
    else:
        for i in range(abs(dx)):
            print('LEFT')
    if dy > 0:
        for i in range(dy):
            print('UP')
    else:
        for i in range(abs(dy)):
            print('DOWN')
        
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
