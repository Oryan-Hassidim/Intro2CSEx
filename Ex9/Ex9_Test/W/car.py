class Car:
    def __init__(self, name, length, location, orientation):
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        i, j = self.__location
        return [(i, j), (i, j+1)]

    def possible_moves(self):
        return {'r': 'two steps right' }

    def movement_requirements(self, movekey):
        i,j = self.__location
        return [(i, j+2), (i, j+3)] if movekey == 'r' else []

    def move(self, movekey):
        if movekey == 'r':
            self.__location = (self.__location[0], self.__location[1]+2)
            return True
        return False

    def get_name(self):

        return self.__name

    def __repr__(self):
        return f"Car({self.__name}, {self.__length}, {self.__location}, {self.__orientation})"
