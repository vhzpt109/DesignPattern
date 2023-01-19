# implementor
class Power:
    def powerUp(self):
        pass

    def powerDown(self):
        pass


class Engine(Power):
    def powerUp(self):
        print('engine power up')

    def powerDown(self):
        print('engine power down')


class Motor(Power):
    def powerUp(self):
        print('motor power up')

    def powerDown(self):
        print('motor power down')


# abstaction car
class Car:
    def __init__(self, power: Power):
        self.power = power

    def drive(self):
        self.power.powerUp()

    def stop(self):
        self.power.powerDown()


class Sedan(Car):
    def sedanOnlyFn(self):
        print('sedan only')


if __name__ == "__main__":
    sedan = Sedan(Motor())
    sedan.drive()
    sedan.stop()
    sedan.sedanOnlyFn()
