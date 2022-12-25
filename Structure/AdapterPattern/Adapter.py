class Animal:  # interface class
    def walk(self):
        pass


class Cat(Animal):
    def walk(self):
        print("cat walking")


class Dog(Animal):
    def walk(self):
        print("dog walking")

def makeWalk(animal: Animal):
    animal.walk()


class Fish:  # fish doesn't have a run method
    def swim(self):
        print("fish swimming")


class FishAdapter(Animal):
    def __init__(self, fish: Fish):
        self.fish = fish

    def walk(self):
        self.fish.swim()


if __name__ == "__main__":
    nemo = Fish()

    adapted_nemo = FishAdapter(nemo)
    makeWalk(adapted_nemo)

    kitty = Cat()
    bingo = Dog()

    makeWalk(kitty)
    makeWalk(bingo)
