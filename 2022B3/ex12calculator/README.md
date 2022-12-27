# WPE 2022 B3 Exercise 12: Command-line calculator

Use "cmd" to build a program that implements a simple calculator.  
Calculator's inputs will only be positive integers; negative numbers and floats can be thrown out.
Upon running the program, the user will be presented with a command prompt. The possible commands are: 

    add
    sub
    mul
    div

But it's not enough to enter a command. You'll enter a command, followed by one or more integers separated by spaces. 
Thus, if you write: 

    add 1 2 3

the system will print "6" on the screen. 
And if you write: 

    sub 10 5 3

the system will print "2" on the screen.

Anything that isn't a positive integer can be ignored. Thus: 

    add 1 abc 2.3 -4 2 3

will also print "6" on the screen.

Be able to enter calculations not only as words, but also as symbols. Examples: 

    + 1 2 3
    - 10 5 3
    * 1 2 3
    / 10 4

Using the symbols will be equivalent to using the words.

You can exit from the calculator either by entering EOF or a "quit" command.
