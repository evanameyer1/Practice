# duplicate encoder

def duplicate_encode(word):
    word = word.lower()
    index = []
    for char in word:
        if char in word[word.index(char) + 1:]:
            index.append(')')
        else:
            index.append('(')
    return ''.join(index)

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# number of occurrences

def number_of_occurrences(element, sample):
    count = 0
    for num in sample:
        if num == element:
            count += 1
    return count

# even or odd

def even_or_odd(number):
    if number % 2 == 0:
        outcome = 'Even'
    else:
        outcome = 'Odd'
    return outcome

# return to sanity

def mystery():
    results = {'sanity': 'Hello'}
    return results

# distance between points in 2D

import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(self, Point):
        dist = math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return dist

# pair zeros

def pair_zeros(arr):
    output = []
    zero_count = 0
    for num in arr:
        if num == 0 and zero_count == 0:
            output.append(num)
            zero_count = 1
        elif num == 0: 
            zero_count = 0
        else: 
            output.append(num)
    return output

# nearest square number

import math 

def nearest_sq(n):
    return round(math.sqrt(n)) ** 2

# Break camelCase

def solution(s):
    index = ''
    for char in s:
        if char == char.upper():
            index += ' '
            index += char
        else:
            index += char
    return index