# Diamonds

'''
Diamonds are available in various shapes, the more common shapes are shown below.
 All shapes have different types of facets which reflect the light.
 For example the round brilliant, cushions, radiant, oval, pear, marquise,
 heart and princess cut diamonds have small facets (underneath) giving them more sparkle where as the emerald,
 baguette and the asscher cut diamond facets are longer giving a more subtle sparkle.
 The most popular is the round brilliant and has been for many years. As it has the highest demand the rounds are more expensive than other shapes.
 Also it has the most amount of waste when it is cut from the rough stone. S
 hapes such as the baguettes and trilliants tend to be accent stones in a setting with one of the other shaped stones.
 And this is one of several pieces of information about diamonds and our jeweler needs to find specifications of the most expensive diamonds.

'''

### Diamonds – Description of data

'''

| Column Name                               | Summary                                        |
|------------------------------------------:|-----------------------------------------------------------------|
|`Price`                                    | price in US dollars (\$326--\$18,823)|
|`Carat`                                  | weight of the diamond (0.2--5.01)|
|`Cut`                                       | quality of the cut (Fair, Good, Very Good, Premium, Ideal)|
|`Color`                                      | diamond colour, from J (worst) to D (best)|
|`Clarity`                                    | a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))|
|`X`                                          | length in mm (0--10.74)|
|`Y`                                          | width in mm (0--58.9)|
|`Z`                                          |depth in mm (0--31.8)|
|`Depth`                                      | total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)|
|`Table`                                      | width of top of diamond relative to widest point (43--95)-
'''
# ADVANCED FUNCTIONAL EXPLORATORY DATA ANALYSIS `(EDA)`

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv('V:\DATALENT\Diamonds\Diamonds\diamonds.csv')
df


def explore_dataframe(df):
    # Display the first 5 rows of the dataframe
    print("\n############## HEAD #############")
    print(df.head())

    # Display the last 5 rows of the dataframe
    print("\n############## TAIL #############")
    print(df.tail())

    # Display the shape of the dataframe
    print("\n############## SHAPE #############")
    print(df.shape)

    # Display information about the dataframe
    print("\n############## INFO #############")
    print(df.info())

    # Display the columns of the dataframe
    print("\n############## COLUMNS #############")
    print(df.columns)

    # Display the index of the dataframe
    print("\n############## INDEX #############")
    print(df.index)

    print("\n############## NUNIQUE #############")
    print(df.nunique())

    # Display the summary statistics of the dataframe
    print("\n############## DESCRIBE #############")
    print(df.describe().T)

    # Check if there are any missing values in the dataframe
    print("\n############## ISNULL/VALUES #############")
    print(df.isnull().values.any())

    # Count the number of missing values in each column of the dataframe
    print("\n############## ISNULL/SUM #############")
    print(df.isnull().sum())


# Call the function to explore the dataframe
explore_dataframe(df)

# Sort the dataframe by the 'price' column in descending order
most_expensive_diamonds = df.sort_values(by='price', ascending=False)

# Display the top 5 most expensive diamonds
most_expensive_diamonds.head()

# Example: Filtering diamonds with premium cut quality
premium_diamonds = df[df['cut'] == 'Premium']

# Show filtered data
print(premium_diamonds.head())

# Example: Examine the cut quality, colour, clarity, etc. of the most expensive diamonds
print(most_expensive_diamonds[['cut', 'color', 'clarity']])

# Creating a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='carat', y='price', data=df)
plt.title('Price Scatter Plot by Carat')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='cut', y='price', data=df, order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
plt.title('Price Breakdown by Cutting Quality')
plt.xlabel('Cutting Quality')
plt.ylabel('Price (USD)')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="price", kde=True)
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

cut_price_relationship = df.groupby('cut')['price'].mean().sort_values(ascending=False)
print(cut_price_relationship)

# Scatter Plot for Colour and Clarity Analysis
plt.figure(figsize=(12, 6))
sns.scatterplot(x='color', y='price', hue='clarity', data=df)
plt.title('Colour and Clarity Analysis - Price Relationship')
plt.xlabel('Color')
plt.ylabel('Price (USD)')
plt.show()

# Boxplot for Colour and Clarity Analysis
plt.figure(figsize=(12, 6))
sns.boxplot(x='color', y='price', hue='clarity', data=df, order=['D', 'E', 'F', 'G', 'H', 'I', 'J'])
plt.title('Colour and Clarity Analysis - Price Breakdown')
plt.xlabel('Color')
plt.ylabel('Price (USD)')
plt.show()

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix Between Features')
plt.show()

# Visualising outliers with boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='cut', y='price', data=df)
plt.title('Outliers - Cutting Quality and Price')
plt.xlabel('Cutting Quality')
plt.ylabel('Price (USD)')
plt.show()

# Filter outliers over a certain threshold value
outlier_values = df[df['price'] > 15000] # An example threshold value, you can use any value you want
print(outlier_values)

# Special analysis: The relationship between the clarity of diamonds of a particular colour and price
special_analysis = df[df['color'] == 'D'].groupby('clarity')['price'].mean().sort_values(ascending=False)
print(special_analysis)

