# python practice

def array_diff(a, b):
    a_log = a
    b_log = b
    a_backup = a
    b_backup = b
    final = []
    for item in a:
        if item in b_backup:
            a_log.remove(item)
            c = a_log.count(item)
            for i in range(c):
                a_log.remove(item)
    for item in b:
        if item in a_backup:
            b_log.remove(item)
    
    for item in a_log:
        final.append(item)
    for item in b_log:
        final.append(item)
    
    return final

array_diff([1,2,2,2,3],[2])

def bouncing_ball(height, bounce, window):
    if height > 0 and 0 < bounce < 1 and window < height:
        bounce_height = bounce * height
       # print(bounce_height)
        outcome = 1
        while bounce_height > window:
            outcome += 2
        #    print(bounces)
            bounce_height *= bounce
     #       print(bounce_height)
    else:
        outcome = -1
    return outcome

bouncing_ball(3, 0.66, 1.5)

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

valid_braces('[(])')

def descending_order(num):
    num = str(num)
    index = []
    index.append(num[0])
    num = '' + num[1:]
    print(index)
    for char in num:
        n = 0
        m = 0
        while m != 1:
            if char > index[n]:
                index.insert(n + 1, char)
                m += 1
            if char <= index[n]:
                n += 1
    return ''.join(index)

descending_order(1236790)

import math

def nearest_sq(n):
    return round(math.sqrt(n)) ** 2

nearest_sq(111)


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
    
pair_zeros([0, 1, 7, 0, 2, 2, 0, 0, 1, 0])

def validate_sudoku(board):
    outcome = 0
    row1 = [] 
    row2 = [] 
    row3 = [] 
    row4 = [] 
    row5 = [] 
    row6 = [] 
    row7 = [] 
    row8 = [] 
    row9 = [] 
    for string in board:
        index = []
        for num in string:
            if num in index:
                outcome = 1
            else:
                index.append(num) 
                row(string[num]).append(num)
    return outcome == 0

validate_sudoku([[7,8,4,1,5,9,3,2,6],
[5,3,9,6,7,2,8,4,1],
[6,1,2,4,3,8,7,5,9],
[9,2,8,7,1,5,4,6,3],
[3,5,7,8,4,6,1,9,2],
[4,6,1,9,2,3,5,8,7],
[8,7,6,3,9,4,2,1,5],
[2,4,3,5,6,1,9,7,8],
[1,9,5,2,8,7,6,3,4]])