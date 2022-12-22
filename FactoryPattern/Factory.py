class Animal():
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("야옹")


class Dog(Animal):
    def speak(self):
        print("멍")


def Factory(animal:str) -> Animal:
    if animal == "Cat":
        return Cat()
    elif animal == "Dog":
        return Dog()


if __name__ == "__main__":
    cat = Factory("Cat")
    cat.speak()

    dog = Factory("Dog")
    dog.speak()