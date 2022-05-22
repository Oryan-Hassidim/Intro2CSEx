from car import Car

VERTICAL = 0
HORIZONTAL = 1
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"


def test_get_name():
    car = Car("a", 2, (0, 0), VERTICAL)
    assert "a" == car.get_name()
    car2 = Car("abra123", 2, (0, 0), VERTICAL)
    assert "abra123" == car2.get_name()


def test_initial_car_coordinates():
    car1 = Car("test", 4, (2,-2), VERTICAL)
    car2 = Car("test", 4, (2,2), HORIZONTAL)
    car3 = Car("test", 1, (2, 2), VERTICAL)
    assert sorted([
        (2,-2), (3,-2), (4,-2), (5,-2)
    ]) == sorted(car1.car_coordinates())
    assert sorted([
        (2,2), (2,3), (2,4), (2,5)
    ]) == sorted(car2.car_coordinates())
    assert sorted([
        (2, 2)
    ]) == sorted(car3.car_coordinates())


def test_possible_moves():
    car = Car("test", 2, (1,4), VERTICAL)
    car2 = Car("test", 4, (1,4), HORIZONTAL)

    possible_moves = set(car.possible_moves().keys())
    assert sorted([MOVE_UP, MOVE_DOWN]) == sorted(possible_moves)
    possible_moves2 = set(car2.possible_moves().keys())
    assert sorted([MOVE_LEFT, MOVE_RIGHT]) == sorted(possible_moves2)


def test_move():
    # moving in valid direction
    car = Car("test", 2, (1,4), VERTICAL)
    coords0 = car.car_coordinates()
    assert car.move(MOVE_UP)
    coords1 = car.car_coordinates()
    assert [(row-1, col) for row, col in sorted(coords0)] == sorted(coords1)
    assert car.move(MOVE_DOWN)
    coords2 = car.car_coordinates()
    assert coords2 == coords0

    car = Car("test", 3, (1,2), HORIZONTAL)
    coords0 = car.car_coordinates()
    assert car.move(MOVE_RIGHT)
    coords1 = car.car_coordinates()
    assert [(row, col+1) for row,col in sorted(coords0)] == sorted(coords1)
    assert car.move(MOVE_LEFT)
    coords2 = car.car_coordinates()
    assert sorted(coords0) == sorted(coords2)

    # moving in wrong direction
    car = Car("kk", 2, (1,4), VERTICAL)
    coords0 = car.car_coordinates()
    assert not car.move(MOVE_RIGHT)
    assert sorted(coords0) == sorted(car.car_coordinates())
    assert not car.move(MOVE_LEFT)
    assert sorted(coords0) == sorted(car.car_coordinates())

    # moving in non existent direction
    car = Car("kk", 2, (1,4), VERTICAL)
    coords0 = car.car_coordinates()
    assert not car.move("abcd")
    assert sorted(coords0) == sorted(car.car_coordinates())

    # cars have no bound limits
    car = Car("woot", 2, (0, 0), HORIZONTAL)
    assert car.move(MOVE_LEFT)
    assert sorted([(0, -1), (0, 0)]) == sorted(car.car_coordinates())


def test_move_requirements():
    car = Car("oki", 2, (2,4), HORIZONTAL)
    assert sorted([(2,6)]) == sorted(car.movement_requirements(MOVE_RIGHT))
    assert sorted([(2,3)]) == sorted(car.movement_requirements(MOVE_LEFT))

    car = Car("oki", 2, (2,4), VERTICAL)
    assert sorted([(1,4)]) == sorted(car.movement_requirements(MOVE_UP))
    assert sorted([(4,4)]) == sorted(car.movement_requirements(MOVE_DOWN))
