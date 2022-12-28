class TrafficLight:
    def __init__(self):
        self.state = 'green'

    # prefer enum
    def setState(self, state: str):
        self.state = state

    def speak(self):
        if self.state == 'green':
            print('green light')
        elif self.state == 'red':
            print('red light')

    def wait(self):
        print('wait.. the light changed')
        if self.state == 'green':
            self.state = 'red'
        elif self.state == 'red':
            self.state = 'green'


if __name__ == "__main__":
    t_light = TrafficLight()
    t_light.speak()
    t_light.wait()
    t_light.speak()