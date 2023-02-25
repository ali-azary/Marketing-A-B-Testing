# create histograms of the posterior distributions for the "ad" and "psa" groups to visualize the uncertainty in the estimates
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import beta

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

# Create histograms of the posterior distributions
plt.hist(ad_posterior.rvs(10000), bins=50, alpha=0.5, label="Ad")
plt.hist(psa_posterior.rvs(10000), bins=50, alpha=0.5, label="PSA")
plt.title("Posterior Distributions of Conversion Rates")
plt.xlabel("Conversion Rate")
plt.ylabel("Frequency")
plt.legend()
plt.savefig('distribution.jpg')
