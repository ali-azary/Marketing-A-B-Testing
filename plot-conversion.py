# create a bar plot to compare the conversion rates for the "ad" and "psa" groups.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("marketing_AB.csv")

# Compute the conversion rates for the ad and psa groups
ad_conversions = data.loc[data["test group"] == "ad", "converted"]
ad_rate = ad_conversions.mean()

psa_conversions = data.loc[data["test group"] == "psa", "converted"]
psa_rate = psa_conversions.mean()

# Create a bar plot
plt.bar(["Ad", "PSA"], [ad_rate, psa_rate])
plt.title("Conversion Rates by Test Group")
plt.xlabel("Test Group")
plt.ylabel("Conversion Rate")
plt.savefig('conversion-bar.jpg')
