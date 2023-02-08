# if else statements

num1 = float(input('Insert your first number: '))
num2 = float(input('Insert your second number: '))   

if num1 == num2:
    print('These are equal!')
else:
    print("These aren't equal!")

if 50 > 30:
    print('50 > 30')
else:
    print('50 !> 30')

health = 10

if health > 70:
    print("You are in great health!")
elif health > 40:
    print("Your health is average. Exercise and eat healthily")
else:
    print('Your health is low! Please see a doctor.')

weight = int(input("Enter the weight of your suitcase in pounds: "))

if weight > 50:
    print('Suitcase is over 50 pounds')
elif weight > 25:
    print('Suitcase is over 25 pounds')
else:
    print('Did you even pack anything!?')

temperature = float(input('What is the temperature (F)? '))
weather = input('What is the weather (rain or shine)? ')

if temperature > 60:
    if weather == 'rain':
        print('bring an umbrella')
    elif weather == 'shine':
        print('wear a t-shirt')
else:
    if weather == 'rain':
        print('bring an umbrella and a jacket')
    else:
        print('bring a jacket')

temperature = int(input("What's today's temperature: "))
weather = input("Rain or shine: ")

if temperature > 60 and weather == 'rain':
    print('Bring an umbrella')
elif temperature > 60 and weather == 'shine':
    print('Wear a t-shirt')
elif temperature <= 60 and weather == 'rain':
    print('Bring an umbrella and a jacket')
else: 
    print('Bring a jacket')

temperature = float(input('What is the temperature (F)? '))
weather = input('What is the weather (rain or shine)? ')

if temperature > 60:
    if weather == 'rain':
        print('bring an umbrella')
    elif weather == 'shine':
        print('wear a t-shirt')
else:
    if weather == 'rain':
        print('bring an umbrella and a jacket')
    else:
        print('bring a jacket')

# for loops

l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
for i in l:
    print(i)
    
for i in range(1, 16):
    print(i)

for i in range(1, 16):
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
    
l=[]
for i in range(1, 16):
    l.append(i)
print(l)

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']
for value in animals:
    print((value.upper()))

l = []
animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']
for value in animals:
    l.append(value.capitalize())
print(animals)
print(l)

animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']
d = {}

vowel = "aeiou"
        
for value in animals:
    vowel_count = 0
    for i in value:
        if i in vowel:
            vowel_count += 1
    d[value] = vowel_count
    
print(d)

# while loops

sentence = "A MAN KNOCKED ON MY DOOR AND ASKED FOR A SMALL DONATION TOWARDS THE LOCAL SWIMMING POOL SO I GAVE HIM A GLASS OF WATER"
vowels = 'AEIOU'
vowel_count = 0
iterations = 0

while vowel_count < 1000000:
    for letter in sentence:
        if letter in vowels:
            vowel_count += 1
    iterations += 1

print(iterations)

