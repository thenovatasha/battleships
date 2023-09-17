storage = [[0,-1,-1,-1,-1,-1,-1,0,0,0], 
		  [0,0,0,0,0,0,0,0,0,0], 
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,-1,0],
		  [0,0,0,0,0,0,0,0,-1,0],
		  [0,0,0,0,0,0,0,0,-1,0],
		  [0,1,0,0,0,0,0,0,-1,0],
		  [0,1,0,0,0,0,0,0,-1,0], 
		  [0,0,0,0,0,0,0,0,0,0]]

heatmap =[[0,0,0,0,0,0,0,0,0,0], 
		  [0,0,0,0,0,0,0,0,0,0], 
		  [0,0,0,0,0,0,0,0,0,0], 
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0]]

def heatmap_hits(storage, heatmap):
    HIT = -1
    for r in range(10):
        for c in range(10):
            is_single_hit = True
            if storage[r][c] == HIT:
                # check left
                if valid_coord(r, c-1, heatmap):
                    #heatmap[r][c-1] += 1
                    if storage[r][c-1] == HIT:
                        is_single_hit = False
                        if valid_coord(r, c+1, heatmap):
                            heatmap[r][c+1] += 5
                # check right
                if valid_coord(r, c+1, heatmap):
                    #heatmap[r][c+1] += 1
                    if storage[r][c+1] == HIT:
                        is_single_hit = False
                        if valid_coord(r, c-1, heatmap):
                            heatmap[r][c-1] += 5
                # check above
                if valid_coord(r-1, c, heatmap):
                    #heatmap[r-1][c] += 1
                    if storage[r-1][c] == HIT:
                        is_single_hit = False
                        if valid_coord(r+1, c, heatmap):
                            heatmap[r+1][c] += 5
                # check below
                if valid_coord(r+1, c, heatmap):
                    #heatmap[r+1][c] += 1
                    if storage[r+1][c] == HIT:
                        is_single_hit = False
                        if valid_coord(r-1, c, heatmap):
                            heatmap[r-1][c] += 5
                if is_single_hit:
                    if valid_coord(r, c-1, heatmap):
                        heatmap[r][c-1] += 5
                    if valid_coord(r, c+1, heatmap):
                        heatmap[r][c+1] += 5
                    if valid_coord(r-1, c, heatmap):
                        heatmap[r-1][c] += 5
                    if valid_coord(r+1, c, heatmap):
                        heatmap[r+1][c] += 5
                # add adjacency bonuses to hit squares which aren't adjacent to any hit square

                
                
    return heatmap
def valid_coord(x, y, heatmap):
    return (0<=x<=9 and 0<=y<=9 and heatmap[x][y] != 0)

def heatmap_zeros(storage, heatmap):
    HIT = -1
    MISS = 1
    UNKNOWN = 0
    for r in range(10):
        for c in range(10):
            if storage[r][c] != UNKNOWN:
                heatmap[r][c] = 0
    return heatmap
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

def update_horizontal_hits(x,y, storage, heatmap):
	i = 0
	count = 0
	if(storage[x][y] == -1):
		while(y + i < 10):
			if(storage[x][y + i] == -1):
				count += 1
				i += 1
			else:
				break
	if(y != 0 and storage[x][y - 1] == -1):
		return heatmap
	else:
		if(y + count < 10 and count == 5):
			heatmap[x][y + count] -= 5
		if(y - 1 >= 0 and count == 5):
			heatmap[x][y - 1] -= 5

    
def update_vertical_hits(x, y, storage, heatmap):
	i = 0
	count = 0
	if(storage[x][y] == -1):
		while(x + i < 10):
			if(storage[x + i][y] == -1):
				count += 1
				i += 1
			else:
				break
	if(x != 0 and storage[x - 1][y] == -1):
		return heatmap
	else:
		if(x + count < 10 and count == 5):
			heatmap[x + count][y] -= 5
		if(x - 1 >= 0 and count == 5):
			heatmap[x - 1][y] -= 5
		
def update_edges(storage, heatmap):
	for i in range(0, 10):
		for j in range(0, 10):
			update_horizontal_hits(i, j, storage, heatmap)
			update_vertical_hits(i, j, storage, heatmap)
	return heatmap

def print_grid(array):
    for r in range(10):
        for c in range(10):
            print(array[r][c], end=" ")
        print()
    print()


heatmap = get_heat_map(storage, heatmap)
heatmap = heatmap_hits(storage, heatmap)
heatmap = update_edges(storage, heatmap)
heatmap = heatmap_zeros(storage, heatmap)

print_grid(heatmap)
