class Command:
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, print_str:str):
        self.print_str = print_str

    def execute(self):
        print(self.print_str)

class Dog:
    def sit(self):
        print("sit")

    def stay(self):
        print("stay")


class DogCommand(Command):
    def __init__(self, dog: Dog, commands):
        self.dog = dog
        self.commands = commands

    def execute(self):
        for command in self.commands:
            if command == "sit":
                self.dog.sit()
            elif command == "stay":
                self.dog.stay()


class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command: Command):
        self.command_list.append(command)

    def runCommands(self):
        for command in self.command_list:
            command.execute()


if __name__ == "__main__":
    first_command = PrintCommand("first command")
    second_command = PrintCommand("second command")

    first_command.execute()
    second_command.execute()

    baduk = Dog()
    dog_command = DogCommand(baduk, ["stay", "sit"])

    invoker = Invoker()
    invoker.addCommand(first_command)
    invoker.addCommand(dog_command)
    invoker.addCommand(second_command)
    invoker.runCommands()
