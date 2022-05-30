# q1. Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"
for i in my_str:
    print(i)

# q2. Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(i)
for i in several_things:
    print(type(i))

# q3. Write code that uses iteration to print out the length of each element of the list stored in str_list.

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in str_list:
    print(len(i))

# q4. Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

acum = 0
for i in original_str:
    acum += 1
num_chars = acum

# q5. addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"
lst = addition_str.split('+')
new_lst = [int(i) for i in lst]
sum_val = sum(new_lst)

# q6. week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
temp_list = week_temps_f.split(',')
lst=[float(i) for i in temp_list]
avg_temp = sum(lst)/len(lst)

# q7. Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.

nums = []
for i in range(0,68):
    nums.append(i)

# q8. Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
p = original_str.split()
for i in p:
    yo = len(i)
    num_words_list.append(yo)
print(num_words_list)

# q9. Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").

lett = ""

for i in range(7):
    
    lett = lett + "b"

# q10. Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

import turtle
wn = turtle.Screen()
mujju = turtle.Turtle()
mujju.shape("turtle")
d = 100
a = 30
mujju.speed(0)

for i in range(12):
        
        mujju.forward(d)
        mujju.stamp()
        mujju.backward(d)
        mujju.right(a)