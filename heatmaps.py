# heatmaps for conversion by days and hours
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('marketing_AB.csv')

# Convert 'most ads day' to categorical data type and specify order of weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['most ads day'] = pd.Categorical(df['most ads day'], categories=weekday_order, ordered=True)

# Create pivot table with counts of conversions by most ads day and most ads hour for each group
ad_df = df[df['test group'] == 'ad']
ad_pivot_df = ad_df.pivot_table(index=['most ads day', 'most ads hour'], columns='test group', values='converted', aggfunc='sum')

psa_df = df[df['test group'] == 'psa']
psa_pivot_df = psa_df.pivot_table(index=['most ads day', 'most ads hour'], columns='test group', values='converted', aggfunc='sum')

# Create heatmap for AD group
plt.figure(figsize=(10, 8))
sns.heatmap(ad_pivot_df, cmap='coolwarm', annot=False, fmt='g', linewidths=0.5, cbar_kws={'label': 'Number of Conversions'})
plt.title('Number of Conversions by Most Ads Day and Most Ads Hour for AD Group')
plt.xlabel('Test Group')
plt.ylabel('Most Ads Day and Hour')
plt.tight_layout()
plt.savefig('ad-heatmap.jpg')

# Create heatmap for PSA group
plt.figure(figsize=(10, 8))
sns.heatmap(psa_pivot_df, cmap='coolwarm', annot=False, fmt='g', linewidths=0.5, cbar_kws={'label': 'Number of Conversions'})
plt.title('Number of Conversions by Most Ads Day and Most Ads Hour for PSA Group')
plt.xlabel('Test Group')
plt.ylabel('Most Ads Day and Hour')
plt.tight_layout()
plt.savefig('psa-heatmap.jpg')

