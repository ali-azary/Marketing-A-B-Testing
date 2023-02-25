# plot the probability density function of the posterior distributions for the "ad" and "psa" groups to visualize the shape of the distributions
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import beta
import numpy as np

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

# Create a range of values for the x-axis
x = np.linspace(0, 1, 1000)

# Plot the probability density functions of the posterior distributions
plt.plot(x, ad_posterior.pdf(x), label="Ad")
plt.plot(x, psa_posterior.pdf(x), label="PSA")
plt.xlim(.0,.05)
plt.title("Posterior Distributions of Conversion Rates")
plt.xlabel("Conversion Rate")
plt.ylabel("Probability Density")
plt.legend()
plt.savefig('pdf.jpg')
