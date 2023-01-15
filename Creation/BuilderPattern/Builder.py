class Cat:
    def __init__(self, height, weight, color):  # could be more props such as type,and more...
        self.height = height
        self.weight = weight
        self.color = color

    def print(self):
        return print(f"{self.height}cm,{self.weight}kg,{self.color}")


class CatBuilder:
    def __init__(self):
        self.height = None
        self.weight = None
        self.color = None

    def setHeight(self, height):
        self.height = height
        return self

    def setWeight(self, weight):
        self.weight = weight
        return self

    def setColor(self, color):
        self.color = color
        return self

    def build(self):
        cat = Cat(self.height, self.weight, self.color)
        # building a cat can be very complex
        return cat


class WhiteCatBuilder(CatBuilder):
    def __init__(self):
        super().__init__()
        self.color = "white"


class BlackCatBuilder(CatBuilder):
    def __init__(self):
        super().__init__()
        self.color = "black"


# Director is not mandatory
class Director:
    def setSmallCat(self, builder: CatBuilder):
        builder.setWeight(5)
        builder.setHeight(5)

    def setBigCat(self, builder: CatBuilder):
        builder.setWeight(100)
        builder.setHeight(100)


if __name__ == "__main__":
    cat_builder = CatBuilder()
    cat_builder.setHeight(30)
    cat_builder.setWeight(7)
    cat_builder.setColor("black")
    cat = cat_builder.build()
    cat.print()

    cat = CatBuilder().setHeight(20).setWeight(19).setColor("green").build()
    cat.print()

    white_cat = WhiteCatBuilder().setHeight(10).setWeight(10).build()
    white_cat.print()
    black_cat = BlackCatBuilder().setHeight(20).setWeight(20).build()
    black_cat.print()

    director = Director()
    black_cat_builder = BlackCatBuilder()
    director.setBigCat(black_cat_builder)
    cat = black_cat_builder.build()
    cat.print()