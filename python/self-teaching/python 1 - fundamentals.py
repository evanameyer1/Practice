# day 1 - learning the fundamentals of python

v = 4

v2 = v*v

print(v)
print(v2)

15 + 25

f = 'apple'

# variables

x = 3.6
x = 4
x = 'apple'

type(x)
print(type(x))

# operators

print(45+6)
print(25-4)
print(3*7)
print(15/3)

10//2

2 ** 2

15 % 2

x = True

True and False

not False

True or False

# numbers

float(4)
int(4)

# strings

x = "apple"
y = 'apple'
print(x)
print(y)

len(x)

x.replace('pp', 'PP')

x.index("p", 2, 4)
x[1:3]
x[-3]
x[1:4:2]

print("app" + "le")
print(x[0:3] + x[3:6])

print(greeting + ", my name is " + name + " and I am " + mood + " about learning python.")

print(str(2) + "apple")

# lists

fruits = ["banana", "orange", "apple"]

fruits[0]
fruits[-2]

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
type(colors[0]), type(colors[1]), type(colors[2]), type(colors[3]), type(colors[4]), type(colors[5]), type(colors[6])
print(f'The colors of the rainbow are {colors}')

colors[2] = "Lightning Yellow"
colors[4] = "Deep Sea Blue"
print(colors)

print(colors[2])
print(colors)

colors.append("Pink")
print(colors)

colors[::2]
colors[3][0:4:2]

start = 10
stop = 30
step = 2
list(range(start, stop, step))

l = []

l.append(2)
l.append(4)
l.append(6)
l.extend(['g', 'h'])
l.insert(2, 'd')
l.extend(['a', 'a', 'a'])
print(l)
del l[8:]
print(l)

candidates = ["Alice", "Boris", "Carmen"]

candidates.append("Diego")
print(candidates)

candidates[0] = "Alyce"
print(candidates)

candidates.insert(0, "Aaron")
print(candidates)

borisplace = candidates.index("Boris")
print(f"{candidates[2]} is currently in {borisplace}nd place!") 

candidates.remove("Carmen")
print(candidates)

candidates.pop(0)
print(candidates)

candidates.insert(2, "DeSean")
candidates.pop(0)
print(candidates)

print(candidates)

# tuples

testtuple = ("apple", "banana", "orange", "watermelon")
print(testtuple)
print(type(testtuple))

testtuple[0::2]

(red, yellow, orange, green) = testtuple
print(red)
print(yellow)
print(orange)
print(green)
(red, *yellow, green) = testtuple
print(red)
print(yellow)
print(green)

# sets

testset = set(testtuple)
print(testset)

testset.add("pineapple")
print(testset)

testset.remove("pineapple")
print(testset)

print(*set(testtuple))

# dictionaries

item = {'item_name': 'tomato', 'category':'food', 'price':1.99, 'fresh': True}
print(item)

print(item['fresh'])
print(item['item_name'])

item["brand"] = "Mrs. Tomato"
print(item)

item["category"] = "vegetable"
print(item)

print(tuple(item))

house = { "address": "123 Fake Street", "price": 750000, "bedrooms": 3}

for key, value in house.items():
    if key == "bedrooms":
        print(value)

print(house['bedrooms'])

house["zip_code"] = 95404
print(house)

print("This " + str(house["bedrooms"]) + " bedroom house costs $" + str(house["price"]))

print("Hey! Welcome to the housing market simulator. Sell your house!")
address = input("What is your houses' address: ")
starting_price = float(input("What do you want to price your house at: "))
house = { "address": address, "price": starting_price, "bedrooms": 3}
original_price = math.trunc(house['price'])
print(f"Starting price is ${original_price}")
updated_house = int(house['price'])
multiplier = float(input("Oh snap! Interest is high so you should increase your price! Insert the desired % increase: "))
                 
if multiplier <= 1 :
      multiplier = float(input("No silly! Only whole number %'s work: "))
else:
      increase = float((multiplier + 100) / 100)

updated_house *= increase
updated_price = math.trunc(updated_house)
price = (1.3 - increase) * updated_price

if multiplier > 30:
    updated_price = float(input("Woahhhhh! That's a little much and now you lost interest. Pick a new price that's lower then your starting: "))
    difference = ((starting_price - updated_price) / starting_price) * 100  
    if updated_price < starting_price:
        print(f"Bam, house sold! Unfortunately you got a little greedy so ultimately you sold for {difference}% less then your original price, but at least it's sold!")
    else:
        print("Hello, my name is Karma. And I'm a bitch. You didn't sell your house because you got greedy and tried to cheat me!")

elif multiplier > 10:
    print(f"You priced perfectly! Now, your house on '{house['address']}' increased in price by {multiplier}% from ${original_price} to ${updated_price} and sold!")
else:
    print(f"You don't believe in yourself enough! You made a little more, but you could have made even more! You lost out on ${price}!") 






























