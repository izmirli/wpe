# WPE 2022 B3 Exercise 4: Immutable me

Create a class, ImmutableParent. This class is basically an abstract base class 
(but you don't have to define it explicitly as such); the idea is that other 
classes will inherit from it.  When a class inherits from ImmutableParent, they 
should *not* implement `__init__` on their own.  Instead, `__init__` will take 
**kwargs, and will use the key-value pairs there to set attributes on the object.

Any attempt to change an attribute's value, or to add a new attribute, will 
result in an exception being thrown. For example:

    im = ImmutableMe(x=111,y=222,z=333)
    print(f"Before, vars(im) = {vars(im)}")    # shows x=111, y=222, z=333
    im.x = 999            # exception thrown; cannot change an attribute
    im.a = "Hello"        # exception thrown; cannot add an attribute

Note that if an attribute is itself mutable, then its contents may be changed.

