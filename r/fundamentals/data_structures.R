# Handling NA values in vectors

order_detail <-c (10,20,30,NA,50,60)
order_detail
names(order_detail) <-c ("Mon","Tue","Wed","Thu","Fri","Sat")
order_detail
order_detail + 5 #Any operation peformed on vector, will be applied to all the values of vector

# Practice Problems:

# 1. Replace all NA values in order_detail with the mean of the non-NA values.
#    Store the result in a new vector called updated_order.
updated_order <- order_detail
updated_order[is.na(updated_order)] <- mean(updated_order[!is.na(updated_order)])
print(updated_order)

# 2. Count the number of NA values in the order_detail vector.
print(sum(is.na(order_detail)))

# 3. Create a new vector called scaled_order that scales all non-NA values
#    in order_detail by dividing them by the maximum non-NA value.
scaled_order <- order_detail[!is.na(order_detail)] / max(order_detail[!is.na(order_detail)])
print(scaled_order)

# -----------------------------------------------------------------

#To add two vectors

new_order <- c(5,10)
update_order <- order_detail + new_order
update_order

# Practice Problems: 

# 1. Create a new vector called weighted_order that multiplies each element
#    of order_detail by the corresponding element in new_order.
weighted_order <- order_detail * new_order
print(weighted_order)

# 2. Find the common elements between order_detail and new_order.
#    Store the result in a vector called common_elements.
common_elements <- intersect(order_detail, new_order)
print(common_elements)

# 3. Calculate the dot product of order_detail and new_order.
dot_product <- sum(order_detail * new_order, na.rm = TRUE)
print(dot_product)

# -----------------------------------------------------------------

#Creating subset of vector

firsttwo<-order_detail[1:2]
firsttwo
l<-length(order_detail)
l

v1<-order_detail[(l-1):l]
v1
v2<-order_detail[(l-1):2]
v2
v3<-order_detail[l:1]
v3
v4<-order_detail[(l-2):l]
v

# Practice Problems: 

# 1. Extract all values from order_detail that are not present in new_order.
#    Store the result in a vector called unique_values.
unique_values <- setdiff(order_detail, new_order)
print(unique_values)

# 2. Identify and extract the local maxima in order_detail.
od_max <- max(order_detail, na.rm = TRUE)
od_min <- min(order_detail, na.rm = TRUE)
print(od_max)
print(od_min)

# 3. Create a vector called reversed_order that reverses the order of elements in order_detail.
reversed_order <- rev(order_detail)
print(reversed_order)

# -----------------------------------------------------------------

#Extract all the values below 30
order_detail<30
order_detail[order_detail<30]

#To omit NA value from the vector
na.omit(order_detail[order_detail<30])

#To find the order details that are multiple of 3

(order_detail %% 3)==0
order_detail[(order_detail %% 3)==0]
na.omit(order_detail[(order_detail %% 3)==0])

sum(order_detail) #Returns NA because there is an NA value in the order detail vector

# Use na.rm to remove the NA value
sum(order_detail,na.rm=T)

mean(order_detail,na.rm=T)
max(order_detail,na.rm=T)
min(order_detail,na.rm=T)
sd(order_detail,na.rm=T)
sqrt(order_detail) # returns the square root

##-----------Matrix in R-------------------##

# We use function matrix() to create a matrix

v <- 20:30
v
matrix(v)

mat1<-matrix(0,3,3)
mat1
mat2<-matrix(1:9,3,3)
mat2

mat3<-matrix(1:9,nrow=3,byrow=T)
mat3
mat3<-matrix(1:9,3,3,byrow=T)
mat3

# Creating matrix from vectors

stock1 <- c(450,451,452,445,468)
stock2 <- c(230,231,232,236,228)
stocks <- c(stock1,stock2) # Merge both the vectors
stocks
stock.matrix <- matrix(stocks,byrow=TRUE,nrow=2)
stock.matrix

