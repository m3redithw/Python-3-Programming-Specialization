#!/usr/bin/env python
# coding: utf-8

# ## 2.2. Values and Data Types
# A **value** is one of the fundamental things — like a word or a number — that a program manipulates. Some values are 5 (the result when we add 2 + 3), and "Hello, World!". These objects are classified into different classes, or data types: 4 is an integer, and “Hello, World!” is a string, so-called because it contains a string or sequence of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.
# 
# We can specify values directly in the programs we write. For example we can specify a number as a **literal** just by (literally) typing it directly into the program (e.g., 5 or 4.32). In a program, we specify a word, or more generally a string of characters, by enclosing the characters inside quotation marks (e.g., "Hello, World!").
# 
# During execution of a program, the Python interpreter creates an internal representation of literals that are specified in a program. It can then manipulate them, for example by multiplying two numbers. We call the internal representations **objects** or just **values**.
# 
# You can’t directly see the internal representations of values. You can, however, use the print function to see a printed representation in the output window.
# 
# The printed representation of a number uses the familiar decimal representation (reading Roman Numerals is a fun challenge in museums, but thank goodness the Python interpreter doesn’t present the number 2014 as MMXIV in the output window). Thus, the printed representation of a number shown in the output window is the same as the literal that you specify in a program.
# 
# The printed representation of a character string, however, is not exactly the same as the literal used to specify the string in a program. For the literal in a program, you enclose the string in quotation marks. The printed representation, in the output window, omits the quotation marks.
# 
# Numbers with a decimal point belong to a class called **float**, because these numbers are represented in a format called floating-point. At this stage, you can treat the words class and type interchangeably. We’ll come back to a deeper understanding of what a class is in later chapters.

# ## 2.3. Operators and Operands
# **Operators** are special tokens that represent computations like addition, multiplication and division.
# The values the operator works on are called **operands**.
# 

# In[ ]:


20 + 32
5 ** 2
(5 + 9) * (15 - 7)


# The tokens +, -, and *, and the use of parentheses for grouping, mean in Python what they mean in mathematics. The asterisk (*) is the token for multiplication, and ** is the token for exponentiation.

# In Python 3, which we will be using, the division operator / produces a floating point result (even if the result is an integer; 4/2 is 2.0). If you want truncated division, which ignores the remainder, you can use the // operator (for example, 5//2 is 2).

# In[1]:


print(9 / 5)
print(5 / 9)
print(9 // 5)


# The **modulus operator**, sometimes also called the **remainder operator** or **integer remainder operator** works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax is the same as for other operators.

# In[2]:


print(7 // 3)    # This is the integer division operator
print(7 % 3)     # This is the remainder or modulus operator


# The modulus operator turns out to be surprisingly useful. For example, you can check whether one number is divisible by another—if x % y is zero, then x is divisible by y. Also, you can extract the right-most digit or digits from a number. For example, x % 10 yields the right-most digit of x (in base 10). Similarly x % 100 yields the last two digits.

# ## 2.11. Order of Operations
# When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence. Python follows the same precedence rules for its mathematical operators that mathematics does.

# In[3]:


print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!


# ## 2.4. Function Calls
# The Python interpreter can compute new values with function calls. You are familiar with the idea of functions from high school algebra. There you might define a function f by specifying how it transforms an input into an output, f(x) = 3x + 2. Then, you might write f(5) and expect to get the value 17.
# 
# Python adopts a similar syntax for invoking functions. If there is a named function foo that takes a single input, we can invoke foo on the value 5 by writing foo(5).
# 
# There are many built-in functions available in Python. You’ll be seeing some in this chapter and the next couple of chapters.
# 
# Functions are like factories that take in some material, do some operation, and then send out the resulting object.
# 
# Icon that represents a function. Appears simliar to a factory with three places on top for inputs to come in and a place on the bottom for the output/return value to come out.
# In this case, we refer to the materials as arguments or inputs and the resulting object is referred to as output or return value. This process of taking input, doing something, and then sending back the output is demonstrated in the gif below.

# ## 2.5. Data Types
# If you are not sure what class (data type) a value falls into, Python has a function called type which can tell you.

# In[5]:


print(type("Hello, World!"))
print(type(17))
print("Hello, World")
print(type(3.2))


# In[6]:


print(type("17"))
print(type("3.2"))


# In[7]:


print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))


# In[8]:


print(42500)
print(42,500)


# In[10]:


print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)


# ## 2.6. Type conversion functions
# The functions int, float and str will (attempt to) convert their arguments into types int, float and str respectively. We call these **type conversion** functions.
# 
# The **int** function can take a floating point number or a string, and turn it into an int. For floating point numbers, it discards the decimal portion of the number - a process we call truncation towards zero on the number line. Let us see this in action:

# In[12]:


print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
print(int("23"))


# The type converter **float** can turn an integer, a float, or a syntactically legal string into a float.

# In[13]:


print(float("123.45"))
print(type(float("123.45")))


# The type converter **str** turns its argument into a string. Remember that when we print a string, the quotes are removed in the output window. However, if we print the type, we can see that it is definitely **str**.

