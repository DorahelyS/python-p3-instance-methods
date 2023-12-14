#!/usr/bin/env python3
'''
Sure! In simple terms, an instance method is like a set of instructions that belong to a specific object. 
Imagine you have a toy car. The instance methods of the toy car would be actions that the car can do, 
like moving forward, turning, or stopping. Just like that, in programming, instance methods are functions or 
actions that can be performed by an object of a particular class. Each object has its own set of instance methods
that it can use.
'''

class Dog:
    # Class body goes here
#In the Dog class, let's define our bark() instance method:
    #Instance method definition
    def bark(self):
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()
# Woof!
snoopy.sit()

#Note the use of the self keyword in our instance method definition above. We will explore the concept of self in 
#depth in the next module- just know for now that it allows methods to access the other methods and attributes. 
#self is required in instance method definitions, though you don't actually need to pass it in when you call the 
#method.

'''
If you execute this code in the terminal by running python lib/dog.py, you should see "Woof!" written out.

By defining bark() within the Dog class, bark becomes a method of all instances of Dogs. Let's create a second 
instance of Dog, snoopy, and verify that snoopy also knows how to bark by running python lib/dog.py

'''
'''
class Dog:
  def bark(self):
    print("Woof!")

fido = Dog()
fido.bark()
# Woof!

fido.sit()
# AttributeError: 'Dog' object has no attribute 'sit'

In the same manner, instance methods, the methods that belong to particular instances of particular classes, cannot be used globally like procedural methods. They cannot be called without an instance.

class Dog:
  def bark(self):
    print("Woof!")

fido = Dog()
fido.bark()
# Woof!

# Let's try just calling bark without fido
bark()
# NameError: name 'bark' is not defined

'''
