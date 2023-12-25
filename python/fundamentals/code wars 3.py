#boolean to string

def boolean_to_string(b):
    return 'True' if b == True else 'False'

#reverse words

def reverse_words(text):
    return ' '.join([x[::-1] for x in text.split(' ')])

#hastag generator

def generate_hashtag(s):
    outcome = []
    for word in s.split():
        words = []
        count = 0
        for letter in word.lower():
            if count == 0:
                words.append(letter.upper())
                count = 1
            else:
                words.append(letter)
        outcome.append(''.join(words))
    outcome = '#' + ''.join(outcome)
    if len(outcome) == 1 or len(outcome) > 140:
        outcome = False      
    return outcome

#moving zeroes to the end

def move_zeros(lst):
    outcome = []
    zeros = []
    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            outcome.append(i)
    for o in zeros:
        outcome.append(o)
    return outcome

#testing divisibility

def is_divisible(n,x,y):
    return n % x == 0 and n % y ==0

#counting character types in strings

def solve(s):
    upcount = 0
    lowcount = 0
    numcount = 0
    speccount = 0
    for char in s:
        print(char)
        if char in 'QWERTYUIOPLKJHGFDSAMNBVCXZ':
            upcount += 1
        elif char in 'qwertyuioplkjhgfdsazxcvbnm':
            lowcount += 1
        elif char in '1234567890':
            numcount += 1
        else:
            speccount += 1
    return [upcount, lowcount, numcount, speccount]

#hamming distance

def hamming(a,b):
    count = 0
    for i in range(len(b)):
        if b[i] != a[i]:
            count += 1
    return count 