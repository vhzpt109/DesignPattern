class AnimalVisitor:
    def catVisit(self, elem):
        pass

    def dogVisit(self, elem):
        pass


class SpeakVisitor(AnimalVisitor):
    def catVisit(self, elem):
        print("meow~")

    def dogVisit(self, elem):
        print("bark!")


class NameVisitor(AnimalVisitor):
    def catVisit(self, elem):
        print(f"cat, {elem.name}")

    def dogVisit(self, elem):
        print(f"dog, {elem.name}")


class Animal:
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: AnimalVisitor):
        pass


class Cat(Animal):
    def accept(self, visitor: AnimalVisitor):
        visitor.catVisit(self)


class Dog(Animal):
    def accept(self, visitor: AnimalVisitor):
        visitor.dogVisit(self)


if __name__ == "__main__":
    baduk = Dog('baduk')
    kitty = Cat('kitty')

    baduk.accept(NameVisitor())
    kitty.accept(NameVisitor())

    baduk.accept(SpeakVisitor())
    kitty.accept(SpeakVisitor())
