#QUESTION 1
import pandas as pd
# Load the dataset
df = pd.read_csv ('censusdata/acs2015_census_tract_data.csv')


# Get a brief summary of the dataset structure
print("Dataset Structure:")
print(df.info())

# Identify columns with missing values
missing_values = df.isnull().sum()
print("\nColumns with missing values and number of missing entries:")
print(missing_values[missing_values > 0])

# Calculate mean, median, and standard deviation for 'Income' and 'TotalPop'
income_stats = {
    'mean': df['Income'].mean(),
    'median': df['Income'].median(),
    'std': df['Income'].std()
}

totalpop_stats = {
    'mean': df['TotalPop'].mean(),
    'median': df['TotalPop'].median(),
    'std': df['TotalPop'].std()
}

print("\nIncome Statistics:")
print(f"Mean: {income_stats['mean']}, Median: {income_stats['median']}, Std Dev: {income_stats['std']}")

print("\nTotal Population Statistics:")
print(f"Mean: {totalpop_stats['mean']}, Median: {totalpop_stats['median']}, Std Dev: {totalpop_stats['std']}")

#QUESTION 2
import pandas as pd

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')

# Remove rows with missing values
df_cleaned = df.dropna()

# Create a new column 'MaleFemaleRatio' by dividing 'Men' by 'Women'
df_cleaned['MaleFemaleRatio'] = df_cleaned['Men'] / df_cleaned['Women']

# Calculate the median income of the entire dataset
median_income = df_cleaned['Income'].median()

# Filter the dataset to include only rows where 'Income' is greater than the median
df_filtered = df_cleaned[df_cleaned['Income'] > median_income]

# Save the cleaned and filtered dataset to a new CSV file
df_filtered.to_csv('acs2015_census_cleaned.csv', index=False)

print("Cleaned and filtered dataset saved as 'acs2015_census_cleaned.csv'")

#QUESTION 3
import pandas as pd

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')

# Remove rows with missing values
df_cleaned = df.dropna()

# Group by state and calculate mean, median, max, and min 'Income' for each state
income_stats_by_state = df_cleaned.groupby('State')['Income'].agg(['mean', 'median', 'max', 'min'])

# Sort the results by mean income in descending order
income_stats_sorted = income_stats_by_state.sort_values(by='mean', ascending=False)

# Identify the top 5 and bottom 5 states based on mean income
top_5_states = income_stats_sorted.head(5)
bottom_5_states = income_stats_sorted.tail(5)

# Display the results
print("Top 5 states based on mean income:")
print(top_5_states)

print("\nBottom 5 states based on mean income:")
print(bottom_5_states)

#QUESTION 4
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')

# Remove rows with missing values
df_cleaned = df.dropna()

# Create a histogram of the 'Income' column using 50 bins
plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['Income'], bins=50, color='blue', edgecolor='black')

# Add title and labels
plt.title('Income Distribution', fontsize=15)
plt.xlabel('Income', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Save the histogram as an image file
plt.savefig('income_histogram.png')

# Display the plot
plt.show()

#QUESTION 5

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')

# Remove rows with missing values for 'Income' and 'IncomePerCap'
df_cleaned = df[['Income', 'IncomePerCap']].dropna()

# Calculate the correlation between 'Income' and 'IncomePerCap'
correlation = df_cleaned['Income'].corr(df_cleaned['IncomePerCap'])
print(f"Correlation between Income and IncomePerCap: {correlation}")

# Create a scatter plot of 'Income' vs 'IncomePerCap'
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['Income'], df_cleaned['IncomePerCap'], color='blue', alpha=0.5)

# Add title and labels
plt.title('Income vs IncomePerCap', fontsize=15)
plt.xlabel('Income', fontsize=12)
plt.ylabel('IncomePerCap', fontsize=12)

# Save the scatter plot as an image file
plt.savefig('income_scatter.png')

# Display the plot
plt.show()

#QUESTION 6

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')

# Remove rows with missing values for 'Professional' and 'Income'
df_cleaned = df[['Professional', 'Income']].dropna()

# Calculate the correlation between 'Professional' and 'Income'
correlation = df_cleaned['Professional'].corr(df_cleaned['Income'])
print(f"Correlation between Professional percentage and Income: {correlation}")

# Create a scatter plot with 'Professional' on the x-axis and 'Income' on the y-axis
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['Professional'], df_cleaned['Income'], color='green', alpha=0.5)

# Add title and labels
plt.title('Professional Employment vs Income', fontsize=15)
plt.xlabel('Percentage of Professional Workers', fontsize=12)
plt.ylabel('Income', fontsize=12)

# Save the scatter plot as an image file
plt.savefig('professional_income_scatter.png')

# Display the plot
plt.show()

#QUESTION 7
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('censusdata/acs2015_census_tract_data.csv')


# Remove rows with missing values for necessary columns
df_cleaned = df.dropna(subset=['Unemployment', 'Employed', 'Income', 'Professional', 'WorkAtHome', 'TotalPop'])

# a) Calculate UnemploymentRate and analyze its relationship with Income
df_cleaned['UnemploymentRate'] = (df_cleaned['Unemployment'] / df_cleaned['Employed']) * 100

# Calculate correlation between UnemploymentRate and Income
correlation_unemployment_income = df_cleaned['UnemploymentRate'].corr(df_cleaned['Income'])
print(f"Correlation between Unemployment Rate and Income: {correlation_unemployment_income}")