# In[14]:


print(str(17))
print(str(123.45))
print(type(str(123.45)))


# ## 2.7. Variables
# One of the most powerful features of a programming language is the ability to manipulate **variables**. A variable is a name that refers to a value.
# 
# **Assignment Statements** create new variables and also give them values to refer to.
# 

# In[17]:


message = "What's up, Doc?"
n = 17
pi = 3.14159


# This example makes three assignments. The first assigns the string value "What's up, Doc?" to a new variable named message. The second assigns the integer 17 to n, and the third assigns the floating-point number 3.14159 to a variable called pi.
# 
# The **assignment token**, =, should not be confused with equality (we will see later that equality uses the == token). The assignment statement links a name, on the left hand side of the operator, with a value, on the right hand side. This is why you will get an error if you enter:
# 

# In[18]:


17 = n


# ## 2.8. Variable Names and Keywords
# **Variable names** can be arbitrarily long. They can contain both letters and digits, but they have to begin with a letter or an underscore. Although it is legal to use uppercase letters, by convention we don’t. If you do, remember that case matters. Bruce and bruce are different variables.
# 
# **Caution** Variable names can never contain spaces.
# 
# The underscore character ( _) can also appear in a name. It is often used in names with multiple words, such as my_name or price_of_tea_in_china. There are some situations in which names beginning with an underscore have special meaning, so a safe rule for beginners is to start all names with a letter.
# 
# If you give a variable an illegal name, you get a syntax error. In the example below, each of the variable names is illegal.

# In[19]:


76trombones = "big parade"
more$ = 1000000
class = "Computer Science 101"

# 76trombones is illegal because it does not begin with a letter.
# more$ is illegal because it contains an illegal character, the dollar sign.


# It turns out that class is one of the Python **keywords**. Keywords define the language’s syntax rules and structure, and they cannot be used as variable names. Python has thirty-something keywords (and every now and again improvements to Python introduce or eliminate one or two):

# and | as | assert | break | class | continue
# 
# def | del | elif | else | except | exac
# 
# finally | for | from | global | if | import
# 
# in | is | lambda | nonlocal | not | or
# 
# pass | raise | return | try | while | with
# 
# yield | True | False | None

# ## 2.9. Choosing the Right Variable Name
# Programmers generally choose names for their variables that are meaningful to the human readers of the program — they help the programmer document, or remember, what the variable is used for. Beginning programmers sometimes think it is funny to use strange or obscene names for their variables. This is not good practice and will not amuse your professor. Get in the habit of using meaningful names right away.

# ## 2.10. Statements and Expressinos
# A **statement** is an instruction that the Python interpreter can execute. You have only seen the assignment statement so far. Some other kinds of statements that you’ll see in future chapters are while statements, for statements, if statements, and import statements. (There are other kinds too!)
# 
# An **expression** is a combination of literals, variable names, operators, and calls to functions. Expressions need to be evaluated. The result of evaluating an expression is a value or object.
# 

# If you ask Python to *print* an **expression**, the interpreter **evaluates** the expression and displays the result.

# In[20]:


print(1 + 1 + (2 * 3))
print(len("hello"))


# In this example len is a built-in Python function that returns the number of characters in a string.
# 
# The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements. A literal all by itself is a simple expression, and so is a variable.

# In[21]:


y = 3.14
x = len("hello")
print(x)
print(y)


# In a program, anywhere that a literal value (a string or a number) is acceptable, a more complicated expression is also acceptable. Here are all the kinds of expressions we’ve seen so far:
# 
# - literal
#     e.g., “Hello” or 3.14
# 
# - variable name
#     e.g., x or len
# 
# - operator expression
# <expression> operator-name <expression>
# 
# - function call expressions
# <expression>(<expressions separated by commas>)

# Notice that operator expressions (like + and *) have sub-expressions before and after the operator. Each of these can themselves be simple or complex expressions. In that way, you can build up to having pretty complicated expressions.

# In[ ]:


print(2 * len("hello") + len("goodbye"))


# ## 2.12. Reassignment
# As we have mentioned previously, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

# In[ ]:


bruce = 5
print(bruce)
bruce = 7
print(bruce)


# The first time bruce is printed, its value is 5, and the second time, its value is 7. The assignment statement changes the value (the object) that bruce refers to.

# It is important to note that in mathematics, a statement of equality is always true. If a is equal to b now, then a will always equal to b. In Python, an assignment statement can make two variables refer to the same object and therefore have the same value. They appear to be equal. However, because of the possibility of reassignment, they don’t have to stay that way:

# In[ ]:


a = 5
b = a    # after executing this line, a and b are now equal
print(a,b)
a = 3    # after executing this line, a and b are no longer equal
print(a,b)


#    ## 2.13. Updating Variable
#    One of the most common forms of reassignment is an **update** where the new value of the variable depends on the old. For example,
# 
# 

# In[1]:


x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)


# Before you can update a variable, you have to **initialize** it, usually with a simple assignment. In the above example, x was initialized to 6.
# Updating a variable by adding something to it is called an **increment**; subtracting is called a **decrement**. Sometimes programmers talk about incrementing or decrementing without specifying by how much; when they do they usually mean by 1. Sometimes programmers also talk about **bumping** a variable, which means the same as incrementing it by 1.

