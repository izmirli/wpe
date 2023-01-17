# WPE 2022 B3 Exercise 15: The end

 Create a TempFile class.  This class will work just like a regular file object, except that when the object is 
 garbage collected, the file associated with it is erased.  For example, I can say:

    f = TempFile('myfile.txt', 'w')
    f.write('abc\n')
    f.close()

The above code will work just like a regular file-like object.
The difference is that when there are no more references to our file -- for example, if we delete the "f" variable:

    del(f)   # remove the only reference to our file

At this point, I'd like the file on disk to be removed.  In this way, the file really is temporary.  
However, it goes away not when the file is closed, but rather via the garbage collector.

Note that all of the regular method calls on a file should work on this object.

I'd also like you to make our TempFile object work as a context manager. This will make it easier (and more natural) 
for us to work with such objects:

    with TempFile('myfile2.txt', 'w') as f:
        f.write('defg\n')
        f.write('hijk\n')
