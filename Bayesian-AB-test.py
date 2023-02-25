import pandas as pd
from scipy.stats import bernoulli, beta
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("marketing_AB.csv")

# Convert the boolean values in the 'converted' column to binary values (0 or 1)
data["converted"] = data["converted"].astype(int)

# Compute the conversion rates for the ad and psa groups
ad_conversions = data.loc[data["test group"] == "ad", "converted"]
ad_rate = ad_conversions.mean()

psa_conversions = data.loc[data["test group"] == "psa", "converted"]
psa_rate = psa_conversions.mean()

# Set the hyperparameters for the beta prior distribution
a = 2
b = 2

# Compute the posterior distributions using Bayesian updating
ad_posterior = beta(a + ad_conversions.sum(), b + len(ad_conversions) - ad_conversions.sum())
psa_posterior = beta(a + psa_conversions.sum(), b + len(psa_conversions) - psa_conversions.sum())

# Compute the posterior means and credible intervals
ad_mean = ad_posterior.mean()
psa_mean = psa_posterior.mean()

ad_ci = ad_posterior.interval(0.95)
ad_ci = (round(ad_ci[0],4),round(ad_ci[1],4))
psa_ci = psa_posterior.interval(0.95)
psa_ci = (round(psa_ci[0],4),round(psa_ci[1],4))

# Print the results
print("Conversion rate for ad group:", ad_rate)
print("Conversion rate for psa group:", psa_rate)
print("Posterior mean for ad group:", ad_mean)
print("Posterior mean for psa group:", psa_mean)
print("95% credible interval for ad group:", ad_ci)
print("95% credible interval for psa group:", psa_ci)

# Create a dictionary with the data
data = {'Group': ['Ad', 'PSA'],
        'Conversion Rate': [ad_rate, psa_rate],
        'Posterior Mean': [ad_mean, psa_mean],
        '95% Credible Interval': [ad_ci, psa_ci]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Set the 'Group' column as the index
df.set_index('Group', inplace=True)

# Plot the DataFrame as a table
fig, ax = plt.subplots()
ax.axis('off')
ax.axis('tight')
table=ax.table(cellText=df.round(4).values, colLabels=df.columns, rowLabels=df.index, loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
# Save the table as a JPG image
plt.savefig('table.jpg')
