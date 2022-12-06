# WPE 2022 B3 Exercise 9: MyMyPy

A very simple version of "mypy", which I call "mymypy". This will not be a static code analyzer. Rather, it'll work at 
runtime, via a decorator.

We can apply the "mymypy" decorator to a function, passing it a list of valid types.  For example:
```python
@mymypy([int, int])
def mul(a,b):
    return a*b
```

This indicates that the first two arguments of "mul" must be integers.  No, there's no way to deal with *args or 
**kwargs. Nor is there a way to say that the arguments might be either ints or floats, or generic sequences.

If I then invoke:
```python
print(mul(3,5))            # works normally, prints 15
```

Nothing unusual happens. But if I invoke:
```python
print(mul([10,20,30],5))   # raises a TypeError, indicating that
                           # the 1st arg must be an int
```

we get a TypeError exception at runtime.
