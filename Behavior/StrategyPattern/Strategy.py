class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("meow")


class Lion(Animal):
    def speak(self):
        print("rar")


def makeSpeak(animal:Animal):
    animal.speak()


def createAnimal(input:str)->Animal:
    if input == "cat":
        return Cat()
    elif input == "lion":
        return Lion()


if __name__ == "__main__":
    animal = createAnimal(input())

    animal.speak()
