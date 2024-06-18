from app.commands import Command


class MenuCommand(Command):
    
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        print("Loaded commands:")
        for plugin_name, commands in self.command_handler.commands.items():
            if isinstance(commands, list):
                for command in commands:
                    print(f"- {plugin_name}")
            else:
                print(f"- {plugin_name}")