# Naming a matrix using colnames() and rownames()

days <- c('Mon','Tue','Wed','Thu','Fri')
st.names <- c('stock1','stock2')

colnames(stock.matrix) <- days
rownames(stock.matrix) <- st.names

stock.matrix

# Functions associated with matrix

nrow(mat3) #returns no. of rows
ncol(mat3) #returns no. of columns
dim(mat3) #returns no. of rows and columns
rownames(stock.matrix) #returns row names
colnames(stock.matrix) #returns column names
dimnames(stock.matrix) #returns row and column names

# Arithmetic operations in Matrix

mat1 <- matrix(1:50,byrow=TRUE,nrow=5)
mat1

# Matrix addition
5+mat1

# Matrix multiplication
5*mat1

# Division of matrix

2/mat1 # returns the reciprocal

# Division of matrix

mat1/2 # returns the quotient

# Exponent

mat1 ^ 2

# Matrix arithmetic with multiple matrices

mat1 + mat1
mat1-mat1
mat1*mat1

# Matrix operations

colSums(stock.matrix) # Returns the sum for each column
rowSums(stock.matrix) # Returns the sum for each row
rowMeans(stock.matrix) # Returns the mean for each row

# Adding rows and columns to a matrix using rbind() and cbind() function

stock3 <- c(150,151,149,120,114)
total_stock <- rbind(stock.matrix,stock3)
total_stock

avg <- rowMeans(total_stock)
avg

total_stock <- cbind(total_stock,avg)
total_stock

# Practice Problems: 

# 1. Calculate the determinant of mat1.
det_mat1 <- det(mat1)
print(det_mat1)

# 2. Multiply each element in mat2 by its row number.
#    Store the result in a new matrix called scaled_mat2.
rows <- 1:nrow(mat2)
scaled_mat2 <- rows * mat2
print(scaled_mat2)

# 3. Create a new matrix called mat4 that is a concatenation of mat1 and mat2 along columns.
mat4 <- cbind(mat1, mat2)
mat5 <- rbind(mat1, mat2)
print(mat4)
print(mat5)

# -----------------------------------------------------------------

# Matrix selection and indexing
student <- matrix(sample(c(NA, runif(8, 40, 98)), size = 16, replace = TRUE), nrow = 4, ncol = 4, byrow = TRUE)
dimnames(student) <- list(c("John","Mathew","Sam","Alice"),c("Phy","Chem","Bio","Maths"))
student

# Practice Problems:

# Matrix selection and indexing

# 1. Replace all NA values in the student matrix with the mean of the entire matrix.
rounded_means <- round(apply(student, 2, mean, na.rm = TRUE))
student[is.na(student)] <- as.integer(rounded_means)
print(student)

# 2. Calculate the average score for each student across all subjects.
#    Store the result in a vector called avg_score.
average_scores <- apply(student, 1, mean)
print(average_scores)

# 3. Extract a submatrix from the student matrix that includes only the students who passed all subjects.
submatrix <- student[apply(student > 60, 1, all), ]
print(submatrix)

# -----------------------------------------------------------------

# Extraction of columns

student[,1]
student[,1:2]
student[,c(1,3)]

# Extraction of rows

student[1,]
student[1:2,]
student[c(1,3),]
student[2,2]
student[2,2:4]

student[3:4,2:3]
student[2:4,c(1,4)]

#Find John's score in Chem and Bio
student["John",2:3]

#Find John's and Sam's score in maths
student[c("John","Sam"),4]

#Find maths & Bio score of Sam and Alice
student[c("Sam","Alice"),3:4]

#Find average score of John
mean(student[c("John"),],na.rm=T)

#Find the average and the total score for all the students
apply(student,1,mean,na.rm=T) #here 1 stands for the row and 2 is for columns
help(apply)
apply(student,1,sum,na.rm=T)

passing_score<-c(25,25,25,70)
passing_score

