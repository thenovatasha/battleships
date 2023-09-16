import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):

    # Building the storage array
    storage = update_storage(storage, p1ShotSeq, p1PrevHit)

    # Creating a heatmap
    heatmap = []
    heatmap = zero_heatmap(heatmap)
    heatmap = heatmap_misses(storage, heatmap)
    heatmap = heatmap_hits(storage, heatmap)
    
    # Choose a coord from the heatmap
    coord = select_from_heatmap(heatmap)

    # Return this coordinate as a guess
    x, y = coord[0], coord[1]
    return [x,y], storage
    


# HELPER FUNCTIONS HERE
def print_key_info(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    """
    - Round is an integer storing how many total hits have been made
    - yourHp and enemyHp are integers 
    - yourmap is a 10x10 list showing the status of each square: 
        0 (empty ocean), 1 (miss), 2 (unhit ship), -1 (hit ship)
    - p1ShotSeq stores the coords (as lists in lists aka [[7, 6], [6, 10]]) of
    all of the previous shots we have made, but does not tell us whether they 
    were hits or misses
    - p1PrevHit is a boolean, whether the last iten in p1ShotSeq was a hit
    - storate is an empty list, we will use it to store (x
    """
    print(f"Round: {round}")
    print(f"Yourmap: {yourMap}")
    print(f"yourHp: {yourHp}")
    print(f"enemyHp: {enemyHp}")
    print(f"p1ShotSeq: {p1ShotSeq}")
    print(f"p1PrevHit: {p1PrevHit}")
    print(f"Storage: {storage}")


def update_storage(storage, p1ShotSeq, p1PrevHit):
    """ Update the storage list to hold """
    # IMPORTANT: TO UPDATE STORAGE YOU MUST CALL FUNCTION AS storage = updateStorage(., ., .)
    # takes 1-10 coord but converts to 0-9
    # if storage has something in it, update, otherwise initialise
    UNKNOWN = 0
    HIT = -1
    MISS = 1
    if (storage):
        # update, indexing in terms of x-1 and y-1
        lastShot = p1ShotSeq[-1]
        if p1PrevHit:
            storage[lastShot[0]-1][lastShot[1]-1] = HIT
        else:
            storage[lastShot[0]-1][lastShot[1]-1] = MISS
        return storage
    else:
        #initialise
        initStorage = []
        for row in range(10):
            initInnerRow = 10*[UNKNOWN]
            initStorage.append(initInnerRow)
        storage = initStorage
        return storage


def zero_heatmap(heatmap):
    """ Set the heatmap to all zeros """
    for x in range(10):
        heatmap.append([])
        for y in range(10):
            heatmap[x][y] = 0
    return heatmap

def heatmap_misses(storage, heatmap):
    heatmap = [[]]
    return heatmap


def heatmap_hits(storage, heatmap):
    HIT = -1
    for r in range(10):
        for c in range(10):
            if storage[r][c] == HIT:
                # check left
                if valid_coord(r, c-1, heatmap):
                    heatmap[r][c-1] += 100
                # check right
                if valid_coord(r, c+1, heatmap):
                    heatmap[r][c+1] += 100
                # check above
                if valid_coord(r-1, c, heatmap):
                    heatmap[r-1][c] += 100
                # check below
                if valid_coord(r+1, c, heatmap):
                    heatmap[r+1][c] += 100
    return heatmap


def valid_coord(x, y, heatmap):
    return (0<=x<=9 and 0<=y<=9 and heatmap[x][y] != 0)


def select_from_heatmap(heatmap):
    # Find the largest heatmap value
    max_heat_val = 0
    for x in range(10):
        for y in range(10):
            heat_val = heatmap[x][y]
            if heat_val >= max_heat_val:
                max_heat_val = heat_val
    
    # Find the coordinates of these largest values
    max_coords = []
    for x in range(10):
        for y in range(10):
            heat_val = heatmap[x][y]
            if heat_val == max_heat_val:
                max_coords.append((x, y))
    
    # Break tiebreakers between items in max_coords
    if len(max_coords) > 1:
        # Only take coordinates along diagonals to choose from a checkerboard
        # pattern of coordinates for more efficient guessing
        for coord in max_coords:
            if ((coord[0] + coord[1])/2 != 0):
                max_coords.remove(coord)
        
    # If there are still multiple coords left after this process, choose 
    # one randomly
    return random.choice(max_coords)