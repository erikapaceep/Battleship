import pytest
from battleships import *

s = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})
s1 = (1, 1, True, 4, {(1, 1), (1, 2), (1, 3)})
s2 = (8, 6, True, 2, {})
s3 = (0, 0, False, 3, {(0, 0), (1, 0), (2, 0)})
s4 = (1, 1, True, 1, {(1, 1)})


def test_is_sunk1():
    # (row, column, horizontal, length, hits)
    assert is_sunk(s) == True


def test_is_sunk2():
    assert is_sunk(s1) == False


def test_is_sunk3():
    assert is_sunk(s2) == False


def test_is_sunk4():
    assert is_sunk(s3) == True


def test_is_sunk5():
    assert is_sunk(s4) == True


# add at least four more tests for is_sunk by the project submission deadline

def test_ship_type():
    assert ship_type(s) == "cruiser"


def test_ship_type1():
    assert ship_type(s1) == "battleship"


def test_ship_type2():
    assert ship_type(s2) == "destroyer"


def test_ship_type3():
    assert ship_type(s3) == "cruiser"


def test_ship_type4():
    assert ship_type(s4) == "submarine"

    # add at least one test for ship_type by the deadline of session 7 assignment
    # provide at least five tests in total for ship_type by the project submission deadline


def test_is_open_sea():
    row = 0
    column = 0
    fleet = [(2, 2, False, 1, set()), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert is_open_sea(row, column, fleet) == True


def test_is_open_sea1():
    assert is_open_sea(0, 0, [(1, 1, False, 1, set()), (1, 3, True, 4, set()), (1, 9, False, 1, set()),
                              (3, 1, False, 1, set()), (3, 4, True, 2, set())]) == False


def test_is_open_sea2():
    assert is_open_sea(0, 0, [(1, 0, False, 1, set()), (2, 3, True, 4, set())]) == False


def test_is_open_sea3():
    assert is_open_sea(0, 0, [(3, 3, False, 3, set()), (7, 1, True, 4, set())]) == True


def test_is_open_sea4():
    assert is_open_sea(0, -1, [(0, 0, False, 3, set()), (7, 1, True, 4, set())]) == False


def test_is_open_sea5():
    assert is_open_sea(9, 11, [(3, 3, False, 3, set()), (7, 1, True, 4, set())]) == False
    # add at least one test for open_sea by the deadline of session 7 assignment
    # provide at least five tests in total for open_sea by the project submission deadline





def test_ok_to_place_ship_at():
    fleet = [(1, 1, False, 1, {(1, 1)}), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (5, 0, False, 2, {(5, 0), (6, 0)}), (6, 3, False, 1, {(6, 3)})]
    assert ok_to_place_ship_at(0, 0, False, 3, fleet) == False


def test_ok_to_place_ship_at1():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),
             (3, 3, True, 3, set()), (5, 0, False, 2, set()), (6, 3, False, 1, set())]
    assert ok_to_place_ship_at(7, 8, False, 4, fleet) == False


def test_ok_to_place_ship_at2():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),
             (3, 3, True, 3, set()), (5, 0, False, 2, set()), (6, 3, False, 1, set())]
    assert ok_to_place_ship_at(7, 2, True, 2, fleet) == False


def test_ok_to_place_ship_at3():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),
             (3, 3, True, 3, set()), (5, 0, False, 2, set()), (6, 3, False, 1, set())]
    assert ok_to_place_ship_at(0, 7, False, 1, fleet) == False


def test_ok_to_place_ship_at4():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),
             (3, 3, True, 3, set()), (5, 0, False, 2, set()), (6, 3, False, 1, set())]
    assert ok_to_place_ship_at(7, 5, False, 2, fleet) == True

    # add at least one test for place_ship_at by the deadline of session 7 assignment
    # provide at least five tests in total for place_ship_at by the project submission deadline


def test_place_ship_at():
    s1 = (1, 1, False, 1, set())
    s2 = (1, 3, True, 4, set())
    s3 = (3, 3, True, 3, set())
    s4 = (5, 0, False, 2, set())
    s5 = (6, 3, False, 1, set())

    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()), (3, 3, True, 3, set()), (5, 0, False, 2, set()),
             (6, 3, False, 1, set())]

    actual = place_ship_at(5, 6, True, 2, fleet)
    actual.sort()
    expected = [s1, s2, s3, s4, s5, (5, 6, True, 2, set())]
    expected.sort()
    assert expected == actual


def test_place_ship_at1():
    s1 = (1, 1, False, 1, set())
    s2 = (1, 3, True, 4, set())
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set())]
    actual = place_ship_at(8, 8, True, 1, fleet)
    actual.sort()
    expected = [s1, s2, (8, 8, True, 1, set())]
    expected.sort()
    assert expected == actual


def test_place_ship_at2():
    s1 = (1, 1, False, 1, set())
    s2 = (1, 3, True, 4, set())
    s3 = (3, 3, True, 3, set())
    s4 = (5, 0, False, 2, set())
    s5 = (6, 3, False, 1, set())
    s6 = (8, 7, True, 2, set())

    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()), (3, 3, True, 3, set()), (5, 0, False, 2, set()),
             (6, 3, False, 1, set()), (8, 7, True, 2, set())]
    actual = place_ship_at(9, 0, True, 2, fleet)
    actual.sort()
    expected = [s1, s2, s3, s4, s5, s6, (9, 0, True, 2, set())]
    expected.sort()
    assert expected == actual

