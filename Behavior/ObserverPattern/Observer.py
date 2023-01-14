class Observer:
    def update(self):
        pass


class Cat(Observer):
    def update(self):
        print('meow')


class Dog(Observer):
    def update(self):
        print('bark')


class Owner:
    def __init__(self):
        self.animals = []

    def register(self, animal: Observer):
        self.animals.append(animal)

    def notify(self):
        for animal in self.animals:
            animal.update()


if __name__ == "__main__":
    owner = Owner()
    cat = Cat()
    dog = Dog()

    owner.register(cat)
    owner.register(dog)

    owner.notify()