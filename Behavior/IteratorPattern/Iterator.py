class Iterator:
    def nextVal(self):
        pass

    def hasNext(self):
        pass


class ArrayIterator(Iterator):
    def __init__(self, arrayContainer):
        self.container = arrayContainer.container
        self.pos = -1

    def hasNext(self):
        if self.pos < len(self.container) - 1:
            return True
        else:
            return False

    def nextVal(self):
        if self.hasNext():
            self.pos += 1
            return self.container[self.pos]


class ArryContainer:
    def __init__(self):
        self.container = []

    def add(self, num: int):
        self.container.append(num)

    def getIterator(self):
        return ArrayIterator(self)


def printByIter(iter):
    while iter.hasNext():
        print(iter.nextVal(), end=' ')
    print(' ')


if __name__ == "__main__":
    array_container = ArryContainer()
    array_container.add(1)
    array_container.add(3)
    array_container.add(5)
    iterator = array_container.getIterator()

    printByIter(iterator)