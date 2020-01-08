
# import modules
import pandas as pd
import matplotlib.pyplot as plt

# Read datasets for yearly deaths by clinic
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')

# Print out yearly
print(yearly.head(5))

# calculate the proportion of deaths per births
yearly['proportion_deaths'] = (yearly.deaths / yearly.births)

# Extract clinic depended deaths
clinic1 = yearly[yearly.clinic == 'clinic 1']
clinic2 = yearly[yearly.clinic == 'clinic 2']

# print sample clinic 1
print(clinic1.head(5))

# plot yearly proportion of deaths
ax1=clinic1.plot(x='year',y='proportion_deaths', label='clinic 1')
clinic2.plot(x='year', y='proportion_deaths', label='clinic 2', ax=ax1)
plt.show()

# read the monthly deaths data
monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])

# print sample rows
print(monthly.head(5))
# find the propotion of deaths
monthly['proportion_deaths'] = (monthly.deaths / monthly.births)
# plot monthly proportion of deaths
ax = monthly.plot(x='date', y='proportion_deaths')
ax.set_ylabel('proportion of deaths')
plt.show()

# handwashing effect
handwashing_start = pd.to_datetime('1847-06-01')

# split monthly deaths data to before and after handwashing started
before_handwashing = monthly[monthly['date'] < handwashing_start]
after_handwashing  = monthly[monthly['date'] >= handwashing_start]

# plot monthly proportion of deaths before and after handwshing started
ax2 = before_handwashing.plot(x='date', y='proportion_deaths', label='before handwashing')
after_handwashing.plot(x='date', y='proportion_deaths', label='after_handwashing', ax=ax2)
ax2.set_ylabel('proportion of deaths')
plt.show()

# difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_handwashing.proportion_deaths
after_proportion  = after_handwashing.proportion_deaths

# calculate the mean difference
mean_diff = (after_proportion.mean() - before_proportion.mean())
print(mean_diff)

# a boostrap analysis of the reduction in deaths due to handwshing

boot_mean_diff = []
for i in range(10000):
    before_boot = before_proportion.sample(frac=1, replace=True)
    after_boot  = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(after_boot.mean() - before_boot.mean())

# calculate the 95% confidence interval
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])

print(confidence_interval * 100)
print('Nice doctors should wash their hands')
