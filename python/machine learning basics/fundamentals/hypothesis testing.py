import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import binom_test
from scipy.stats import ttest_1samp

#problems 1-3

prices = np.genfromtxt("prices.csv")
print(prices)

prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))

expected_mean = 1000
tstat, pval = ttest_1samp(prices, expected_mean)

print(tstat)
print(pval)

plt.hist(prices)
plt.show()

# problem 4

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

expected_mean = 1000
tstat, pval = ttest_1samp(daily_prices[0], expected_mean)

print(tstat)
print(pval)

pvalues = []
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], expected_mean)
  pvalues.append(pval)

print(pvalues)

updated_mean = 950

pvalues = []
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], updated_mean)
  pvalues.append(pval)

print(pvalues)

# problem 5

monthly_report = pd.read_csv('monthly_report.csv')

print(monthly_report.head())

sample_size = len(monthly_report)
print(sample_size)

num_purchased = len(monthly_report[monthly_report['purchase'] == 'y'])
print(num_purchased)

# problem 6

one_visitor = np.random.choice(['y', 'n'], p=[0.1, 0.9])
print(one_visitor)

simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
print(simulated_monthly_visitors)

# problem 7
num_purchased = len([v for v in simulated_monthly_visitors if v == 'y'])
print(num_purchased)

# problem 8

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)

null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(null_min, null_max)

# problem 9
plt.hist(null_outcomes)
plt.axvline(41, color = 'r')
plt.show()

# problem 10
null_90CI = np.percentile(null_outcomes, [5, 95])
print(null_90CI)

# problem 11
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41) / len(null_outcomes)
print(p_value)

# problem 12
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59)) / len(null_outcomes)
print(p_value)

# problem 13
def simulation_binomial_test(observed_successes, n, p):
  null_outcomes = []
  
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1 - p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 

  return p_value

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = simulation_binomial_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

# problem 14

from scipy.stats import binom_test

p_value_2sided = binom_test(41, n=500, p=0.1)
print(p_value_2sided)

p_value_1sided = binom_test(41, n=500, p=0.1, alternative = 'less')
print(p_value_1sided)

# problem 15

def simulation_binomial_test(observed_successes, n, p, alternative_hypothesis):
  null_outcomes = []
  
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)
  null_outcomes = np.array(null_outcomes)
  if alternative_hypothesis == 'less':
    p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  elif alternative_hypothesis == 'not_equal':
    difference = np.abs(n*p - observed_successes)
    upper = p*n + difference
    lower = p*n - difference
    p_value = np.sum((null_outcomes <= lower) | (null_outcomes >= upper))/len(null_outcomes) 
  else:
    p_value = np.sum(null_outcomes >= observed_successes)/len(null_outcomes) 

  return p_value

print('lower tail one-sided test:')
p_value1 = simulation_binomial_test(45, 500, .1, alternative_hypothesis = 'less')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

print('upper tail one-sided test:')
p_value1 = simulation_binomial_test(53, 500, .1, alternative_hypothesis = 'greater')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(53, 500, .1, alternative = 'greater')
print("binom_test p-value: ", p_value2)

print('two-sided test:')
p_value1 = simulation_binomial_test(42, 500, .1, alternative_hypothesis = 'not_equal')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(42, 500, .1)
print("binom_test p-value: ", p_value2)

# problem 16

false_positives = 0
sig_threshold = 0.01

for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

print(false_positives/1000)

# problem 17

sig_threshold = 0.1
num_tests = np.array(range(50))
probabilities = 1-((1-sig_threshold)**num_tests)
plt.plot(num_tests, probabilities)

plt.title('Type I Error Rate for Multiple Tests', fontsize=15)
plt.ylabel('Probability of at Least One Type I Error', fontsize=12)
plt.xlabel('Number of Tests', fontsize=12)
              
plt.show()

# problem 18

heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
chol_hd = yes_hd.chol

yes_hd_mean = np.mean(yes_hd.chol)
print(yes_hd_mean)

yes_hd_ttest, yes_hd_pval = ttest_1samp(chol_hd, 240)
yes_hd_pval = yes_hd_pval / 2
print(yes_hd_pval)

sig_thresh = 0.05

if yes_hd_pval <= sig_thresh:
  print('significant')
else:
  print('not significant')

no_hd_mean = np.mean(no_hd.chol)
print(no_hd_mean)

no_hd_ttest, no_hd_pval = ttest_1samp(chol_hd, 240)
no_hd_pval = no_hd_pval / 2
print(no_hd_pval)

sig_thresh = 0.05

if no_hd_pval <= sig_thresh:
  print('significant')
else:
  print('not significant')

num_patients = len(heart)

num_highfbs_patients = len([x for x in heart.fbs if x == 1])
print(num_highfbs_patients)

expected_diabetes = 0.08 * num_patients
print(expected_diabetes)

p_value = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')
print(p_value)

if p_value <= sig_thresh:
  print('significant')
else:
  print('not significant')