# WPE 2022 B3 Exercise 14: Single dispatch

Given "mysum" function:
```python
def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total
```

Use "singledispatch" to create functionality that extends "mysum" as described here:

    - if we get a string, then we should turn each character into an
      integer. We'll ignore non-integers, but will turn integers into
      numbers and add them.

    - if we get a dict, then we should iterate over the values, adding
      them together. If there's a non-number among the values, then
      the function can raise a TypeError.

    - In all other cases, then we should iterate over the argument and
      add the numbers.  If there's a non-number, then the function can
      raise a TypeError exception.

Just to be clear: You should *not* be using "if" to choose! 
Rather, you should let the single-dispatch system choose from among the functions for you.
