import random

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    
    # FOR SEARCHING
        # Get the position of all hits and misses

        # Simulate placing all 5 ships on the current board x amounts of time
            # Hit coords must have part of a ship put on them
            # No part of a ship can be put on a missed coord

        # Record every time in x 'ship placements' that a ship is put on a
        # coord

        # This should generate a matrix where each square has the number of 
        # times a ship was put on it in 'ship placement' simulation

        # Remove all 'odd' coords from this matrix

        # Pick a random square, with the probability of picking that square 
        # given by the number on the square
    
    # When 5 hits have been made,
    # FOR DESTROYING
        # Consider possibilites of where each ship can fit based on position
        # of hits and misses

            # Possibly use the same simulation approach as Searching:  For 
            # each hit, pick a random ship, a random orientation and a random
            # position on the ship that should lie above the hit
            
                # Take into account not only the misses around the ship that
                # limit it's position but also the hits - try to make guesses
                # for the position of a ship that cover multiple preexisting 
                # hits

            # Whichever combination of ships, ship positions and orientations
            # occured the most, make a guess based on that combination

            # Always guess a coord directly adjacent to the hit being searched 
            # around to avoid complete misses that don't give much info about
            # the ship
    
    
    # If hp != 0 when DESTROYING phase is finished, return to the searching phase

    return [x,y] 