# ## 2.14. Hard Coding

#  **“Don’t hard code”** basically means, you should rely on your code, your logic, your program, and you should not write things out by hand or do computation in your head – even if you can do so easily.
#  
#  Try as much as you can not to rely on your brilliant but fallible human brain to do computation when you program – use your brain to determine how to write the correct code to solve the problem for you!

# ## 2.15 Input
# Our programs get more interesting if they don’t do exactly the same thing every time they run. One way to make them more interesting is to get input from the user. Luckily, in Python there is a built-in function to accomplish this task. It is called **input**.
# 
# 

# In[ ]:


n = input("Please enter your name: ")


# The input function allows the programmer to provide a **prompt string**.
# 
# It is very important to note that the input function returns a string value. Even if you asked the user to enter their age, you would get back a string like "17". It would be your job, as the programmer, to convert that string into an int or a float, using the int or float converter functions we saw earlier.

# ## 2.16. Glossary
# 
# ### assignment statement
# 
# A statement that assigns a value to a name (variable). To the left of the assignment operator, =, is a name. To the right of the assignment token is an expression which is evaluated by the Python interpreter and then assigned to the name. The difference between the left and right hand sides of the assignment statement is often confusing to new programmers. In the following assignment:
# 
# n = n + 1
# n plays a very different role on each side of the =. On the right it is a value and makes up part of the expression which will be evaluated by the Python interpreter before assigning it to the name on the left.
# 
# ### assignment token
# 
# = is Python’s assignment token, which should not be confused with the mathematical comparison operator using the same symbol.
# 
# ### boolean expression
# An expression that is either true or false.
# 
# ### boolean value
# There are exactly two boolean values: True and False. Boolean values result when a boolean expression is evaluated by the Python interepreter. They have type bool.
# 
# ### class
# see data type below
# 
# ### comment
# Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.
# 
# ### data type
# A set of values. The type of a value determines how it can be used in expressions. So far, the types you have seen are integers (int), floating-point numbers (float), and strings (str).
# 
# ### decrement
# Decrease by 1.
# 
# ### evaluate
# To simplify an expression by performing the operations in order to yield a single value.
# 
# ### expression
# A combination of operators and operands (variables and values) that represents a single result value. Expressions are evaluated to give that result.
# 
# ### float
# A Python data type which stores floating-point numbers. Floating-point numbers are stored internally in two parts: a base and an exponent. When printed in the standard format, they look like decimal numbers. Beware of rounding errors when you use floats, and remember that they are only approximate values.
# 
# ### increment
# Both as a noun and as a verb, increment means to increase by 1.
# 
# ### initialization (of a variable)
# To initialize a variable is to give it an initial value. Since in Python variables don’t exist until they are assigned values, they are initialized when they are created. In other programming languages this is not the case, and variables can be created without being initialized, in which case they have either default or garbage values.
# 
# ### int
# A Python data type that holds positive and negative whole numbers.
# 
# ### integer division
# An operation that divides one integer by another and yields an integer. Integer division yields only the whole number of times that the numerator is divisible by the denominator and discards any remainder.
# 
# ### keyword
# A reserved word that is used by the compiler to parse program; you cannot use keywords like if, def, and while as variable names.
# 
# ### literal
# A number or string that is written directly in a program. Sometimes these are also referred to as literal values, or just values, but be careful not to confuse a literal value as written in a program with an internal value maintained by the Python interpreter during execution of a program.
# 
# ### logical operator
# One of the operators that combines boolean expressions: and, or, and not.
# 
# ### modulus operator
# An operator, denoted with a percent sign ( %), that works on integers and yields the remainder when one number is divided by another.
# 
# ### object
# Also known as a data object (or data value). The fundamental things that programs are designed to manipulate (or that programmers ask to do things for them).
# 
# ### operand
# One of the values on which an operator operates.
# 
# ### operator
# A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
# 
# ### prompt string
# Used during interactive input to provide the use with hints as to what type of value to enter.
# 
# ### reference diagram
# A picture showing a variable with an arrow pointing to the value (object) that the variable refers to. See also state snapshot.
# 
# ### rules of precedence
# The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.
# 
# ### state snapshot
# A graphical representation of a set of variables and the values to which they refer, taken at a particular instant during the program’s execution.
# 
# ### statement
# An instruction that the Python interpreter can execute. So far we have only seen the assignment statement, but we will soon meet the import statement and the for statement.
# 
# ### str
# A Python data type that holds a string of characters.
# 
# ### type conversion function
# A function that can convert a data value from one type to another.
# 
# ### value
# A number or string (or other things to be named later) that can be stored in a variable or computed in an expression.
# 
# ### variable
# A name that refers to a value.
# 
# ### variable name
# A name given to a variable. Variable names in Python consist of a sequence of letters (a..z, A..Z, or _) and digits (0..9) that begins with a letter. In best programming practice, variable names should be chosen so that they describe their use in the program, making the program self documenting.
