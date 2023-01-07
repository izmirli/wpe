# WPE 2022 B3 Exercise 13: Threadify

Write the "threadify" function.  We'll pass this function several arguments:
* the function that should be invoked 
* a list of tuples, with each tuple representing one set of arguments for the function

The idea is that the function will be invoked, inside of a new thread, for each tuple in the list, and will get the 
contents of the tuple as arguments. When all of the threads have finished executing, "threadify" will return all of 
the results as a list.

Thus, if I have a function "add" that takes two arguments, and returns those two arguments added together, I could call:

    result = threadify(add, [(2,2), (3,3), (4,4)])

Inside of "threadify", we'll create three threads, invoking the "add" function once in each of the threads. 
The results will be returned as the list, [4, 6, 8].

Since we don't know the order in which the threads will finish their actions, it's possible that the output will be in 
a different order each time. Use a PriorityQueue, which will ensure that when you remove items from the queue, it's in 
a specified order.
