# Basic Arithmetic Operations

# Explanation of topic
# R supports basic arithmetic operations such as addition, subtraction, multiplication, division, exponentiation, and modulo.

# Example of topic in use
sum_result <- 192 + 250    # Addition
diff_result <- 955 - 380   # Subtraction
prod_result <- 20 * 100    # Multiplication
div_result <- 50 / 5       # Division
exp_result <- 5^4          # Exponentiation
mod_result <- 18 %% 7      # Modulo
order_result <- (500 * 2) + (80 / 2)  # Order of operations
order_result2 <- 500 * (2 + 1)         # Order of operation

# Practice problems
# 1. Calculate the result of (15 * 3) - (8 / 2).
ans1 <- (15 * 3) - (8 / 2)
print(ans1)

# 2. Compute the square of 9.
ans2 <- 9^2
print(ans2)

# 3. Find the remainder when 67 is divided by 9.
ans3 <- 67 %% 9
print(ans3)

# Assigning Variables

# Explanation of topic
# Variables in R can be assigned using the <- operator.

# Example of topic in use
selling <- 500               # Assign variable1
cost <- 250                  # Assign variable2
profit <- selling - cost     # Assign variable3

# Practice problems
# 1. Create a variable called "length" and assign it the value 10.
length <- 10
print(length)

# 2. Calculate the total cost by subtracting 20 from the selling price.
total_cost <- selling - 20
print(total_cost)
  
# 3. Create a variable named "name" and assign it your name.
name <- 'Evan'
print(name)

# Data Types in R

# Explanation of topic
# R has different data types, including numeric, integer, logical, character, and complex.

# Example of topic in use
num <- 3.7           # Numeric data type
i <- 10              # Integer data type
t <- TRUE            # Logical data type
f <- FALSE           # Logical data type
ch <- "HELLO"        # Character data type
c <- 1 + 2i          # Complex data type

# Practice problems
# 1. Create a logical variable named "is_positive" and assign it the value TRUE.
is_positive <- TRUE
print(is_positive)

# 2. Define a character variable "city" and assign it the name of your city.
city <- 'Chicago'
print(city)

# 3. Create a complex variable named "comp_num" with a real part of 3 and an imaginary part of 2.
comp_num <- 3 + 2i
print(comp_num)

# Vectors in R

# Explanation of topic
# Vectors are one-dimensional arrays in R that can hold elements of the same data type.

# Example of topic in use
vec1 <- c(10, 20, 30)
vec2 <- c("a", "b", "c")
vec3 <- c(TRUE, FALSE, TRUE)

# Practice problems
# 1. Create a numeric vector named "ages" with values 25, 30, and 35.
ages <- c(25, 30, 35)
print(ages)

# 2. Form a character vector "colors" with the names of three different colors.
colors <- c("red", "blue", "green")
print(colors)

# 3. Construct a logical vector "status" with three values representing True, False, and True.
status <- c(True, False, True)
print(status)

# Naming Your Vectors

# Explanation of topic
# Vectors in R can be assigned names using the names() function.

# Example of topic in use
temperature <- c(72, 71, 68, 73, 69, 75, 71)
names(temperature) <- c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(temperature)

# Practice problems
# 1. Create a numeric vector "sales" with values 120, 150, and 200, and name it as "Week1", "Week2", and "Week3".
sales <- c(120, 150, 200)
names(sales) <- c('Week1', 'Week2', 'Week3')
print(sales)

# 2. Generate a character vector "months" with the names of three different months and assign names accordingly.
months <- c('Apr', 'Oct', 'Dec')
names(months) <- c('April', 'October', 'December')
print(months)

# 3. Form a logical vector "results" with three values representing True, False, and True, and provide meaningful names.
results <- c(True, False, True)
names(results) <- c('Happy', 'Healthy', 'Tired')
print(results)

# Basic Operations on Vectors

# Explanation of topic
# Basic mathematical operations can be performed on vectors in R.

# Example of topic in use
v1 <- c(2, 1, 4)
v2 <- c(5, 6, 7)

# Practice problems
# 1. Create two numeric vectors, v3 and v4, with three elements each and perform element-wise addition.
v3 <- c(12, 47, 83)
v4 <- c(42, 11, 90)
v5 <- v3 + v4
print(v5)

# 2. Form two logical vectors, log1 and log2, with three elements each and perform element-wise multiplication.
log1 <- c(23, 45, 180)
log2 <- c(145, 2, 7)
print(log2 * log1)

# 3. Create a numeric vector "prices" with values 50, 75, 100, and calculate the total sum of these prices.
prices <- c(50, 75, 100)
print(sum(prices))

# Comparing Vectors Using Comparison Operators

# Explanation of topic
# Vectors in R can be compared using comparison operators.

# Example of topic in use
v1 <- c(19, 12, 45)
v2 <- c(19, 20, 30)

# Practice problems
# 1. Create a numeric vector "nums" with values 10, 15, and 20. Compare it with the vector v1 using the equality operator.
nums <- c(10, 15, 20)
print(nums == v1)

# 2. Generate a logical vector "checks" by comparing v1 and v2 using the greater than operator.
checks <- v2 > v1
print(checks)

# 3. Form a logical vector "inequality" by checking if v1 is not equal to v2.
inequality <- v1 == v2
print(inequality)

# Vector Slicing and Indexing

# Explanation of topic
# Vectors can be sliced and indexed using various methods in R.

# Example of topic in use
price1 <- seq(550, 670, 20)
names(price1) <- paste0("p", 1:7)

# Practice problems
# 1. Retrieve the third element from the vector price1 using index position.
print(price1[3])

# 2. Extract elements 3 and 4 from price1 using index positions.
print(price1[3:4])

# 3. Select the elements at index 1 and 4 from price1 using a combination of index positions.
print(price1[c(1, 4)])
