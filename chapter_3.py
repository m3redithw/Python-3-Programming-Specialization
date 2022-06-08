#!/usr/bin/env python
# coding: utf-8

# ## 3.1. Introduction to Debugging
# “The art of debugging is figuring out what you really told your program to do rather than what you thought you told it to do.”  — Andrew Singer

# ## 3.3. Debugging
# Programming errors are called **bugs** and the process of tracking them down and correcting them is called **debugging**. 
# 
# One of the most important skills you need to acquire to complete this book successfully is the ability to debug your programs. Debugging might be the most under-appreciated, and under-taught, skill in introductory computer science. For that reason we are introducing a series of “debugging interludes.” Debugging is a skill that you need to master over time, and some of the tips and tricks are specific to different aspects of Python programming. So look for additional Way of the Programmer interludes throughout the rest of this book.
# 
# Programming is an odd thing in a way. Here is why. As programmers we spend 99% of our time trying to get our program to work. We struggle, we stress, we spend hours deep in frustration trying to get our program to execute correctly. Then when we do get it going we celebrate, hand it in, and move on to the next homework assignment or programming task. But here is the secret, when you are successful, you are happy, your brain releases a bit of chemical that makes you feel good. You need to organize your programming so that you have lots of little successess. It turns out your brain doesn’t care all that much if you have successfully written hello world, or a fast fourier transform (trust me its hard) you still get that little release that makes you happy. When you are happy you want to go on and solve the next little problem. Essentially I’m telling you once again, start small, get something small working, and then add to it.
# 
# 

# ## 3.3.1. How to Avoid Debugging
# It is **largely avoidsable** if you work carefully.
# 
# 1. **Understand the Problem** You must have a firm grasp on what you are trying to accomplish but not necessarily how to do it. You do not need to understand the entire problem. But you must understand at least a portion of it and what the program should do in a specific circumstance – what output should be produced for some given input. This will allow you to test your progress. You can then identify if a solution is correct or whether there remains work to do or bugs to fix. This is probably the single biggest piece of advice for programmers at every level.
# 
# 2. **Start Small** It is tempting to sit down and crank out an entire program at once. But, when the program – inevitably – does not work, you have a myriad of options for things that might be wrong. Where to start? Where to look first? How to figure out what went wrong? I’ll get to that in the next section. So, start with something really small. Maybe just two lines and then make sure that runs. Hitting the run button is quick and easy. It gives you immediate feedback about whether what you have just done works or not. Another immediate benefit of having something small working is that you have something to turn in. Turning in a small, incomplete program, is almost always better than nothing.
# 
# 3. **Keep Improving It**  Once you have a small part of your program working, the next step is to figure out something small to add to it – how can you move closer to a correct solution. As you add to your program, you gain greater insight into the underlying problem you are trying to solve. If you keep adding small pieces of the program one at a time, it is much easier to figure out what went wrong. (This of course means you must be able to recognize if there is an error. And that is done through testing.) As long as you always test each new bit of code, it is most likely that any error is in the new code you have just added. Less new code means its easier to figure out where the problem is.

# ## 3.4. Tips for Debugging
# Debugging a program is a different way of thinking than writing a program. The process of debugging is much more like being a detective. Here are a few rules to get you thinking about debugging.
# 
# 1. Everyone is a suspect (Except Python)! It’s common for beginner programmers to blame Python, but that should be your last resort. Remember that Python has been used to solve CS1 level problems millions of times by millions of other programmers. So, Python is probably not the problem.
# 
# 2. Check your assumptions. At this point in your career you are still developing your mental model of how Python does its work. Its natural to think that your code is correct, but with debugging you need to make your code the primary suspect. Even if you think it is right, you should verify that it really is by liberally using print statements to verify that the values of variables really are what you think they should be. You’ll be surprised how often they are not.
# 
# 3. Find clues. This is the biggest job of the detective and right now there are two important kinds of clues for you to understand.
# - Error Messages
# 
# - Print Statements
# 
# Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic errors. It is useful to distinguish between them in order to track them down more quickly.

# ## 3.5. Syntax Errors
# Python can only execute a program if the program is syntactically correct; otherwise, the process fails and returns an error message. **Syntax** refers to the structure of a program and the rules about that structure.

# In Python, rules of syntax include requirements like these: strings must be enclosed in quotes; statements must generally be written one per line; the print statement must enclose the value to be displayed in parenthesis; expressions must be correctly formed. The following lines contain syntax errors:

# In[2]:


print(Hello, world!)
print "Hello, world!"
print(5 + )


# ## 3.6. Runtime Errors
# The second type of error is a **runtime error**. A program with a runtime error is one that passed the interpreter’s syntax checks, and started to execute. However, during the execution of one of the statements in the program, an error occurred that caused the interpreter to stop executing the program and display an error message. Runtime errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened.
# 
# Here are some examples of common runtime errors you are sure to encounter:
# 
# - Misspelled or incorrectly capitalized variable and function names
# 
# - Attempts to perform operations (such as math operations) on data of the wrong type (ex. attempting to subtract two variables that hold string values)
# 
# - Dividing by zero
# 
# - Attempts to use a type conversion function such as int on a value that can’t be converted to an int

# Notice the following important differences between syntax errors and runtime errors that can help you as you try to diagnose and repair the problem:
# 
# - If the error message mentions SyntaxError, you know that the problem has to do with syntax: the structure of the code, the punctuation, etc.
# 
# - If the program runs partway and then crashes, you know the problem is a runtime error. Programs with syntax errors don’t execute even one line.

# ## 3.7. Semantic Errors
# The third type of error is the **semantic error**, also called a **logic error**. If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, your program will not do the right thing. It will do something else. Specifically, it will do what you **told** it to do, not what you **wanted** it to do.
# 
# The following program has a semantic error. Execute it to see what goes wrong:

# In[3]:


num1 = input('Enter a number:')
num2 = input('Enter another number:')
sum = num1 + num2

print('The sum of', num1, 'and', num2, 'is', sum)


# This program runs and produces a result. However, the result is not what the programmer intended. It contains a semantic error. The error is that the program performs concatenation instead of addition, because the programmer failed to write the code necessary to convert the inputs to integers.

# ## 3.7.1. Test Cases
# 
# ### Test Case
# A **test case** is a set of input values for the program, together with the output that you expect the program should produce when it is run with those particular inputs.
# 
# Here is an example of a test case for the program above:

# In[4]:


Test Case
---------
Input: 2, 3
Expected Output: 5

