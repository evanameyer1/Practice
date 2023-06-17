# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:

print('Students that complete 0 prior lessons are expected to have a score around 13.21.')

# Slope interpretation:

print('Students are expected to see about a 1.3 increase in their score for each lesson they completed prior.')

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)

plt.plot(codecademy.completed, results.predict(codecademy))

# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
answer1 = results.params[0] + results.params[1] * 20

test_data = {'completed':[20]}
answer2 = results.predict(test_data)

print(answer1, answer2)

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x = 'lesson', y = 'score', data = codecademy)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
lesson_a_avg = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
lesson_b_avg = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])

print(lesson_a_avg, lesson_b_avg, lesson_a_avg - lesson_b_avg)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()