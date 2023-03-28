# working with scipy.stats
import numpy as np
import scipy.stats as stats

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 10

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# create 12-sided "die"
die_12 = range(1, 13)

# roll the 12-sided "die" 10 times
results_2 = np.random.choice(die_12, size = 10, replace = True)

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

## Question 2
prob_2 = stats.binom.pmf(7, 20, 0.5)

## Checkpoint 1
prob_1 = stats.binom.pmf(4, 10, 0.5) + stats.binom.pmf(5, 10, 0.5) + stats.binom.pmf(6, 10, 0.5)
print(prob_1)

## Checkpoint 2
prob_2 = 1 - (stats.binom.pmf(0, 10, 0.5) + stats.binom.pmf(1, 10, 0.5) + stats.binom.pmf(2, 10, 0.5))
print(prob_2)

## Checkpoint 1
prob_1 = stats.binom.cdf(3, 10, 0.5)
print(prob_1)

# compare to pmf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 2
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
print(prob_2)


## Checkpoint 3
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5)
print(prob_3)

# compare to pmf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))

prob = stats.norm.cdf(175, 167.64, 8)
print(prob)

## Checkpoint 1
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)
print(temp_prob_1)

## Checkpoint 2
temp_prob_2 = 1 - stats.norm.cdf(24, 20, 3)
print(temp_prob_2)

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 7)
print(np.random.choice(die_6, size = 5, replace = True))


## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))


## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))


## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))


## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))


# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15, 15)

# print prob_15
print(prob_15)

## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(9, 15) + stats.poisson.pmf(7, 15) + stats.poisson.pmf(8, 15)
print(prob_7_to_9)

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20, 15)
print(prob_more_than_20)

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print(prob_17_to_21)

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17), max(rand_vars_17))

## Checkpoint 1
expected_baskets = 0.85 * 20

## Checkpoint 2
expected_late = 0.02 * 180

## Checkpoint 1
variance_baskets = 20 * 0.85 * 0.15

## Checkpoint 2
variance_late = 180 * 0.98 * 0.02

## Checkpoint 1
expected_bonus = 75000 * 0.08

## Checkpoint 2
num_goals =  stats.poisson.rvs(4, size = 100)

## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = num_goals * 2
print(np.var(num_goals) * 4)

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
print(stats.poisson.pmf(lam, lam))

## Task 3:
print(stats.poisson.cdf(4, lam))

## Task 4:
print(1 - stats.poisson.cdf(9, lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size=365)

## Task 6:
for i in range(20):
  print(year_defects[i])

## Task 7:
print(stats.poisson.pmf(lam, lam) * 365)
print(lam * 365)

## Task 8:
print(sum(year_defects))
print(sum(year_defects) - (lam * 365))

## Task 9:
print(np.mean(year_defects))

## Task 10:
print(max(year_defects))

## Task 11:
print(1 - stats.poisson.cdf(max(year_defects), lam))

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9, lam))

# Task 13
print(len([num for num in year_defects if num >= stats.poisson.ppf(0.9, lam)]) / len(year_defects))