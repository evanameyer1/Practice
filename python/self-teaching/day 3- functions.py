# functions

def greeting(name):
    return f'Hello, {name}'

greetingvar = greeting('Paul')

print(greetingvar)

def numsum(x, y):
    return x + y

a = 5
b = 10

numsum(a, b)

def collect ():
    print('Please input two numbers')
    a = int(input("number 1: "))
    b = int(input("number 2: "))
    return a, b

a, b = collect()
print(numsum(a,b))

def multiply(x, y):
    return x * y

a = int(input('num 1: '))
b = int(input('num 2: '))

answer = multiply(a, b)
print(answer)

def search_lst(given_lst, value):
    for item in given_lst:
        if item == value:
            return True
    return False

lst = [1, 2, 3]

search_lst(lst, 2)

search_lst(['a', 'b'], 'c')

def letter_count(string, letter):
    count = 0
    string = string.lower()
    for char in string:
        if char == letter:
            count += 1
    return count

letter_count("Hello my name is Evan!", 'e')

# functions within functions

def letter_count(string, letter):
    count = 0
    string = string.lower()
    for char in string:
        if char == letter:
            count += 1
    return count

def most_common_letter(string):
    max_letter_so_far = string[0]
    max_letter_count = 1
    for letter in string:
        instances_of_letter = letter_count(string, letter)
        if instances_of_letter >= max_letter_count:
            if instances_of_letter > max_letter_count:
                max_letter_so_far = letter
                max_letter_count = instances_of_letter
            else:
                print(f'This is tied for first!')
    return max_letter_so_far, max_letter_count

most_common_letter('I am a data analyst')

def dna_to_rna(string):
    string = string.upper()
    rna = string.replace('T', 'U')
    return rna

dna_to_rna('ACGTAAAACGTGGTGGATTTGACGTGTTTG')

# functions practice

def square(side):
    return(side**2)

square(int(input('What is the length of the side of the square: ')))

def triangle(height, width):
    return(height * width / 2)

triangle(int(input('What is the height of the triangle: ')), int(input('What is the width of the triangle: ')))

def string_count(string):
    return(list(set(list(string))), len(string))

string_count('apple')

def text_to_int(int1, int2):
    int1 = int(int1)
    int2 = int(int2)
    return([int1 + int2, int2 - int2, int1 * int2])

text_to_int('7', '9')

def return_tuple(tuple1):
    tuple_list = []
    for item in tuple1:
        if tuple1.index(item) % 2 == 0:
            tuple_list.append(item)
    reverse_list = tuple1[::-1]
    return(reverse_list, tuple_list)

return_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])

import string
def word_score(word):
    score = 0
    alphabet = string.ascii_lowercase
    for letter in word:
        if letter in alphabet:
            score += alphabet.index(letter) + 1
    return(word, score)

word_score('handsome')