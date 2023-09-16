import random

def getShipPos():
    '''
    THIS IS THE LIST OF SHIPS
    [5,3,3,2,2] 
    That is: 
    1x 5 long
    2x 3 long
    2x 2 long

    Your ships must satisfy this 
    Ship positions must be (0-9, 0-9)
    '''
    # GENERATE SHIP POSITIONS
    # List of ships that must be placed
    remaining_ships = [5, 3, 3, 2, 2]
    shipPos = []
    all_pos = []
    # Place ships in a random order
    
    # Put down all ships
    for ship in remaining_ships:
        fits = False
        while (not fits):
            fits = True
            this_shipPos = []
            if bool(random.getrandbits(1)):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                x_end = x+ship
                for x_counter in range(x, x_end):
                    this_shipPos.append((x_counter, y))
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                y_end = y+ship
                for y_counter in range(y, y_end):
                    this_shipPos.append((x, y_counter))

            for coord in this_shipPos:
                on_board = bool(0<=coord[0]<=9 and 0<=coord[1]<=9)
                for old_shipPos in shipPos:
                    for old_coord in old_shipPos:
                        if ((on_board != True) or coord == old_coord):
                            fits = False

                
        
                
        shipPos.append(this_shipPos)

    """
    shipPos = [[(3,1), (4,1),(5,1)], 
                [(2,1),(2,2),(2,3),(2,4),(2,5)], 
                [(7,7),(8,7)] , 
                [(0,9), (1,9), (2,9)], 
                [(5,9), (6,9)]]
    """
    return shipPos
