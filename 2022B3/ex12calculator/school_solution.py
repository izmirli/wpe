#!/usr/bin/env python3

import cmd
import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}


class Menu(cmd.Cmd):
    def line_to_int_list(self, line):
        return [int(x)
                for x in line.split()
                if x.isdigit()]

    def precmd(self, line):
        parts = line.split()
        print(f"parts = '{parts}'")

        if parts[0] in ops:
            print(f"Found {parts[0]}")
            parts[0] = ops[parts[0]].__name__
            return ' '.join(parts)
        else:
            return line

    def meta(self, line, which_operator):
        numbers = self.line_to_int_list(line)
        if not numbers:
            print(f"Nothing to {ops[which_operator]}")
        else:
            total = numbers[0]
            for one_number in numbers[1:]:
                total = ops[which_operator](total, one_number)
            print(total)

    def do_add(self, line):
        return self.meta(line, '+')

    def do_mul(self, line):
        return self.meta(line, '*')

    def do_sub(self, line):
        return self.meta(line, '-')

    def do_truediv(self, line):
        return self.meta(line, '/')

    do_div = do_truediv

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Menu().cmdloop()