#Find in how many subjects Alice has passed
pass<-(student[c("Alice"),]>passing_score)
pass
sum(pass, na.rm = T)

#Find in how many subjects Sam has passed
pass1<-(student[c("Sam"),]>passing_score)
pass1
sum(pass1, na.rm = T)

#----------DataFrames in R---------------#

# Check the list of pre-loaded dataset

data()
data(AirPassengers)
head(AirPassengers)
data(iris)
head(iris)
View(iris)
View(state.x77)
View(USPersonalExpenditure)
tail(USPersonalExpenditure)

# Check the statistical summary of a dataset
summary(iris)

# Check the structure of a dataset
str(iris)

# Creating a data frame using data.frame() function

days <- c('mon','tue','wed','thu','fri')
temp <- c(25.6,30.1,45,37.3,41.2)
rain <- c(TRUE, TRUE, FALSE, FALSE, TRUE)

df <- data.frame(days,temp,rain)
print(df)
summary(df)
str(df)

# Dataframe indexing

df[1,] # Extract the first row
df[,2] # Extract the second row

# Selecting using column names
df[,'temp'] # Extracts all the temperature values
df[2:4,c('days','temp')] # extracts the 2nd, 3rd and 4th rows for days and temp

# Use dollar sign if you want all the values of a particular column 

df$days
df$rain

# Use bracket notation to return a data frame format of the same information
df['rain']
df['temp']

# Filtering dataframes using a subset function

subset(df,subset=rain==TRUE) # Returns all the columns where it rained 
subset(df,subset= temp>25) # Returns all the columns where temperature>25

# Sorting dataframes using order function

sorted.temp <- order(df['temp'])
df[sorted.temp,] # Returns the all the columns with temp sorted in ascending order
sorted.temp

desc.temp <- order(-df['temp']) # Returns the all the columns with temp sorted in descending order
df[desc.temp,]

# Another method to sort
sort.temp <- order(df$temp)
df[sort.temp,]

# Merging Data Frames

authors <- data.frame(
    surname = I(c("Tukey", "Venables", "Tierney", "Ripley", "McNeil")),
    nationality = c("US", "Australia", "US", "UK", "Australia"),
    deceased = c("yes", rep("no", 4)))

books <- data.frame(
    name = I(c("Tukey", "Venables", "Tierney",
               "Ripley", "Ripley", "McNeil", "R Core")),
    title = c("Exploratory Data Analysis",
              "Modern Applied Statistics ...",
              "LISP-STAT",
              "Spatial Statistics", "Stochastic Simulation",
              "Interactive Data Analysis",
              "An Introduction to R"),
    other.author = c(NA, "Ripley", NA, NA, NA, NA,
                     "Venables & Smith"))

authors
books

(m1 <- merge(authors, books, by.x = "surname", by.y = "name"))

# Example to manipulate a dataframe 

salesreport <- data.frame(Id=101:110,
                        Product=c("A","B"),
                        Unitprice=as.integer(runif(10,100,200)),
                        Qty=as.integer(runif(10,10,20))
)
salesreport

#1.Transpose data frame
transpose.salesreport<-t(salesreport)
View(transpose.salesreport)
head(transpose.salesreport)

#2.Sorting of data frame
salesreport[order(salesreport$Unitprice),]
salesreport[order(salesreport$Unitprice,decreasing = T),]
salesreport[order(salesreport$Product,-salesreport$Unitprice),]

#3.Subsetting data frame

subset.ProductA<-subset(salesreport,Product=="A")
subset.ProductA

# Extact the rows for which Product is A and Unitprice > 150
subset.salesreport<-subset(salesreport,Product=="A" & Unitprice>150)
subset.salesreport

# Extract only the first and the fourth column Product is A and Unitprice > 150
subset.salesreport<-subset(salesreport,Product=="A" & Unitprice>150,c(1,4))
subset.salesreport

