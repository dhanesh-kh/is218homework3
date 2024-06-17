import sys

from app.commands import Command, CommandHandler


class MenuCommand(Command):

    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        self.command_handler.print_available_commands()
