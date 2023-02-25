# Marketing-A-B-Testing
Marketing A/B Testing

data from https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing?resource=download

Marketing A/B testing dataset
Marketing companies want to run successful campaigns, but the market is complex and several options can work. So normally they tun A/B tests, that is a randomized experimentation process wherein two or more versions of a variable (web page, page element, banner, etc.) are shown to different segments of people at the same time to determine which version leaves the maximum impact and drive business metrics.

The companies are interested in answering two questions:

Would the campaign be successful?
If the campaign was successful, how much of that success could be attributed to the ads?
With the second question in mind, we normally do an A/B test. The majority of the people will be exposed to ads (the experimental group). And a small portion of people (the control group) would instead see a Public Service Announcement (PSA) (or nothing) in the exact size and place the ad would normally be.

The idea of the dataset is to analyze the groups, find if the ads were successful, how much the company can make from the ads, and if the difference between the groups is statistically significant.

Data dictionary:

Index: Row index
user id: User ID (unique)
test group: If "ad" the person saw the advertisement, if "psa" they only saw the public service announcement
converted: If a person bought the product then True, else is False
total ads: Amount of ads seen by person
most ads day: Day that the person saw the biggest amount of ads
most ads hour: Hour of day that the person saw the biggest amount of ads

Bayesian test is done and conversion rates, trends, and ads hors and days have been analyzed.

![table](https://user-images.githubusercontent.com/69943289/221383667-a5558ffe-29b2-4554-b696-ab69a2e066fe.jpg)
![ad-heatmap](https://user-images.githubusercontent.com/69943289/221383684-1b8429ac-8bbd-4f5d-a2ff-551aeebbffe1.jpg)
![ads-seen-conversion](https://user-images.githubusercontent.com/69943289/221383686-2e464579-8fe0-4c2a-ac29-d74acc2f8b68.jpg)
![conversion-bar](https://user-images.githubusercontent.com/69943289/221383688-295b986d-d403-4766-92e0-8d5599b65cfb.jpg)
![days](https://user-images.githubusercontent.com/69943289/221383691-6907b33b-f06b-4e6e-8a9b-355cedb3e916.jpg)
![distribution](https://user-images.githubusercontent.com/69943289/221383693-a0602cd9-13bc-4ea9-a4d5-3b18a67d390b.jpg)
![hours](https://user-images.githubusercontent.com/69943289/221383694-09f58eda-84b0-46af-897d-3b3741e5f5e3.jpg)
![pdf](https://user-images.githubusercontent.com/69943289/221383695-a9a26e3e-93be-4cec-9dc0-bf4aa37ccc1b.jpg)
![psa-heatmap](https://user-images.githubusercontent.com/69943289/221383696-01ea3e66-ac7d-433b-91e5-ae254b5239f3.jpg)
