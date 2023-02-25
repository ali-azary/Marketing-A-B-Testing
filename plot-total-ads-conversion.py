# make a bar plot of the conversion rates by the total number of ads seen for each group, with a trend line overlaid for each group
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv("marketing_AB.csv")

# Compute the conversion rates by total ads seen for each group
ad_conversion_rates = data.loc[data["test group"] == "ad"].groupby("total ads")["converted"].mean()
psa_conversion_rates = data.loc[data["test group"] == "psa"].groupby("total ads")["converted"].mean()

# Create a bar plot of the conversion rates by total ads seen
plt.bar(ad_conversion_rates.index, ad_conversion_rates.values, label="Ad")
plt.bar(psa_conversion_rates.index, psa_conversion_rates.values, label="PSA")

# Add a trend line to the bar plot
ad_trend = np.poly1d(np.polyfit(ad_conversion_rates.index, ad_conversion_rates.values, 1))
psa_trend = np.poly1d(np.polyfit(psa_conversion_rates.index, psa_conversion_rates.values, 1))
plt.plot(ad_conversion_rates.index, ad_trend(ad_conversion_rates.index), linestyle="--", color="blue", label="Ad Trend")
plt.plot(psa_conversion_rates.index, psa_trend(psa_conversion_rates.index), linestyle="--", color="orange", label="PSA Trend")

plt.title("Conversion Rates by Total Ads Seen")
plt.xlabel("Total Ads Seen")
plt.ylabel("Conversion Rate")
plt.legend()
plt.savefig('ads-seen-conversion.jpg')

