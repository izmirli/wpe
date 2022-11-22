# WPE 2022 B3 Exercise 7: Socket file functions

When the server program starts up, it looks in the current directory for files whose names look like "server_func*.py". 
Each such file contains one or more Python function definitions.

The server program should iterate over each of these files, turning each of the files' function definitions into 
a key-value pair in our "actions" dictionary. Then, when the client's request comes in, the names of the functions 
will be defined by whatever files were available at server startup time.

For example, the current directory might contain the following files: 

    # filename: server_func_numbers.py
    def numbers():
        return list(range(10))

    # filename: server_func_others.py
    def reverse_word(word):
        return word[::-1]

    def unicode_map(word):
        return { letter : ord(letter) for letter in word }

If these two files are located in the current directory, then the server will (as in the previous exercise) respond to 
three different actions: "numbers", "reverse_word", and "unicode_map".  Notice that we can have one or more function 
definitions in each file.

A hint: You're going to need to use the "exec" function for this exercise.  And indeed, while "exec" is often a 
dangerous thing to do in a Python program, this exercise is designed to demonstrate when it can be useful, and how you 
can tame it a bit.
