"""Command-line calculator.

Use "cmd" to build a program that implements a simple calculator.
Calculator's inputs will only be positive integers, anything else will be disregard.
"""
import cmd
from functools import reduce

ops = {
    '+': {'cmd': 'add', 'name': 'add', 'func': lambda a, b: a + b},
    '-': {'cmd': 'sub', 'name': 'subtract', 'func': lambda a, b: a - b},
    '*': {'cmd': 'mul', 'name': 'multiply', 'func': lambda a, b: a * b},
    '/': {'cmd': 'div', 'name': 'divide', 'func': lambda a, b: a / b},
}


class Menu(cmd.Cmd):
    """A Command-line-menu calculator."""
    intro = 'Welcome to the command-line calculator.  Type help or ? to list commands.\n'
    prompt = '[Calc] '

    def precmd(self, line: str) -> str:
        """Normalize calc actions that start with valis simbols."""
        op, sep, rest = line.partition(' ')
        if op in ops:
            return f"{ops[op]['cmd']}{sep}{rest}"

        return line

    def do_add(self, args):
        """Add valid arguments."""
        return self.calc(args, ops['+']['func'], ops['+']['name'])

    def do_sub(self, args):
        """Subtract valid arguments."""
        return self.calc(args, ops['-']['func'], ops['-']['name'])

    def do_mul(self, args):
        """Multiply valid arguments."""
        return self.calc(args, ops['*']['func'], ops['*']['name'])

    def do_div(self, args):
        """Divide valid arguments."""
        return self.calc(args, ops['/']['func'], ops['/']['name'])

    def do_quit(self, args):
        """Quit calculator."""
        return self.do_EOF(args)

    @staticmethod
    def calc(args, func, op_name):
        """General purpose calc function.

        Valid Arguments are positive integers. Anything else will be disregard.

        :param args: arguments string
        :param func: operation function (for two arguments)
        :param op_name: common name for operation
        :return: None
        """
        valid_args = [int(a) for a in args.split() if a.isdigit()]
        if not valid_args:
            print(f"Nothing to {op_name}")
            return None

        print(reduce(func, valid_args))

    @staticmethod
    def do_EOF(args):
        """Quit calculator."""
        print('Quiting calculator.')
        return True


if __name__ == '__main__':
    Menu().cmdloop()
