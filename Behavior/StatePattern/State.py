class TrafficLight:
    def __init__(self):
        self.state = GreenLight()

    def setState(self, state):
        self.state = state

    def speak(self):
        self.state.speak()

    def change(self):
        self.state.change(self)


class StateInterface:
    def speak(self):
        pass

    def change(self, traffit_light: TrafficLight):
        pass


class GreenLight(StateInterface):
    def speak(self):
        print("green light")

    def change(self, traffit_light: TrafficLight):
        print("change state")
        traffit_light.setState(RedLight())


class RedLight(StateInterface):
    def speak(self):
        print("red light")

    def change(self, traffit_light: TrafficLight):
        print("change state")
        traffit_light.setState(GreenLight())


if __name__ == "__main__":
    t_light = TrafficLight()
    t_light.speak()

    t_light.change()

    t_light.speak()