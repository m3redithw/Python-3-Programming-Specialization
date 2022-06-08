# Map

def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

# the map function, that makes it more clear what the overall structure of the computation is. map takes two arguments, a function and a sequence.
# the map function produces an “iterator”, which is like a list but produces the items as they are needed.
# map actually returns a real list, but to make this code compatible with a full python environment, we always convert it to a list.

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

# once we get used to using the map function, it’s no longer necessary to define functions like tripleStuff and quadrupleStuff.

things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line

print(list(map((lambda value: 5*value), [1, 2, 3])))

# Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def f(str):
    return str.upper()

abbrevs_upper = list(map(f, abbrevs))

# ---------------------------------------------------------------------
# Filter
# the filter function. filter takes two arguments, a function and a sequence. The function takes one item and return True if the item should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.

def keep_evens(nums):
    new_seq = filter(lambda num: num%2==0, nums)
    return list(new_seq)
print(keep_evens([3, 4, 6, 7, 0, 1]))

# Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: 'o' in word,lst)

print(lst2)

# ---------------------------------------------------------------------
# Zip

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)

# The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on.

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))
print(L4)