# create a bar plot of the conversion rates by the most common day for each group
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv("marketing_AB.csv")

# Compute the conversion rates by most ads day for each group
ad_conversion_rates = data.loc[data["test group"] == "ad"].groupby("most ads day")["converted"].mean()
psa_conversion_rates = data.loc[data["test group"] == "psa"].groupby("most ads day")["converted"].mean()

# Create a bar plot of the conversion rates by most ads day
plt.bar(ad_conversion_rates.index, ad_conversion_rates.values, label="Ad")
plt.bar(psa_conversion_rates.index, psa_conversion_rates.values, label="PSA")
plt.title("Conversion Rates by Most Ads Day")
plt.xlabel("Most Ads Day")
plt.ylabel("Conversion Rate")
plt.legend()
plt.savefig('days.jpg')
