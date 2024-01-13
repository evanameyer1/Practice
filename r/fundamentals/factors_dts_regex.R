#-------Factors in R----------#

Type<-c("s","m","l","s","l","m")
Type[3]>Type[4]
Type[1]>Type[2]
Type[2]<Type[3]

Type.factor<-factor(TRUE)

#default Nominal factor
Type.factor

Type.factor2<-factor(Type,ordered=T)
#Factor created in ordinal
Type.factor2

Type.factor3<-factor(Type,ordered=T,level=c("s","m","l"))
#Ordered factor with user given order
Type.factor3

Type.factor4<-factor(Type,ordered=T,level=c("s","m","l"),
                     labels=c("small","medium","large"))
Type.factor4

Type.factor4[1]>Type.factor4[2]

Type<-c("Small","Tall","Tallest","Medium","Small",
        "Medium","Tallest","Tall","Small","Small")
Type

#Compare height type of first value with fourth value

Type.factor5<-factor(Type,ordered=T,level=c("Small","Medium","Tall","Tallest"))

Type.factor5

Type.factor5[1]>Type.factor5[4]

as.integer(Type.factor5)

# Practice Problems

# Challenge 1
# Compare the levels of Type.factor2

factor2_levels <- levels(Type.factor2)
prev <- NULL
for (level in factor2_levels) {
  if (!is.null(prev)) {
    print(level)
    print(prev)
    print(level > prev)
  }
  prev <- level
}

# Challenge 2
# Check if the levels of Type.factor3 are in the specified order

factor3_levels <- levels(Type.factor3)
correct_order <- c("s", "m", "l")
print(factor3_levels == correct_order)

# Challenge 3
# Compare the labels of Type.factor4 after reordering

factor4_labels <- labels(Type.factor4)
print(factor4_labels)
for (i in seq_along(factor4_labels[-length(factor4_labels)])) {
  if (factor4_labels[i] > factor4_labels[i + 1]) {
    output <- paste(factor4_labels[i], " > ", factor4_labels[i + 1])
  } else if (factor4_labels[i] < factor4_labels[i + 1]) {
    output <- paste(factor4_labels[i], " < ", factor4_labels[i + 1])
  } else {
    output <- paste(factor4_labels[i], " = ", factor4_labels[i + 1])
  }
  print(output)
}

#-------Vectors in R----------#

# Create a sequence

v <- seq(0,20, by=2)
v

# Sort a vector

v <- c(2,4,5,7,1,16,4)
sort(v)
sort(v,decreasing = TRUE)

# Reverse a vector

v2 <- c(1,2,3,4,5)
rev(v2)

# Structure of a vector
print(v)
str(v)

# Append 2 vectors
append(v,v2)

# Check the class of an R object
v <- c(1,2,3)
is.vector(v)
is.list(v)

# Covert the vector into a list using as.list()
as.list(v)

# Convert the vector into a matrix
as.matrix(v)

# Sample 2 random values between 10 and 20
sample(x = 10:20,1) # The value changes everytime you run it

# Practice Problems:

# Challenge 1
# Check if the first element of v is greater than the last
print(v[1] > v[length(v)])

# Challenge 2
# Create a new vector by concatenating v and v2, then sort it in descending order
v3 <- append(v, v2)
v3 <- sort(v3, decreasing = TRUE)
print(v3)

# Challenge 3
# Check if v is a list, then convert it to a list and check again
print(is.list(v))
v <- as.list(v)
print(is.list(v))

#-------Basic maths functions----------#

abs(-5) # returns the absolute value

v <- c(-3,0,1,-5,6,4,5)
abs(v)

sum(v)
mean(v)
round(45.12453)
round(45.12453,2) # Rounds the number to 2 decimal places
ceiling(45.12453) # Return the next highest integer
floor(45.12453) # Returns the next lowest integer
trunc(56.783) # Truncates the decimal places 
log(2) # Return the log
exp(2) # Return exponent

# Practice Problems

# Challenge 1
# Calculate the sum of the absolute values of vector v
abs_sum <- sum(abs(v))
print(abs_sum)

# Challenge 2
# Round the mean of vector v to the nearest integer
rounded_mean <- round(mean(v))
print(rounded_mean)

# Challenge 3
# Calculate the exponent of the ceiling value of 45.12453
ceil_exp <- exp(ceiling(45.12453))
print(ceil_exp)

#-------Regular expressions----------#

text <- "R is fun to learn"
grepl('learn', text) #returns a logical value indicating if the pattern was found
grepl('study',text)

v <- c('a','b','c','d')
grep('b',v)

grep('d',v)

# Practice Problems

# Challenge 1
# Check if the pattern 'fun' exists in the text variable
grepl('fun', text)

# Challenge 2
# Use grep to find the index of the element 'c' in vector v
grep('c', v)

# Challenge 3
# Check if the pattern 'learn' exists in the text variable using regex
grepl('learn', text)

#-------Working with timestamps----------#

Sys.Date() # Returns the current system date

# Set as a variable
today <- Sys.Date()
today

# YYYY-MM-DD
as.Date('1990-11-03')

# Using Format
# %b month abbreviated
# %d day of the month
# %y year in 2 digits

date1 <- as.Date("Nov-03-90",format="%b-%d-%y")

# Using Format
# %B Full month name
# %Y year in 4 digits

as.Date("November-03-1990",format="%B-%d-%Y")

# Practice Problems:

# Challenge 1
# Calculate the difference in days between today and '1990-11-03'
diff <- today - date1
print(diff)

# Challenge 2
# Create a date object for 'November-03-1990' and print the day of the week
date2 <- as.Date("November-03-1990", format = "%B-%d-%Y")
weekdays(date2)

# Challenge 3
# Create a date object for 'Nov-03-90' and print the month in full
date3 <- as.Date("Nov-03-90", format = "%b-%d-%y")
print(format(date3, "%B"))
