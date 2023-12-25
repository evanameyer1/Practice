# functions/list comprehension

def area_triangle(base, height):
    return base * height / 2
area_triangle(5, 4)

import math
from math import pi

def area_circle(radius):
    return math.pi*radius**2
area_circle(10)

def sum_n(max_num):
    return sum([x for x in range(1, max_num+1)])
sum_n(15)

def sum_squares(max_num):
    return sum([x**2 for x in range(1, max_num+1)])
sum_squares(15)

def to_dollar(num):
    return num*1.1
to_dollar(10)

def to_dollar_list(num_list):
    return [round(num*1.1) for num in num_list] 
to_dollar_list([1, 10, 100])

def is_tall(num):
    return ["Tall enough" if num > 60 else "Too short"]      
is_tall(72)

def is_tall_list(num_list):
    return ["Tall enough" if x > 60 else "Too short" for x in num_list]
is_tall_list([58, 70, 60])

def letter_grade(grade):
    return "FDCBA"[max(0, (grade - 50) // 10)]
letter_grade(65)

def letter_grade(num_list):
    return [("FDCBA"[max(0, (grade - 50) // 10)]) for x in num_list]
letter_grades([85, 62, 90])

def vowel_count(string):
    return sum([[c].count(c) for c in string if c in 'aeiouAEIOU'])
vowel_count('General Assembly')

def toggle_case(string):
    return ''.join([c.upper() if c not in 'aeiouAEIOU' else c.lower() for c in string])
toggle_case('General Assembly')

def disemvowel(string):
    return ''.join([c for c in string if c not in 'aeiouAEIOU' ])
disemvowel('Python is my favorite language')

def smart_disemvowel(string):
    return ' '.join([word if len(word) == 1 else ''.join([c for c in word if c not in 'aeiouAEIOU' ]) for word in string.split()])
smart_disemvowel('I love Python programming')

def word_reverser(string):
    return ' '.join(reversed(string.split()))
word_reverser('Data science is cool')

def letter_reverser(string):
    return ' '.join([char[::-1] for char in string.split()])
letter_reverser('Data science is cool')

def to_leet_speak(string):
    return ''.join([{'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3',
            'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!', 'J' : 'J',
             'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0',
             'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : '$', 'T' : '7',
             'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y',
             'Z' : '2'}.get(char.upper()) if char != ' ' else ' ' for word in string for char in word])
to_leet_speak('i am elite')

def is_prime(num):
    return all([num % i != 0 for i in range(2, num)])
is_prime(15)

def sum_primes(num):
    index = []
    for i in range(2, num + 1):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            index.append(i)
    return sum(set(index))

sum_primes(15)

def sum_primes(num):
    return sum(i for i in range(2, num + 1) if all(i % x != 0 for x in range(2, i)))
sum_primes(15)

# bonus questions

def permissions_to_octa(string):
    sum_sum = []
    outcome = []
    count = 0
    num_sum = []
    for char in string:
        if char == 'r':
            num_sum.append(4)
            count += 1
        elif char == 'w':
            num_sum.append(2)
            count += 1
        elif char == 'x':
            num_sum.append(1)
            count += 1
        else:
            num_sum.append(0)
            count += 1
        if count == 3:
            sum_sum.append(num_sum)
            num_sum = []
            count = 0
    for num in sum_sum:
        outcome.append(sum(num))
    return int("".join([str(i) for i in outcome]))

permissions_to_octa("rwxr-xr-x")

def min_bags(items, lbags, sbags):
    bag_count = 0
    l_bag_count = 5 * lbags    
    items -= l_bag_count
    bag_count += lbags
    if items > sbags:
        bag_count = -1
    else:
        while items > 0:
            bag_count += 1
            items -= 1     
    return bag_count

print(min_bags(16, 2, 10))
print(min_bags(20, 2, 2))