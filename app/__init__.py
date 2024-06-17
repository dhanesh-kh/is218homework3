from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
    
    def start(self):
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        print("Type 'exit' to exit.")
        while True: 
            self.command_handler.execute_command(input(">>> ").strip())