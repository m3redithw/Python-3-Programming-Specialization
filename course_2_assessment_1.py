# q1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
fileref = open('travel_plans.txt','r')
content = fileref.read()
num = 0
for char in content:
    num +=1
print(num)

# 316

# q2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
fileref = open('emotion_words.txt', 'r')
content = fileref.read()
words = content.split()
num_words = 0
for n in words:
    num_words += 1
print(num_words)

# 48

# q3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.
fileref = open('school_prompt.txt', 'r')
lines = fileref.readlines()
num_lines = 0
for l in lines:
    num_lines += 1

# 10

# q4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = open('school_prompt.txt', 'r')
content = fileref.read()
beginning_chars = ''
for i in range(0,30):
    beginning_chars += content[i]
print(beginning_chars)

# Writing essays for school can 

# q5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
fileref = open('school_prompt.txt', 'r')
lines = fileref.readlines()
three = []
for l in lines:
    s = l.split()
    three.append(s[2])
print(three)

# ['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,']

# q6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
fileref = open('emotion_words.txt', 'r')
lines = fileref.readlines()
emotions = []
for l in lines:
    s = l.split()
    emotions.append(s[0])
print(emotions)

# ['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous']

# q7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
fileref = open('travel_plans.txt', 'r')
content = fileref.read()
first_chars = ''
for char in range(0,33):
    first_chars += content[char]
print(first_chars)

# This summer I will be travelling.

# q8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
fileref = open('school_prompt.txt', 'r')
content = fileref.readlines()
p_words = []
for lines in content:
    l = lines.split()
    for word in l:
        if 'p' in word:
            p_words.append(word)
print(p_words)

# ['topic', 'point', 'papers,', 'ups,', 'scripts.']