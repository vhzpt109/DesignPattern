class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("meow", end='')


class Dog(Animal):
    def speak(self):
        print("bark", end='')


def makeSpeak(animal: Animal):
    animal.speak()
    print(" ")


class Decorator(Animal):
    def __init__(self, animal: Animal):
        self.animal = animal

    def speak(self):
        self.animal.speak()


class WithSmile(Decorator):
    def speak(self):
        self.animal.speak()
        print("😀", end='')


class WithHeartEyes(Decorator):
    def speak(self):
        self.animal.speak()
        print("😍", end='')


if __name__ == "__main__":
    kitty = Cat()
    makeSpeak(kitty)
    kitty_smile = WithSmile(kitty)
    makeSpeak(kitty_smile)
    kitty_smile_heart = WithHeartEyes(kitty_smile)
    makeSpeak(kitty_smile_heart)

    dog = Dog()
    makeSpeak(dog)
    dog_heart = WithHeartEyes(dog)
    makeSpeak(dog_heart)
    dog_heart_smile = WithSmile(dog_heart)
    makeSpeak(dog_heart_smile)