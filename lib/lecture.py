'''
Key Vocab
Class: a bundle of data and functionality. Can be copied and modified to accomplish a wide variety of 
programming tasks.
Initialize: create a working copy of a class using its __init__() method.
Instance: one specific working copy of a class. It is created when a class's __init__() method is called.
Object: the more common name for an instance. The two can usually be used interchangeably.
Function: a series of steps that create, transform, and move data.
Method: a function that is defined inside of a class.
Attribute: variables that belong to an object.

Introduction
We know that classes are a collection of data and functionality that act as a factory for our objects. 
We create those objects by calling our class just as we would a function, with closed parentheses:

class Dog:
    pass

fido = Dog()
# <__main__.Dog object at 0x1027f07f0>

But what can this instance of a dog stored in the local variable fido do? In fact, how do we even ask this 
object to do something?

The Behavior of Objects
Objects on their own don't do very much. In order to see the behavior of an object, we need to interact 
with it to elicit a response. There are certain strategies for interacting with objects that allow us to 
access their data and functionality from the outside.

Dot Notation
We send objects messages asking them to perform an operation or task through a syntax known as "Dot Notation".

class Dog:
    pass

fido = Dog()
# <__main__.Dog object at 0x1027f07f0>

fido.__dir__()
# ['__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__',
# '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__',
# '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__',
# '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__',
# '__format__', '__sizeof__', '__dir__', '__class__']

When we interact with an object through dot notation, we are calling the variable or function that is defined 
inside of the object. We call these instance variables attributes and these instance functions methods. 
Unless otherwise specified, all of an object's methods are considered instance methods. Instance methods 
can access and modify the attributes of an instance.

In the example above, we access the fido instance's __dir__() method by separating the object, fido and the 
method, __dir__() by a dot (.).

The __dir__() method provides you with a list of the object's methods and attributes. You'll notice that even 
though we didn't provide the Dog class with any attributes or methods, it has many by default!

How do we add our own methods to our classes? In our Dog example, can we teach our Dog a new trick? Can we 
teach our Dog to bark for example?

We can. We're used to defining functions already with the def keyword. If we place this function definition within
the body of a class, that function becomes a specific behavior of instances of that class, not a generic procedure 
we can just call whenever we want.



