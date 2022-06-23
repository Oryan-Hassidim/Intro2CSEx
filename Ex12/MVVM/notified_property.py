class NotifiedProperty:
    def __init__(self, value):
        "initializes new notified property with a given value"
        self.__value = value
        self.__observers = []

    def get(self):
        "gets the current value of the property."
        return self.__value

    def set(self, value):
        """
        sets the value of the property.
        if the value changed, notify all observers.
        """
        if self.__value != value:
            self.__value = value
            self.notify_changed()

    def notify_changed(self):
        "notify all observers about change"
        for observer in self.__observers:
            observer()

    def add_observer(self, observer):
        "adds new observer to be notified"
        self.__observers.append(observer)

    def remove_observer(self, observer):
        "remove a given observers from listening the property notifications"
        self.__observers.remove(observer)
