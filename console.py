#!/usr/bin/python3
"""
This script defines a command-line interpreter using the `cmd` module.
The interpreter allows users to interact with it through a command prompt
and execute specific commands.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    is a command-line interpreter class that inherits from `cmd.Cmd`.
    It provides a prompt and specific commands for user interaction.
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''
        Exit from the interpreter.

        Usage: EOF
        '''
        return True

    def do_quit(self, line):
        '''
        Quit from the interpreter.

        Usage: quit
        '''
        return True

    def EmptyLine(self):
        '''
        Called when the user inserts an empty line.
        It does nothing in this case.
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
