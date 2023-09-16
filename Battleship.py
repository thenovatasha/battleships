import random
def print_shots(storage):
	matrix_zeros = [[0 for i in range(10)] for j in range(10)]
	for i in range(10):
		for j in range(10):
			if storage[i][j] == -1:
				matrix_zeros[i][j] = 'X'
			elif storage[i][j] == 1:
				matrix_zeros[i][j] = '0'
			else:
				matrix_zeros[i][j] = '.'
	print_grid(matrix_zeros)
		
		
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):


    # Building the storage array
    storage = update_storage(storage, p1ShotSeq, p1PrevHit)
    print_shots(storage)

    # Creating a heatmap
    heatmap = zero_array()
    #print("SET HEATMAP TO ZEROS")
    #print_grid(heatmap)
    heatmap = get_heat_map(storage, heatmap)
    #print("CREATE HEATMAP BASED ON VALID SHIP POSITIONS")
    #print_grid(heatmap)
    heatmap = heatmap_hits(storage, heatmap)
    #print("BIAS HEATMAP BASED ON HITS")
    #print_grid(heatmap)
    # Choose a coord from the heatmap
    heatmap = heatmap_zeros(storage, heatmap)

    print_grid(heatmap)

    coord = select_from_heatmap(heatmap)



    # Return this coordinate as a guess
    x, y = coord[0], coord[1]
    # print(f"x: {x}, y: {y}")
    print(x+1, y+1)
    return [x+1,y+1], storage
    


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
        storage = zero_array()
        return storage


def zero_array():
    """ Set the heatmap to all zeros """
    initArray = []
    UNKNOWN = 0
    for row in range(10):
        initInnerRow = 10*[UNKNOWN]
        initArray.append(initInnerRow)
    return initArray


def heatmap_hits(storage, heatmap):
    HIT = -1
    for r in range(10):
        for c in range(10):
            is_single_hit = True
            if storage[r][c] == HIT:
                # check left
                if valid_coord(r, c-1, heatmap):
                    heatmap[r][c-1] += 1
                    if storage[r][c-1] == HIT:
                        is_single_hit = False
                        if valid_coord(r, c+1, heatmap):
                            heatmap[r][c+1] += 7
                # check right
                if valid_coord(r, c+1, heatmap):
                    heatmap[r][c+1] += 1
                    if storage[r][c+1] == HIT:
                        is_single_hit = False
                        if valid_coord(r, c-1, heatmap):
                            heatmap[r][c-1] += 7
                # check above
                if valid_coord(r-1, c, heatmap):
                    heatmap[r-1][c] += 1
                    if storage[r-1][c] == HIT:
                        is_single_hit = False
                        if valid_coord(r+1, c, heatmap):
                            heatmap[r+1][c] += 7
                # check below
                if valid_coord(r+1, c, heatmap):
                    heatmap[r+1][c] += 1
                    if storage[r+1][c] == HIT:
                        is_single_hit = False
                        if valid_coord(r-1, c, heatmap):
                            heatmap[r-1][c] += 7
                if is_single_hit:
                    if valid_coord(r, c-1, heatmap):
                        heatmap[r][c-1] += 4
                    if valid_coord(r, c+1, heatmap):
                        heatmap[r][c+1] += 4
                    if valid_coord(r-1, c, heatmap):
                        heatmap[r-1][c] += 4
                    if valid_coord(r+1, c, heatmap):
                        heatmap[r+1][c] += 4
                # add adjacency bonuses to hit squares which aren't adjacent to any hit square

                
                
    return heatmap

def heatmap_zeros(storage, heatmap):
    HIT = -1
    MISS = 1
    UNKNOWN = 0
    for r in range(10):
        for c in range(10):
            if storage[r][c] != UNKNOWN:
                heatmap[r][c] = 0
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
                max_coords.append([x, y])

    # If there are still multiple coords left after this process, choose 
    # one randomly
    return random.choice(max_coords)

def fit_ships(count): 
	''' Checks the number of ships that will fit in a given space 
		and returns the number of ships that will fit.'''
	
	# 5 ships fit	
	if count >= 5:
		return 5
	# 4 ships fit
	elif count >= 3:
		return 4
	# 3 ships fit
	elif count >= 2:
		return 2
	# no ships fit
	else:
		return 0

# function checks how many ships can fit to the right of the given coordinate
def check_right(x,y, storage):
	''' Checks how many ships can fit to the right of the given coordinate.'''
	i = 0
	# count amount of available spaces to the right
	count = 0
	# if within bounds of the board, keep checking 
	while(y + i < 10):
		# if coordinate has no hit or miss, increment count
		if storage[x][y + i] != 1:
			count += 1
		else:
			# if coordinate has a hit or miss, stop counting
			break
		i += 1
	# return the number of ships that can fit in the space	
	return fit_ships(count)
		
# function checks how many ships can fit to the left of the given coordinate
def check_left(x,y, storage):
	''' Checks how many ships can fit to the left of the given coordinate.'''
	i = 0
	# count spaces to the left
	count = 0
	# if within bounds of the board, keep checking
	while(y - i >= 0):
		# if coordinate has no hit or miss, increment count
		if storage[x][y - i] != 1:
			count += 1
		else:
			# coordinate has a hit or miss, stop counting
			break
		i += 1
	# return the number of ships that can fit in the space
	return fit_ships(count)	
	
def check_down(x,y, storage):
	''' Checks how many ships can fit below the given coordinate.'''
	i = 0
	count = 0
	# if within bounds of the board, keep checking
	while(x + i < 10):
		# if coordinate has no hit or miss, increment count
		if storage[x + i][y] != 1:
			count += 1
		else:
			break
		i += 1
	# return the number of ships that can fit in the space
	return fit_ships(count)

def check_up(x,y, storage):
	''' Checks how many ships can fit above the given coordinate. '''
	i = 0
	count = 0
	# if within bounds of the board, keep checking
	while(x - i >= 0):
		# if coordinate has no hit or miss, increment count
		if storage[x - i][y] != 1:
			count += 1
		# if coordinate has a hit or miss, stop counting
		else:
			break
		i += 1
	# return the number of ships that can fit in the space		
	return fit_ships(count)

def calculate_heat_map(storage, heatmap):
	''' Returns a heatmap of the board, with the number of ships that can fit in each space. '''
	
	for i in range(0, 10):
		for j in range(0, 10):
			# if coordinate has a hit or miss, set heatmap to 0
			if storage[i][j] == 1: # or storage[i][j] == -1:
				heatmap[i][j] = 0
			# if coordinate has no hit or miss, check how many ships can fit	
			else:
				# add all the ships that can fit in the space
				heatmap[i][j] = check_right(i, j, storage) + check_left(i, j, storage) + check_up(i, j, storage) + check_down(i, j, storage)

	return heatmap

def get_heat_map(storage, heatmap):
	return calculate_heat_map(storage, heatmap)

def print_grid(array):
    for r in range(10):
        for c in range(10):
            print(array[r][c], end=" ")
        print()
    print()
