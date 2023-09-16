import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    # Declaring 
    UNKNOWN = 0
    HIT = -1
    MISS = 1

    # Primary logic 
    storage = update_storage(storage, p1ShotSeq, p1PrevHit)
    heatmap = heatmap(storage)
    
    # Find the largest 

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


def make_random_guess():
    """ Random guess for testing purposes """
    x = random.randint(0,9)
    y = random.randint(0,9)
    return x, y

def heatmap_misses(storage):
    heatmap = [[]]
    return heatmap

def heatmap_hits(storage):
    heatmap = [[]]
    return heatmap

def heatmap_zero_seen(storage):
    heatmap = [[]]
    return heatmap