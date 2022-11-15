# WPE 2022 B3 Exercise 6: Socket pickle

On the server, you'll again have a number of functions defined, and a dict seems like the best place to store them. 
But instead of the user sending commands which correspond to functions, the user will name the function that should 
be invoked. The response from the server will be the function's actual output, which can be any built-in data type 
or combination thereof. That output will be pickle'd, and the pickle output (a string) will then be sent to the client.  The client will then un-pickle the response from the server, displaying not just the string version of the object but also its type (for easier debugging).

Note that the server-side functions won't take any arguments. 

For example, let's assume that the server has a function "numbers", which returns a list of integers from 0-9.
If the client says 

    numbers

Then the server will invoke the "numbers" function, pickle the list of integers, and send the list of integers to the client.  The client will un-pickle them, and then display: 

    [0,1,2,3,4,5,6,7,8,9]
    <class 'list'>

This will, once again, continue until the client hangs up with the "bye" command.
