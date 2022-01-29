#>>>>>>>>>>Command<<<<<<<<<<<
"The Command Pattern Concept"
from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The command interface, that all commands will implement"
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"

class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

class Receiver:
    "The Receiver"

    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print("Executing Command 1")

    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print("Executing Command 2")

class Command1(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()

# The CLient
# Create a receiver
RECEIVER = Receiver()

# Create Commands
COMMAND1 = Command1(RECEIVER)
COMMAND2 = Command2(RECEIVER)

# Register the commands with the invoker
INVOKER = Invoker()
INVOKER.register("1", COMMAND1)
INVOKER.register("2", COMMAND2)

# Execute the commands that are registered on the Invoker
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")

#>>>>>>>>>Mediator<<<<<<<<<<<<<

class Mediator():
    "The Mediator Concrete Class"

    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()

    def colleague1_method(self):
        "Calls the method provided by Colleague1"
        return self.colleague1.method_1()

    def colleague2_method(self):
        "Calls the method provided by Colleague2"
        return self.colleague2.method_2()

class Colleague1():
    "This Colleague provides data for Colleague2"

    @staticmethod
    def method_1():
        "A simple method"
        return "Here is the Colleague1 specific data you asked for"

class Colleague2():
    "This Colleague provides data for Colleague1"

    @staticmethod
    def method_2():
        "A simple method"
        return "Here is the Colleague2 specific data you asked for"

# The Client
MEDIATOR = Mediator()

# Colleague1 wants some data from Colleague2
DATA = MEDIATOR.colleague2_method()
print(f"COLLEAGUE1 <--> {DATA}")

# Colleague2 wants some data from Colleague1
DATA = MEDIATOR.colleague1_method()
print(f"COLLEAGUE2 <--> {DATA}")


#>>>>>>>>>>>>>> Strategy <<<<<<<<<<<


class Context():
    "This is the object whose behavior will change"
    @staticmethod
    def request(strategy):
        """The request is handled by the class passed in"""
        return strategy()
class IStrategy(metaclass=ABCMeta):
    "A strategy Interface"
    @staticmethod
    @abstractmethod
    def __str__():
        "Implement the __str__ dunder"
class ConcreteStrategyA(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyA"
class ConcreteStrategyB(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyB"
class ConcreteStrategyC(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyC"
# The Client
CONTEXT = Context()
print(CONTEXT.request(ConcreteStrategyA))
print(CONTEXT.request(ConcreteStrategyB))
print(CONTEXT.request(ConcreteStrategyC))