# WPE 2022 B3 Exercise 3: tar to zip

This week, we'll write a function that takes one or more filenames, each of 
which is assumed to be a tarfile (with or without compression). For each 
filename, the function will create a new zipfile with the same contents, but 
(obviously) in ".zip" format rather than in ".tar.gz" format.

Python comes with two modules, 
"[zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile)" 
and "[tarfile](https://docs.python.org/3/library/tarfile.html)", that should 
help you with that. Note that the "tarfile" module knows how to deal with 
various types of compression automatically, which is pretty impressive and amazing.

For example, if I write:
    tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')

I'm going to expect that in the current directory, we'll then have three files: 
"foo.zip", "bar.zip", and "baz.zip", each of which will contain the same 
contents as the respective tarfiles, but in zip format, instead.

If you get a file that cannot be untar'ed for whatever reason, then print an 
error or warning message, but continue.

You can also pass a value to the "zippath" parameter, indicating where you want
the zipfile to be created.

I'll assume for the purposes of this exercise that it's OK to untar the 
contents of the tarfile in the current directory, although if you can do it in
a temporary directory (e.g., '/tmp/'), all the better.
