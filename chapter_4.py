#!/usr/bin/env python
# coding: utf-8

# ## 4.2. Modules
# A **module** is a file containing Python definitions and statements intended for use in other Python programs. There are many Python modules that come with Python as part of the standard library. Providing additional functionality through modules allows you to only use the functionality you need when you need it, and it keeps your code cleaner.
# 
# Functions imported as part of a module live in their own **namespace**. A namespace is simply a space within which all names are distinct from each other. The same name can be reused in different namespaces but two objects can’t have the same name within a single namespace. One example of a namespace is the set of street names within a single city. Many cities have a street called “Main Street”, but it’s very confusing if two streets in the same city have that name! Another example is the folder organization of file systems. You can have a file called todo in your work folder as well as your personal folder, but you know which is which because of the folder it’s in; each folder has its own namespace for files. Note that human names are not part of a namespace that enforces uniqueness; that’s why governments have invented unique identifiers to assign to people, like passport numbers.

# ## 4.2.1 Importing Modules
# In order to use Python modules, you have to **import** them into a Python program. That happens with an import statement: the word import, and then the name of the module. The name is case-sensitive. Roughly translated to English, an import statement says “there’s some code in another file; please make its functions and variables available in this file.” More technically, an import statement causes all the code in another file to be executed. Any variables that are bound during that execution (including functions that are defined) may then be referred in some way (to be discussed) in the current file.
# 
# By convention, all import commands are put at the very top of your file. They can be put elsewhere, but that can lead to some confusions, so it’s best to follow the convention.
# 
# Where do these other files that you can import come from? It could be a code file that you wrote yourself, or it could be code that someone else wrote and you copied on to your computer.
# 
# For example, if you have a file myprog.py in directory ~/Desktop/mycode/, and myprog.py contains a line of code import morecode, then the python interpreter will look for a file called morecode.py, excecute its code, and make its object bindings available for reference in the rest of the code in myprog.py.
# 
# Note that it is import morecode, not import morecode.py, but the other file has to be called morecode.py.
# 
# The tests you see in your problem sets are also using a Python module that’s in the standard library, called unittest. Right now, you can’t see the code that causes those tests to run, because we have hidden it from you, but later in the course, you will learn how to write your own Unit Tests for code, and to do so, you will need to write an import statement at the beginning of your programs. Even before you learn how to write your own tests, you will see code for Unit Tests in your problem set files.

# ## 4.2.2. Syntax for Importing Modules and Functionality
# When you see imported modules in a Python program, there are a few variations that have slightly different consequences.
# 
# 1. The most common is import morecode. That imports everything in morecode.py. To invoke a function f1 that is defined in morecode.py, you would write morecode.f1(). Note that you have to explicitly mention morecode again, to specify that you want the f1 function from the morecode namespace. If you just write f1(), python will look for an f1 that was defined in the current file, rather than in morecode.py.
# 
# 2. You can also give the imported module an alias (a different name, just for when you use it in your program). For example, after executing import morecode as mc, you would invoke f1 as mc.f1(). You have now given the morecode module the alias mc. Programmers often do this to make code easier to type.
# 
# 3. A third possibility for importing occurs when you only want to import SOME of the functionality from a module, and you want to make those objects be part of the current module’s namespace. For example, you could write from morecode import f1. Then you could invoke f1 without referencing morecode again: f1().

# ## 4.3. The random module
# We often want to use random numbers in programs. Here are a few typical uses:
# 
# - To play a game of chance where the computer needs to throw some dice, pick a number, or flip a coin,
# 
# - To shuffle a deck of playing cards randomly,
# 
# - To randomly allow a new enemy spaceship to appear and shoot at you,
# 
# - To simulate possible rainfall when we make a computerized model for estimating the environmental impact of building a dam,
# 
# - For encrypting your banking session on the Internet.
# 
# Python provides a module random that helps with tasks like this. You can take a look at it in the documentation. Here are the key things we can do with it.

# In[1]:


import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)


# It is important to note that random number generators are based on a **deterministic algorithm** — repeatable and predictable. So they’re called **pseudo-random** generators — they are not genuinely random. They start with a seed value. Each time you ask for another random number, you’ll get one based on the current seed attribute, and the state of the seed (which is one of the attributes of the generator) will be updated. The good news is that each time you run your program, the seed value is likely to be different meaning that even though the random numbers are being created algorithmically, you will likely get random behavior each time you execute.

# ## 4.4. Glossary
# ### deterministic
# A process that is repeatable and predictable.
# 
# ### documentation
# A place where you can go to get detailed information about aspects of your programming language.
# 
# ### module
# A file containing Python definitions and statements intended for use in other Python programs. The contents of a module are made available to the other program by using the import statement.
# 
# ### namespace
# A naming system for making names unique, to avoid duplication and confusion. Within a namespace, no two names can be the same.
# 
# ### pseudo-random number
# A number that is not genuinely random but is instead created algorithmically.
# 
# ### random number
# A number that is generated in such a way as to exhibit statistical randomness.
# 
# ### random number generator
# A function that will provide you with random numbers, usually between 0 and 1.
# 
# ### standard library
# A collection of modules that are part of the normal installation of Python.
