class Visitor:
    def visit(self, elem):
        pass


class NameVisitor(Visitor):
    def visit(self, elem):
        print(elem.name)


class AgeVisitor(Visitor):
    def visit(self, elem):
        print(elem.age)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("meow")

    def accept(self, visitor: Visitor):
        print("use implementation of visitor")
        visitor.visit(self)


if __name__ == "__main__":
    kitty = Cat("kitty", 3)
    kitty.speak()

    name_visitor = NameVisitor()
    kitty.accept(name_visitor)

    age_visitor = AgeVisitor()
    kitty.accept(age_visitor)