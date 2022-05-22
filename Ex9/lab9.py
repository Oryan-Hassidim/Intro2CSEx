class CarDriver:
    def __init__(self, skill):
        self.__skill = float(skill)

    def get_skill(self):
        return self.__skill


class Car:
    def __init__(self, spped):
        self.__speed = spped
        self.__driver = None

    def set_driver(self, driver):
        self.__driver = driver

    def get_driving_speed(self):
        return (self.__speed * self.__driver.get_skill()) if self.__driver else 1.0


class RaceTrack:
    def __init__(self, overall):
        self.__overall = overall
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)

    def race(self):
        return max([car.get_driving_speed() for car in self.__cars]) / self.__overall


class Student:
    def __init__(self, name, grades) -> None:
        self.__name = name
        self.__grades = grades

    def get_grade_avg(self):
        return sum(self.__grades) / len(self.__grades)
    
    def get_name(self):
        return self.__name

class ClassRoom:
    def __init__(self, students):
        self.__students = students

    def __str__(self):
        return repr([(s.get_name(),s.get_grade_avg()) for s in self.__students])

    def __repr__(self):
        return str(self)
