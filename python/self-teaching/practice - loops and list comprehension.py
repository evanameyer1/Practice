# conditional and loops

x = range(1, 11)
for y in x:
    print(y)

x = range(1, 21, 2)
for y in x:
    print(y)

x = range(1, 21)
for y in x:
    if y % 2 == 0:
        print(y)

x = range(1, 101)
total_sum = 0
for y in x:
    total_sum += y
print(total_sum)

friends = ["Alice", "Bob", "Charlie", "Debbie"]
for item in friends:
    item = item.upper()
    print(f"{item} IS AWESOME!")

friends = ["Alice", "Bob", "Charlie", "Debbie"]
for item in friends:
    vowels = 'aeiou'
    if item[-1].lower() in vowels:
        item = item.upper()
        print(f"{item} IS AWESOME!")
    else:
        item = item.lower()
        print(f"{item} is ok...")

sentence = 'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.'
count = 0
for letter in sentence:
    vowels = 'aeiou'
    if letter in vowels:
        count += 1
print(count)

sentence = 'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.'
sentence_rm = ''
for letter in sentence:
    vowels = 'aeiou'
    if letter not in vowels:
        sentence_rm += letter
print(sentence_rm)

fav_number = 9066
num_range = range(1, fav_number + 1)
divisors = []
divisors_count = 0
for num in num_range:
    if fav_number % num == 0:
        divisors.append(num)
        divisors_count += 1
    
if divisors_count > 2:
    print(f'{fav_number} IS NOT prime, with the following divisors: {divisors}')
else:
    print(f'{fav_number} IS prime!')

def reverse_nums(num):
    num = str(num)
    if num == num[::-1]:
        output = True
    else:
        output = False
    return output

reverse_nums(123456789)
reverse_nums(1234554321)

num_list1 = []
palindromes = []

for num in range(10, 100):
    num_list1.append(num)

for num1 in num_list1:
    for num2 in num_list1[::-1]:
        input_num = num1 * num2
        if reverse_nums(input_num) == True:
            palindromes.append(int(input_num))

print(max(palindromes))

# list comprehension

num_list = [x for x in range(1, 11)]
print(num_list)

square_list = [x**2 for x in range(1, 11)]
print(square_list)

even_list = [x for x in range(18, 48) if x % 2 == 0]
print(even_list)

even_squares_list = [x*x for x in range(1, 21) if x % 2 == 0]
print(even_squares_list)

sum_cubes = [sum(x**3 for x in range(7, 38))]
print(sum_cubes)

divisible = [x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0]
print(divisible)

friends = ['Alice', 'Bob', 'Charlie', 'Derek']
friends = [friend.upper() for friend in friends]
print(friends)

new_friends = [friend for friend in friends if friend[-1] in 'aeiouAEIOU']
print(new_friends)

new_sentence = ''.join([letter for letter in 'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.' if letter not in 'aeiouAEIOU']) 
print(new_sentence)

january_csvs = [f'Jan {x}.xlsx' for x in range(1, 32)]
print(january_csvs)

euros = [4.50, 6.70, 3.25, 9.99, 12.75, 0.35]
dollars = [f'${float("{:.2f}".format(x * 1.1))}' for x in euros]
print(dollars)

viable_heights = [x for x in [71, 48, 55, 65, 68, 60, 58, 53] if x >= 60]
print(viable_heights)

lower_heights = [x if x >= 60 else 'None' for x in [71, 48, 55, 65, 68, 60, 58, 53]]
print(lower_heights)

people = {
    'Aaron': 58,
    'Barbara': 66,
    'Clarence': 62,
    'Donovan': 55,
    'Erika': 70,
    'Fernando': 72
}

people = [key for key in people if people[key] > 59]
print(people)

people = {
    'Aaron': [87, 52, 78],
    'Barbara': [92, 79, 85],
    'Clarence': [42, 68, 55],
    'Donovan': [95, 100, 87],
    'Erika': [62, 88, 47],
    'Fernando': [84, 99, 0]
}

final_grades = [f'{key} {max(people[key])}' for key in people]
print(final_grades)

final_grades_dict = {key:max(people[key]) for key in people}
print(final_grades_dict)

#[('A', 'Z'), ('B', 'Y'), ('C', 'X'), ('D', 'W'), ('E', 'V')]

letters_a = ['A', 'B', 'C', 'D', 'E']
letters_z = ['Z', 'Y', 'X', 'W', 'V']

#long-hand to better understand step-by-step
biglist = list(zip(letters_a, letters_z))

fl = []
for index in biglist:  
    tl = ''
    for char in index:
        tl += char 
    fl.append(tl)
print(fl)

#list comprehension version
biglist = [''.join([x,y]) for x,y in zip(letters_a, letters_z)]
print(biglist)

letters_a = ['A', 'B', 'C', 'D', 'E']
letters_a_list = [f'{x} is letter {y} of the alphabet' for y, x in enumerate(letters_a, 1)]
print(letters_a_list)

import math

math.sin(math.pi / 2)

math.log(math.sqrt(math.e))

math.e**math.factorial(3)

from math import ceil
from math import floor

ceil(3.8)
ceil(3.2)
floor(3.8)
floor(3.2)

