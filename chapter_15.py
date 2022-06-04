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
