import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# problem 1
students = pd.read_csv('test_data.csv')
y = 9.85 * students.hours_studied + 43

plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, y)
plt.show()

# problem 2
model = sm.OLS.from_formula("score ~ hours_studied", data = students)
results = model.fit()
print(results.params)

# problem 3
pred_3hr = results.params[1] * 3 + results.params[0]
print(pred_3hr)

new_data = {"hours_studied":[5]}
pred_5hr = results.predict(new_data)
print(pred_5hr)

# problem 4
fitted_values = results.predict(students)
residuals = students.score - fitted_values

for i in range(5):
  print(residuals[i])

# problem 5
plt.hist(residuals)
plt.show()
plt.clf()

plt.scatter(fitted_values, residuals)
plt.show()

# problem 6
plt.scatter(students.breakfast, students.score)

breakfast_score = students.groupby("breakfast").mean().score[1]
no_breakfast_score = students.groupby("breakfast").mean().score[0]
plt.plot([0, 1], [no_breakfast_score, breakfast_score])
plt.show()

# problem 7
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)

model = sm.OLS.from_formula("score ~ breakfast", data = students)
results = model.fit()
print(results.params)

print(mean_score_breakfast - mean_score_no_breakfast)

# problem 8
website = pd.read_csv('website.csv')
print(website.head())

plt.scatter(website.age, website.time_seconds)
plt.show()
plt.clf()

model = sm.OLS.from_formula("time_seconds ~ age", data = website)
results = model.fit()
print(results.params)

linear_regression_line = results.params[0] + results.params[1] * website.age
plt.scatter(website.age, website.time_seconds)
plt.plot(website.age, linear_regression_line)
plt.show()
plt.clf()

fitted_values = results.predict(website)

residuals = website.time_seconds - fitted_values

plt.hist(residuals)

plt.show()
plt.clf()

plt.scatter(residuals, fitted_values)

plt.show()
plt.clf()

pred_40 = results.params[0] + results.params[1] * 40
print(pred_40)

model = sm.OLS.from_formula("time_seconds ~ browser", data = website)
browser_results = browser_model.fit()
browser_eq = browser_results.params[0] + browser_results.params[1] * website.age

plt.scatter(website.browser, website.time_seconds)
plt.plot(website.age, browser_eq)
plt.show

mean_time_chrome = np.mean(website.time_seconds[website.browser == 'Chrome'])
mean_time_safari = np.mean(website.time_seconds[website.browser == 'Safari'])
print('Mean time (Chrome): ', mean_time_chrome)
print('Mean time (Safari): ', mean_time_safari)
print('Mean time difference: ', mean_time_chrome - mean_time_safari)