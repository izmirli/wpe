"""Command-line calculator.

Use "cmd" to build a program that implements a simple calculator.

"""
import cmd


class Menu(cmd.Cmd):
    intro = 'Welcome to the command-line calculator.  Type help or ? to list commands.\n'
    prompt = ' '

    def do_add(self):
        pass


if __name__ == '__main__':
    Menu().cmdloop()
