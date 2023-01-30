class Mediator:
    def notify(sender):
        pass


class Clock:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator

    def Alarm(self):
        print("alarm on")
        self.mediator.notify('AlarmOn')


class Light:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator

    def On(self):
        print("light On")

    def Off(self):
        print("light off")
        self.mediator.notify('LightOff')


class Speaker:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator

    def On(self):
        print("speaker on")

    def Off(self):
        print("speaker off")


class HomeMediator(Mediator):
    def __init__(self, clock, light, speaker):
        self.clock = clock
        self.light = light
        self.speaker = speaker

    def notify(self, signal: str):
        if signal == 'AlarmOn':
            self.speaker.On()
            self.light.On()

        elif signal == 'LightOff':
            self.speaker.Off()


if __name__ == "__main__":
    clock = Clock()
    light = Light()
    speaker = Speaker()

    mediator = HomeMediator(clock, light, speaker)

    clock.setMediator(mediator)
    light.setMediator(mediator)
    speaker.setMediator(mediator)

    clock.Alarm()

    light.Off()