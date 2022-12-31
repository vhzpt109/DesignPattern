class Button:
    def click(self):
        pass


class DarkButton(Button):
    def click(self):
        print("dark click")


class LightButton(Button):
    def click(self):
        print("light click")


class CheckBox:
    def check(self):
        pass


class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")


class LightCheckBox(CheckBox):
    def check(self):
        print("light check")


class ScrollBar:
  def scroll(self):
    pass

class DarkScrollBar(ScrollBar):
  def scroll(self):
    print("dark scroll")

class LightScrollBar(ScrollBar):
  def scroll(self):
    print("light scroll")


class UIFactory:
    def getButton(self):
        pass

    def getCheckBox(self):
        pass

    def getScrollBar(self):
        pass


class DarkUIFactory(UIFactory):
    def getButton(self):
        return DarkButton()

    def getCheckBox(self):
        return DarkCheckBox()

    def getScrollBar(self):
        return DarkScrollBar()


class LightUIFactory(UIFactory):
    def getButton(self):
        return LightButton()

    def getCheckBox(self):
        return LightCheckBox()

    def getScrollBar(self):
        return LightScrollBar()


if __name__ == "__main__":
