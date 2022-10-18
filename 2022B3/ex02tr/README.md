# WPE 2022 B3 Exercise 2: tr

Unix contains all sorts of great little utilities. Some of these utilities, I've found, are excellent examples of things
we can do easily in Python.

This week, we'll look at the "tr" utility that Unix provides. In its most basic form, "tr" allows us to translate from
one set of characters to another. For example, if I want every occurrency of "z" in a file to be turned into an "s",
then I can do the following:

    $ echo 'the quick brown fox jumps over the lazy dog' | tr z s
    the quick brown fox jumps over the lasy dog

Notice that "tr" expects to get its input from stdin.  We can modify more than one letter; "tr" only works on individual
letters, so we can do the following: 

    $ echo 'the quick brown fox jumps over the lazy dog' | tr sz zs
    the quick brown fox jumpz over the lasy dog

This turns every occurrence of 'z' into an 's', and vice versa.  Note that this also shows that the translation occurs
once per letter.

The same letter can appear in the destination mulitple times: 

    $ echo 'the quick brown fox jumps over the lazy dog' | tr aeiou yyyyy
    thy qyyck brywn fyx jymps yvyr thy lyzy dyg

This translates every lowercase vowel (a, e, i, o, or u) into a "y" character.

If the destination string (i.e., the second one) is shorter than the source, then the final letter in the destination covers the rest.  For example: 

    $ echo 'the quick brown fox jumps over the lazy dog' | tr aeiou xy
    thy qyyck brywn fyx jymps yvyr thy lxzy dyg

Or: 

    $ echo 'the quick brown fox jumps over the lazy dog' | tr aeiou xyz
    thy qzzck brzwn fzx jzmps zvyr thy lxzy dzg

For this week's exercise, I want you to implement "tr" as a function that takes two strings, and returns a function that performs the translation on a string. In other words, we should be able to do the following: 

    vowels_to_y = tr('aeiou', 'y')
    print(vowels_to_y('the quick brown fox jumps over the lazy dog'))

and we should see: 

    thy qyyck brywn fyx jymps yvyr thy lxzy dyg

Note that we're not going to try to do the more complex parts of "tr", such as ranges of characters, complements, and the like. And of course, it's unfair to use the "str.translate" method for this to work!
