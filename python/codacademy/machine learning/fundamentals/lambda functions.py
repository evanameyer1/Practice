#Write your lambda function here
contains_a = lambda string: True if 'a' in string.lower() else False

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

#Write your lambda function here
long_string = lambda s:True if len(s) > 12 else False

print(long_string("short"))
print(long_string("photosynthesis"))

#Write your lambda function here
ends_in_a = lambda s:True if s[-1] in "aA" else False

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#Write your lambda function here
double_or_zero = lambda n:n*2 if n > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

#Write your lambda function here
even_or_odd = lambda n:'even' if n % 2 == 0 else 'odd'

print(even_or_odd(10))
print(even_or_odd(5))

#Write your lambda function here
multiple_of_three = lambda n:"multiple of three" if n % 3 == 0 else "not a multiple"

print(multiple_of_three(9))
print(multiple_of_three(10))

#Write your lambda function here
rate_movie = lambda n:"I liked this movie" if n > 8.5 else "This movie was not very good"

print(rate_movie(9.2))
print(rate_movie(7.2))

#Write your lambda function here
ones_place = lambda n:n%10

print(ones_place(123))
print(ones_place(4))

#Write your lambda function here
double_square = lambda n:n**2 * 2

print(double_square(5))
print(double_square(3))

import random
#Write your lambda function here
add_random = lambda n:n + random.randint(1, 10)
print(add_random(5))
print(add_random(100))