
def hitforDraw(row, column, fleet):
    # define the list of tuples for each ship
    shot = (row, column)
    coordinates_in_fleet = []
    for ship in fleet:
        if ship[2]:
            for i in range(ship[1], ship[1] + ship[3] ):
                p = (ship[0], i)
                coordinates_in_fleet.append(p)
            if shot in coordinates_in_fleet:
                return ship
            else:
                coordinates_in_fleet = []
        else:
            for i in range(ship[0], ship[0] + ship[3]):
                p = (i, ship[1])
                coordinates_in_fleet.append(p)
            if shot in coordinates_in_fleet:
                return ship
            else:
                coordinates_in_fleet = []

    #return None

def ship_Letter(ship):
    if ship[3] == 1:
        return " S "
    elif ship[3] == 2:
        return " D "
    elif ship[3] == 3:
        return " C "
    elif ship[3] == 4:
        return " B "

def visualize(fleet,shotpoints):

    mString = "\n   0  1  2  3  4  5  6  7  8  9\n________________________________\n"
    for r in range(0, 10):
        mString += str(r)
        mString += "|"
        for c in range(0, 10):
            ship = hitforDraw(r, c, fleet)
            if ship == None:
                if (r,c) in shotpoints:
                    mString += " - "
                else:
                    mString += " . "
            else:
                if len(ship[4]) == ship[3]:
                    mString += ship_Letter(ship)
                else:
                    if (r, c) in shotpoints:
                        mString += " * "
                    else:
                        mString += " . "
        mString += "\n"
    print(mString)

