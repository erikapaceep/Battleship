#see the readme.md file for description and data 
import random
from extension import *

def is_sunk(ship):
    if len(ship[4]) == ship[3]:
        return True
    else:
        return False


def ship_type(ship):
    if ship[3] == 1:
        return "submarine"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3]== 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"

def is_open_sea(row, column, fleet):
    # define the list of tuples for each ship
    points = []
    for ship in fleet:
        if ship[2]:
            for i in range(ship[1] - 1, ship[1] + ship[3] + 1):
                for k in range(ship[0] - 1, ship[0] + 2):
                    p = (k, i)
                    if p[0] >= 0 and p[0] <= 9 and p[1] >= 0 and p[1] <= 9:
                        points.append(p)
        else:
            for i in range(ship[1] - 1, ship[1] + 2):
                for k in range(ship[0] - 1, ship[0] + ship[3] + 1):
                    p = (k, i)
                    if p[0] >= 0 and p[0] <= 9 and p[1] >= 0 and p[1] <= 9:
                        points.append(p)
    #print(points)
    el = (row, column)
    if el in points:
        return False
    else:
        if el[0]<0 or el[0]>9 or el[1]<0 or el[1]>9:
            return False
        else:
            return True
#print(is_open_sea(7, 2, fleet))


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    check =[]
    if horizontal:
       for i in range(0, length):
          p = is_open_sea(row, column+i, fleet)
          check.append(p)

    else:
       for i in range(0, length):
          p = is_open_sea(row+i, column, fleet)
          check.append(p)

    if False in check:
        return False
    else:
        return True

#to review
def place_ship_at(row, column, horizontal, length, fleet):
    new_ship = (row, column, horizontal, length, set(()))
    fleet.append(new_ship)
    return fleet

#to review
def randomly_place_all_ships():
    length_list = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    fleet = []
    for i in range(0, len(length_list)):
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        horizontal = random.choice([True, False])
        length = length_list[i]
        while not ok_to_place_ship_at(row, column, horizontal, length, fleet):
            row = random.randint(0, 9)
            column = random.randint(0, 9)
        fleet = place_ship_at(row, column, horizontal, length, fleet)
    return fleet

def check_if_hits(row, column, fleet):
    # define the list of tuples for each ship
    shot = (row, column)
    coordinates_in_fleet = []
    for ship in fleet:
        if ship[2]:
            for i in range(ship[1], ship[1] + ship[3]):
                p = (ship[0], i)
                coordinates_in_fleet.append(p)
        else:
            for i in range(ship[0], ship[0] + ship[3]):
                p = (i, ship[1])
                coordinates_in_fleet.append(p)

    if shot in coordinates_in_fleet:
        return True
    else:
        return False

def hit(row, column, fleet):
    hit = (row, column)
    point_in_fleet = []
    fleet1 = fleet
    for ship in fleet1:
        if ship[2]:
           for k in range(ship[1], ship[1] + ship[3]):
                p = (ship[0], k)
                if p[0] >= 0 and p[0] <= 9 and p[1] >= 0 and p[1] <= 9:
                   point_in_fleet.append(p)

        else:
            for i in range(ship[0], ship[0] + ship[3]):
                p = (i, ship[1])
                if p[0] >= 0 and p[0] <= 9 and p[1] >= 0 and p[1] <= 9:
                        point_in_fleet.append(p)
        if hit in point_in_fleet:
            ship[4].add(hit)
            return (fleet1, ship)
    return (fleet1, ship)


def are_unsunk_ships_left(fleet):
    unsunk_ship = []
    for ship in fleet:
        if len(ship[4]) == ship[3]:
            p = False
            unsunk_ship.append(p)
        else:
            p = True
            unsunk_ship.append(p)

    if True in unsunk_ship:
        return True
    else:
        return False

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0
    shotpoints =[]

    while not game_over:
        loc_str = input("Enter row and column to shoot (separted by space) if you wish to quit the game type quit:  ")
        if loc_str.lower() == "quit":
            game_over = True
        else:
            try:
                loc_str1 = loc_str.split()
                curr_row = int(loc_str1[0])
                curr_column = int(loc_str1[1])
                shots += 1
                p = (curr_row, curr_column)
                shotpoints.append(p)
                if check_if_hits(curr_row, curr_column, current_fleet):
                    print("You have a hit!")
                    result = hit(curr_row, curr_column, current_fleet)
                    current_fleet = result[0]
                    ship_hit = result[1]
                    if is_sunk(ship_hit):
                        print("You sank a " + ship_type(ship_hit) + "!")
                else:
                    print("You missed!")

                if not are_unsunk_ships_left(current_fleet): game_over = True
                print(visualize(current_fleet, shotpoints))
            except:
                print("Input is not valid, please enter valid coordinates or quit")
    if game_over:
        print("Game over! You required", shots, "shots.")

if __name__ == '__main__': #keep this in
   main()
