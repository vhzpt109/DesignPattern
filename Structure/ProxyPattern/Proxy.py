class Animal:  # interface class
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("meow")


class CatProxy(Animal):
    def __init__(self, cat: Cat):
        self.cat = cat

    def speak(self):
        print("before speak")
        self.cat.speak()
        print("after speak")


def doSpeak(animal: Animal):
    animal.speak()


if __name__ == "__main__":
    kitty = Cat()
    kitty_proxy = CatProxy(kitty)
    doSpeak(kitty_proxy)
