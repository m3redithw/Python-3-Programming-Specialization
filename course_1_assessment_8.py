# q1. Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

# yes

# q2. Could aliasing cause potential confusion in this problem?
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

# no

# q3. Which of these is a correct reference diagram following the execution of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

# A. 1.

# q4. Which of these is a correct reference diagram following the execution of the following code?
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']

# D. 4.
# Yes, the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first version makes a new object entirely and reassigns to obj. The second version changes the original object so that the contents of object_two are added to the end of the first.

# q5. Which of these is a correct reference diagram following the execution of the following code?
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)

# A. 1.
# Yes, when we make our own diagrams we want to keep the old information because sometimes other variables depend on them. It can get cluttered though if there is a lot of information.
