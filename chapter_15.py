# What will the following code print?
def f(x = 0, y = 1):
    return x * y

print(f())
# 0

# What will the following code print?
def f(x = 0, y = 1):
    return x * y

print(f(1))
# 1

# Keyword parameters with .format
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

# use the .format method to insert the same value into a string multiple times
# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

# anonymous functions with lambda expressions

#  This unnamed object behaves just like the function object constructed below.
# lambda arguments: expression

# def fname(arguments):
# #     return expression
def f(x):
    return x - 1

print(f) # <function f>
print(type(f)) # <class 'function'>
print(f(3)) # 2

print(lambda x: x-2) # <function <lambda>>
print(type(lambda x: x-2)) # <class 'function'>
print((lambda x: x-2)(6)) # 4