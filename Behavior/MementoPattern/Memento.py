import uuid
from datetime import datetime


class CatMemento:
    def __init__(self, age, height):
        self.uuid = uuid.uuid4()
        self.created_time = datetime.now()
        self.age = age
        self.height = height


class Cat:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def speak(self):
        print(f'{self.age}year old, {self.height}cm, meow')

    def createMemento(self):
        cat_memento = CatMemento(self.age, self.height)
        return cat_memento

    def restore(self, memento):
        self.age = memento.age
        self.height = memento.height


if __name__ == "__main__":
    cat_history = []

    cat = Cat(0, 10)
    cat_history.append(cat.createMemento())

    cat.age = 1
    cat.height = 25

    cat_history.append(cat.createMemento())

    cat.age = 2
    cat.height = 50

    cat_history.append(cat.createMemento())

    cat.speak()
    cat.restore(cat_history[0])

    cat.speak()