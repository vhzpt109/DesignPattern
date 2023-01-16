import copy


class Cat:
    def __init__(self):
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None

    def clone(self):
        return copy.deepcopy(self)


class BlackCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = 'black'


class WhiteCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = 'white'


if __name__ == "__main__":
    black_cat = BlackCat()
    black_cat.nose_color = 'pink'
    black_cat.tail_color = 'green'

    kitty = black_cat.clone()
    kitty.eye_color = 'white'
    kitty.name = 'kitty'

    nabi = black_cat.clone()
    nabi.eye_color = 'blue'
    nabi.name = 'nabi'