#4.Merging of data frame

setA<-subset(salesreport,Product=="A")
setB<-subset(salesreport,Product=="B")
setA
setB
cbind(setA,setB)
rbind(setA,setB)

#5.Aggregate function
#Total quantity sold for each product

aggregate(salesreport$Qty,list(salesreport$Prod),sum,na.rm=T)

# Practice Problems:

# 1. Add a new column to the df "df" called "humidity" with values (60, 70, 80, 90, 85).
df$humidity <- c(60, 70, 80, 90, 85)
print(df)

# 2. Find the days where both temperature is above 30 and it rained.
#    Hint: Use subset() function with multiple conditions.
temp.subset <- subset(df, df$temp > 30 & df$rain == TRUE)
print(temp.subset)

#----------------------Lists in R------------------#

list_1<-list(x=c(10,20,30),
            y=c("a","b","c"),
            z=c(TRUE,FALSE))
list_1

list2<-list(vec=seq(1:10),
            mat=matrix(1:9,3,3),
            lis=list(a=10,b=20))
list2

# Recursive variable->Variable that can store values of its own type.
is.recursive(list2)

# Indexing of list

list2[2] # By index
list2$mat # By dollar notation
list2['vec'] # By name
list2$lis[2] #3rd element 2nd value
list2[[3]][2] #3rd element 2nd value

length(list2)
class(list2)

#Conversion of vectors to list

price<-c(10,20,30)
pricelist<-as.list(price)
pricelist
price

#Conversion of list to vector

newPrice<-unlist(pricelist)
newPrice

# Use dim function to convert vectors to matrix

price1<-c(10,20,30,40)
dim(price1)<-c(2,2)
price1

# Practice Problems:

# 1. Add a new element to list_1 called "w" with values c(40, 50, 60).
list_1$w <- c(40, 50, 60)
print(list_1)

# 2. Extract the second element of the vec list within list2 and replace it with the list's mean.
mean <- mean(list2[['vec']])
list2[['vec']][2] <- mean
print(list2)

# 3. Check if the list_1 is recursive
print(is.recursive(list_1))

#----------Basic data type functions------------#
n1<-10
class(n1) # Returns the datatype of the variable
typeof(n1)
n2<-10.5
class(n2)
typeof(n2)

is.numeric(n1)  #is.numeric() function returns True if given value is numeric else false
is.numeric(n2)

I1<-as.integer(10) #as.integer converts the given value into integer
I1
I2<-as.integer(10.5)
I2
I3<-as.integer("10")
class(I2)
class(I1)
class(I3)

#All integers are numeric but all numerics are not integers.

is.numeric(I1) #TRUE
is.integer(I1) #TRUE

c1<-"John"
c2<-"Rob"
class(c1)
class(c2)
is.character(c1)
is.character(c2)

toupper(c1) # Converts to uppercase
substr(c1,1,2) # Extract set of characters
name<-paste(c1,c2)
name
name1<-paste0(c1,c2)
name1
name<-paste(c1,c2,sep=",")
name
newname<-sub("Rob","Cena",name) # Replaces set of characters
newname
length(c1)
nchar(c1)

# Practice Problems:

# 1. Convert the temperature values in the df "df" to Fahrenheit.
#    Hint: Use a conversion formula (F = (C * 9/5) + 32).
df$temp <- ((df$temp * (9/5)) + 32)
print(df)

# 2. Check if the variable I1 is a double, and if it is, round it to the nearest integer.
#    Hint: Use is.double() function.
if (is.double(I1)) {
  I1 <- round(I1)
}
print(I1)

# 3. Create a new character vector called "greetings" with elements "Hello," "Hi," and "Hola."
#    Print the concatenation of each greeting with the name "John."
#    Hint: Use the paste() function.
greetings <- c("Hello", "Hi", "Hola")
greetings <- paste(greetings, "John", sep = " ")
print(greetings)
