class Board:
    def __init__(self):
        self.__cars = {}

    def __str__(self):
        return str([self.cell_content(coor) for coor in self.cell_list()])

    def cell_list(self):
        return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]

    def possible_moves(self):
        return [(car.get_name(), movkey, description)
                for car in self.__cars.values()
                for movkey, description in car.possible_moves().items()]

    def target_location(self):
        return (0, 4)

    def cell_content(self, coordinate):
        if coordinate not in self.cell_list():
            raise ValueError("Invalid coordinate")
        for car in self.__cars.values():
            if coordinate in car.car_coordinates():
                return car.get_name()
        return None

    def add_car(self, car):
        for coor in car.car_coordinates():
            if self.cell_content(coor) is not None:
                return False
        self.__cars[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        if name not in self.__cars:
            return False
        car = self.__cars[name]
        for coor in car.movement_requirements(movekey):
            if self.cell_content(coor) is not None:
                return False
        return car.move(movekey)
