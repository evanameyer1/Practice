import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3
from scipy import stats

# problem 1

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() 

samp_size = 10
sample = np.random.choice(np.array(population), samp_size, replace = False)

sample_mean = round(np.mean(sample), 3)

sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

# problem 2

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf()

samp_size = 10
sample = np.random.choice(np.array(population), samp_size, replace = False)

sample_mean = round(np.mean(sample), 3)

sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

# problem 3

cod_population = pd.read_csv("cod_population.csv")
population = cod_population['Cod_Weight']

sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

plt.clf() 
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

# problem 4

population_mean = 10
population_std_dev = 10
samp_size = 6

population = np.random.normal(population_mean, population_std_dev, size = 100000)

sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

sns.histplot(sample_means, stat='density')
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()

# problem 5

population_mean = 36
population_std_dev = 30
samp_size = 50

population = np.random.normal(population_mean, population_std_dev, size = 100000)

sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlim(-50,125)
plt.ylim(0,0.045)
plt.show()
plt.clf()

sns.histplot(sample_means, stat = 'density')
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}")
plt.xlim(20,50)
plt.ylim(0,0.3)
plt.show()

# problem 6

app_stat_text = "Maximum"
def app_statistic(x):
    return np.mean(x)

mean, std_dev = 50, 15
population = np.random.normal(mean, std_dev, 1000)

pop_statistic = round(app_statistic(population),2)

sns.histplot(population, stat = 'density')
plt.axvline(pop_statistic,color='r',linestyle='dashed')
plt.title(f"Population {app_stat_text}: {pop_statistic}")
plt.xlabel("")
plt.show()
plt.clf()

sample_stats = []
samp_size = 5
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_stat = app_statistic(samp)
    sample_stats.append(this_sample_stat)

sns.histplot(sample_stats, stat = 'density')
plt.title(f"Sampling Dist of the {app_stat_text} \nMean: {round(np.mean(sample_stats),2)}")
plt.axvline(np.mean(sample_stats),color='r',linestyle='dashed')
plt.xlabel(f"Sample {app_stat_text}")
plt.show()
plt.clf()

# problem 7

x = 30
mean = 36
std_dev = 20
samp_size = 25
standard_error = std_dev / (samp_size**.5)

cod_cdf = stats.norm.cdf(x, mean, standard_error)
print(cod_cdf)

# final question

def choose_statistic(x, sample_stat_text):
  if sample_stat_text == "Mean":
    return np.mean(x)
  elif sample_stat_text == "Minimum":
    return np.min(x)
  elif sample_stat_text == "Variance":
    return np.var(x, ddof=1)
  else:
    raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')

def population_distribution(population_data):
  sns.histplot(population_data, stat='density')
  plt.title(f"Population Distribution")
  plt.xlabel('')
  plt.show()
  plt.clf()

def sampling_distribution(population_data, samp_size, stat):
  sample_stats = []
  for i in range(500):
    samp = np.random.choice(population_data, samp_size, replace = False)
    sample_stat = choose_statistic(samp, stat)
    sample_stats.append(sample_stat)
  
  pop_statistic = round(choose_statistic(population_data, stat),2)
  sns.histplot(sample_stats, stat='density')
  plt.title(f'Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}')
  plt.axvline(pop_statistic,color='g',linestyle='dashed', label=f'Population {stat}')
  plt.axvline(np.mean(sample_stats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()

spotify_data = pd.read_csv('spotify_data.csv')
spotify_data.head()
song_tempos = spotify_data['tempo']

population_distribution(song_tempos)
sampling_distribution(song_tempos, 30, 'Mean')
sampling_distribution(song_tempos, 30, 'Minimum')
sampling_distribution(song_tempos, 30, 'Variance')

population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)
sample_size = 30
standard_error = population_std / (sample_size ** 0.5)

print(stats.norm.cdf(140, population_mean, standard_error))
print(1 - stats.norm.cdf(150, population_mean, standard_error))