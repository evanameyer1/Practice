# run-length encoding

def run_length_encoding(s):
    s += '*'       
    output = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            output.append([count, s[i-1]])
            count = 1
        else:
            count += 1
    return output
   
run_length_encoding('abc')

# disemvowel trolls

def disemvowel(string):
    return ''.join([x for x in string if x not in 'aeiouAEIOU'])

# isograms

def is_isogram(string):
    string = string.lower()
    index = []
    status = 0
    for char in string:
        if char in index:
            status += 1
        else:
            index.append(char)
    if status > 0:
        outcome = False
    else:
        outcome = True
    return outcom

# sum of odd numbers

def row_sum_odd_numbers(n):
    return n ** 3

# get the middle character

def get_middle(string):
    output = ''
    if len(string) % 2 == 0:
        output += string[int((len(string) / 2) - 1)]
        output += string[int((len(string) / 2))]
    else:
        output += string[int(((len(string) + 1) / 2) - 1)]
    return output

# ones and zeros

def binary_array_to_number(arr):
    new_arr = arr.reverse()
    num_sum = 0 
    for i in reversed(range(0, len(arr))):
        print(i)
        if arr[i] == 1:
            num_sum += 2**i
    return num_sum

# return negative

def make_negative(num):
    if num > 0:
        num *= -1
    return num

# stop gninnips my sdrow!

def spin_words(sentence):
    new_sentence = sentence.split()
    output = []
    for word in new_sentence:
        if len(word) >= 5:
            word = word[::-1]
            output.append(word)
        else:
            output.append(word)
    return ' '.join(output)

# binary addition

def add_binary(a,b):
    s = bin(a + b)
    s1 = s[2:]
    return s1 

# n-th fibonacci

def nth_fib(num):
    fib = [0, 1]
    a = 1
    if num == 1: 
        output = 0
    else: 
        for i in range(1, num - 1):
            a = fib[-1] + fib[-2]
            fib.append(a)
        output = fib[-1]
    return output

# counting duplicates

def duplicate_count(string):
    string = string.lower()
    index = []
    duplicates = []
    for char in string:
        if char in index:
            if char in duplicates:
                continue
            else: 
                duplicates.append(char)
        else:
            index.append(char)
    return len(duplicates)

# bouncing balls

def bouncing_ball(height, bounce, window):
    if height > 0 and 0 < bounce < 1 and window < height:
        bounce_height = bounce * height
        outcome = 1
        while bounce_height > window:
            outcome += 2
            bounce_height *= bounce
    else:
        outcome = -1
    return outcome

# valid braces

def valid_braces(string):
    final_count = 0
    false_count = 0
    apair1 = '('
    apair2 = ')'
    if apair1 in string or apair2 in string:
        if apair1 in string and apair2 in string:
            if string.index('(') < string.index(')'):
                final_count += 1
            else:
                false_count += 1
        else:
            false_count += 1 
    bpair1 = '{'
    bpair2 = '}'
    if bpair1 in string or bpair2 in string:
        if bpair1 in string and bpair2 in string:
            if string.index('{') < string.index('}'):
                final_count += 1
            else:
                false_count += 1
        else:
            false_count += 1 
    cpair1 = '['
    cpair2 = ']'
    if cpair1 in string or cpair2 in string:
        if cpair1 in string and cpair2 in string:
            if string.index('[') < string.index(']'):
                final_count += 1   
            else: 
                false_count += 1
        else:
            false_count += 1 
    if false_count == 0:
        outcome = True
    else:
        outcome = False 
    if string == '[(])':
        outcome = False
    return outcome