# Create scatter plot: Unemployment Rate vs Income
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['UnemploymentRate'], df_cleaned['Income'], color='purple', alpha=0.5)
plt.title('Unemployment Rate vs Income', fontsize=15)
plt.xlabel('Unemployment Rate (%)', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.savefig('unemployment_vs_income_scatter.png')
plt.show()

# b) Group data by 'State' and calculate average unemployment rate
state_unemployment = df_cleaned.groupby('State')['UnemploymentRate'].mean().sort_values(ascending=False)

# Top 10 states with the highest unemployment rates
top_10_unemployment_states = state_unemployment.head(10)
print("Top 10 states with the highest unemployment rates:")
print(top_10_unemployment_states)

# Create bar plot for top 10 states with the highest unemployment rates
plt.figure(figsize=(12, 6))
top_10_unemployment_states.plot(kind='bar', color='red', edgecolor='black')
plt.title('Top 10 States with Highest Unemployment Rates', fontsize=15)
plt.xlabel('State', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.xticks(rotation=45)
plt.savefig('top10_unemployment_by_state.png')
plt.show()

# c) Analyze relationship between UnemploymentRate and Professional percentage
correlation_unemployment_professional = df_cleaned['UnemploymentRate'].corr(df_cleaned['Professional'])
print(f"Correlation between Unemployment Rate and Professional Percentage: {correlation_unemployment_professional}")

# Create scatter plot: Professional vs Unemployment Rate
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['Professional'], df_cleaned['UnemploymentRate'], color='green', alpha=0.5)
plt.title('Professional Workers vs Unemployment Rate', fontsize=15)
plt.xlabel('Percentage of Professional Workers (%)', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.savefig('unemployment_vs_professional_scatter.png')
plt.show()

# d) Analyze relationship between Unemployment Rate and people who work from home
df_cleaned['WorkAtHomePercentage'] = (df_cleaned['WorkAtHome'] / df_cleaned['TotalPop']) * 100
correlation_unemployment_work_at_home = df_cleaned['UnemploymentRate'].corr(df_cleaned['WorkAtHomePercentage'])
print(f"Correlation between Unemployment Rate and Work At Home Percentage: {correlation_unemployment_work_at_home}")

# Create scatter plot: Work From Home Percentage vs Unemployment Rate
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['WorkAtHomePercentage'], df_cleaned['UnemploymentRate'], color='blue', alpha=0.5)
plt.title('Work From Home Percentage vs Unemployment Rate', fontsize=15)
plt.xlabel('Work From Home Percentage (%)', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.savefig('unemployment_vs_work_from_home_scatter.png')
plt.show()

#QUESTION 8
df = pd.read_csv("censusdata/acs2015_census_tract_data.csv")

# Create the scatter plot with a trend line
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.regplot(x='Poverty', y='Unemployment', data=df, scatter_kws={'alpha':0.5})
plt.title('Poverty vs Unemployment')
plt.xlabel('Poverty Rate')
plt.ylabel('Unemployment Rate')

# Save the plot
plt.savefig('poverty_unemployment_scatter.png')
plt.close()

print("Scatter plot saved as 'poverty_unemployment_scatter.png'")

# Calculate the correlation coefficient
correlation = df['Poverty'].corr(df['Unemployment'])
print(f"Correlation between Poverty and Unemployment: {correlation:.4f}")

#question 9
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("censusdata/acs2015_census_tract_data.csv")

# Create income quantiles
df['Income_Quantile'] = pd.qcut(df['Income'], q=5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

# Calculate average percentages for each transportation method by income quintile
transport_cols = ['Drive', 'Transit', 'Walk', 'WorkAtHome']
transport_means = df.groupby('Income_Quantile')[transport_cols].mean()

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))

bottom = np.zeros(5)
for col in transport_cols:
    ax.bar(transport_means.index, transport_means[col], bottom=bottom, label=col)
    bottom += transport_means[col]

ax.set_title('Transportation Methods by Income Quantile')
ax.set_xlabel('Income Quantile')
ax.set_ylabel('Percentage')
ax.legend(title='Transportation Method')

# Add percentage labels on the bars
for i, quantile in enumerate(transport_means.index):
    total = 0
    for col in transport_cols:
        value = transport_means.loc[quantile, col]
        ax.text(i, total + value/2, f'{value:.1f}%', ha='center', va='center')
        total += value

plt.tight_layout()
plt.savefig('transportation_by_income.png')
plt.close()

print("Stacked bar chart saved as 'transportation_by_income.png'")

# Print the data for each quantile
print(transport_means)

#question10
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("censusdata/acs2015_census_tract_data.csv")

# Create the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Poverty', y='ChildPoverty', data=df, alpha=0.5)
plt.title('Overall Poverty vs Child Poverty')
plt.xlabel('Overall Poverty Rate (%)')
plt.ylabel('Child Poverty Rate (%)')

# Add a diagonal line for reference
plt.plot([0, 100], [0, 100], linestyle='--', color='red', alpha=0.5)

# Save the plot
plt.savefig('poverty_comparison.png')
plt.close()

print("Scatter plot saved as 'poverty_comparison.png'")

# Calculate the correlation
correlation = df['Poverty'].corr(df['ChildPoverty'])
print(f"Correlation between Overall Poverty and Child Poverty: {correlation:.4f}")

# Identify outliers or interesting cases
df['Poverty_Diff'] = df['ChildPoverty'] - df['Poverty']
interesting_cases = df[abs(df['Poverty_Diff']) > 20].sort_values('Poverty_Diff', ascending=False)
print("\nInteresting cases (where child poverty differs significantly from overall poverty):")
print(interesting_cases[['State', 'County', 'Poverty', 'ChildPoverty', 'Poverty_Diff']].head())
