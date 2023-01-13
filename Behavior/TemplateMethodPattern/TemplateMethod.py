class BasicRamenRecipe:
    def cookRamen(self):
        self.boilWater()
        self.addRamen()
        self.addons()
        self.wait()

    def boilWater(self):
        print("boil 550ml of water")

    def addRamen(self):
        print("add noodles, soup Base, flakes")

    def addons(self):
        pass

    def wait(self):
        print("cook for 4min 30s")


class NocopeRecipe(BasicRamenRecipe):
    def addons(self):
        print("add onions")


class GrandmaRecipe(BasicRamenRecipe):
    def boilWater(self):
        print("boil 1000ml of water")

    def wait(self):
        print("cook for 10m")


if __name__ == "__main__":
    basicRecipe = BasicRamenRecipe()
    basicRecipe.cookRamen()

    nocopeRecipe = NocopeRecipe()
    nocopeRecipe.cookRamen()

    granmaRecipe = GrandmaRecipe()
    granmaRecipe.cookRamen()