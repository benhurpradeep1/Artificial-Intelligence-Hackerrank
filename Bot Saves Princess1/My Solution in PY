def displayPathtoPrincess(grid):
    
    # Get coordinates: 'Princess' (px,py) and 'Mario' (mx,my) from the grid
    my, py, i = None, None, -1
    while (my==None)|(py==None): 
        i+=1
        if 'm' in grid[i]:
            mx = i
            my = grid[i].index('m')  
        elif 'p' in grid[i]:
            px = i
            py = grid[i].index('p')
            
    # Calculate the Horizental and Vertical distances
    v_mv, h_mv = px-mx, py-my
    
    # Figure out the moves needed for the respective distances
    h_mvs = abs(h_mv)*["RIGHT" if h_mv>0 else "LEFT"]
    v_mvs = abs(v_mv)*["DOWN" if v_mv>0 else "UP"]
    
    # Figure out the path to reach Princess : should be alternating!
    all_mvs = [None]*(len(h_mvs)+len(v_mvs))
    all_mvs[::2] = v_mvs if len(v_mvs)>len(h_mvs) else h_mvs
    all_mvs[1::2] = v_mvs if len(v_mvs)<=len(h_mvs) else h_mvs
    print(*all_mvs, sep='\n')

n = int(input())
grid = [] 
for i in range(0, n): 
    grid.append(input().strip())

displayPathtoPrincess(grid)
