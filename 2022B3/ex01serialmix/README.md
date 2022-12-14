# WPE 2022 B3 Exercise 1: Serial Mix

Define a class, Serializable, that defines two methods, "dump" and "load". If 
a class inherits from our Serializable class, then you can invoke "dump" and 
"load" on objects of that type, and it'll know how to use the "pickle" module 
from the standard Python library to save itself to disk, and load itself from 
disk. A filename needs to be passed to "dump" and "load", so that the methods 
know with which file to work.

I should thus be able to do the following:
```python
class Book(Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b = Book("Python Workout", "Reuven Lerner", 39)
b.dump('book.data')      # book is now stored on disk, in pickle format

b2 = Book('blah title, 'blah author', 100)
b2.load('book.data')     # title, author, and price now reflect disk file
```

The thing is, maybe we don't want to store the book info in "pickle" format. 
Maybe we want to use CSV, or JSON, or XML. I want you to define a class for 
each of these formats, so that I can do the following:
```python
class Book(CSVMixin, Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b = Book("Python Workout", "Reuven Lerner", 39)
b.dump('book.csv')      # book is now stored on disk, in CSV format

b2 = Book('blah title', 'blah author', 100)
b2.load('book.csv')     # title, author, and price now reflect disk file
```

You'll similarly create JSONMixin and XMLMixin.