def test_place_ship_at3():
    s1 = (1, 1, False, 1, set())
    s2 = (1, 3, True, 4, set())
    s3 = (3, 3, True, 2, set())
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),(3, 3, True, 2, set())]
    actual = place_ship_at(5, 8, False, 2, fleet)
    actual.sort()
    expected = [s1, s2, s3, (5, 8, False, 2, set())]
    expected.sort()
    assert expected == actual


def test_place_ship_at4():
    s1 = (1, 1, False, 1, set())
    s2 = (1, 3, True, 4, set())
    s3 = (3, 3, True, 2, set())
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, set()),(3, 3, True, 2, set())]
    actual = place_ship_at(5, 5, False, 3, fleet)
    actual.sort()
    # specification of place_ship_at does not mandate any order on ships in a fleet, so we need
    # to sort expected and actual fleets in order to use == safely
    expected = [s1, s2, s3, (5, 5, False, 3, set())]
    expected.sort()
    assert expected == actual

def test_check_if_hits():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (3, 3, True, 3, set()), (5, 0, False, 2, {(5, 0)}), (6, 3, False, 1, set())]
    assert check_if_hits(1, 1, fleet) == True


def test_check_if_hits1():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (3, 3, True, 3, set()), (5, 0, False, 2, {(5, 0)}), (6, 3, False, 1, set())]
    assert check_if_hits(0, 1, fleet) == False


def test_check_if_hits2():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (3, 3, True, 3, set()), (5, 0, False, 2, {(5, 0)}), (6, 3, False, 1, set())]
    assert check_if_hits(1, 2, fleet) == False


def test_check_if_hits3():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (3, 3, True, 3, set()), (5, 0, False, 2, {(5, 0)}), (6, 3, False, 1, set())]
    assert check_if_hits(1, 6, fleet) == True


def test_check_if_hits4():
    fleet = [(1, 1, False, 1, set()), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (3, 3, True, 3, set()), (5, 0, False, 2, {(5, 0)}), (6, 3, False, 1, set())]
    assert check_if_hits(7, 2, fleet) == False
    # add at least one test for check_if_hits by the deadline of session 7 assignment
    # provide at least five tests in total for check_if_hits by the project submission deadline


def test_hit():
    # (row, column, fleet)
    fleet = [(2, 1, True, 2, set()), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    fleet1 = [(2, 1, True, 2, {(2, 1)}), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert hit(2, 1, fleet) == (fleet1, (2, 1, True, 2, {(2,1)}))
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline

def test_hit1():
    # (row, column, fleet)
    fleet = [(1, 1, True, 1, set()), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    fleet1 = [(1, 1, True, 1, {(1, 1)}), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert hit(1, 1, fleet) == (fleet1, (1, 1, True, 1, {(1,1)}))
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline

def test_hit2():
    # (row, column, fleet)
    fleet = [(0, 0, True, 4, {(0,0),(0,1),(0,2)}), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    fleet1 = [(0, 0, True, 4, {(0,0),(0,1),(0,2),(0,3)}), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert hit(0, 3, fleet) == (fleet1, (0, 0, True, 4, {(0,0),(0,1),(0,2),(0,3)}))
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline

def test_hit3():
    # (row, column, fleet)
    fleet = [(0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)}), (2, 4, False, 1, set())]
    fleet1 = [(0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)}),(2, 4, False, 1, {(2,4)})]
    assert hit(2, 4, fleet) == (fleet1, (2, 4, False, 1, {(2,4)}))
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline

def test_hit4 ():
    # (row, column, fleet)
    fleet = [(0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)}), (2, 4, False, 1, {(2,4)}),(9,9,True,1,set())]
    fleet1 = [(0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)}),(2, 4, False, 1, {(2,4)}), (9,9,True,1,{(9,9)})]
    assert hit(9, 9, fleet) == (fleet1, (9, 9, True, 1, {(9,9)}))
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left():
    fleet = [(2, 1, True, 2, {(2, 1)}), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left1():
    fleet = [(1, 1, False, 1, {(1, 1)}), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5)}),
             (5, 0, False, 2, {(5, 0), (6, 0)}), (6, 3, False, 1, {(6, 3)})]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left2():
    fleet = [(1, 1, False, 1, {(1, 1)}), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5), (1, 6)}),
             (5, 0, False, 2, {(5, 0), (6, 0)}), (6, 3, False, 1, {(6, 3)})]
    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left3():
    fleet = [(1, 1, False, 1, {(1, 1)}), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5), (1, 6)}),
             (5, 0, False, 2, {(5, 0), (6, 0)}), (6, 3, False, 1, {})]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left4():
    fleet = [(1, 1, False, 1, {(1, 1)}), (1, 3, True, 4, {(1, 3), (1, 4), (1, 5), (1, 6)}),
             (5, 0, False, 2, {(5, 0), (6, 0)}), (6, 3, False, 1, {})]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left5():
    fleet = [(2, 1, True, 2, set()), (2, 4, False, 1, set()), (2, 6, False, 1, set())]
    assert are_unsunk_ships_left(fleet) == True

    # add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
