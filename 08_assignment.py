# -*- coding: utf-8 -*-
"""08_assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xtixhj3NuTCnn99h2wjMbbTJu9mhppbG
"""



"""<a href="https://colab.research.google.com/github/data602sps/assignments/blob/master/05_assignment.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# **Assignment 8**

# **Weeks 10 & 11- matplotlib & seaborn**
* In this homework assignment, you will explore and analyze a public dataset of your choosing. Since this assignment is “open-ended” in nature, you are free to expand upon the requirements below. However, you must meet the minimum requirments as indicated in each section.


* The preferred method for this analysis is in a .ipynb file. Feel free to use whichever platform of your choosing.  


### **Some data examples:**
•	https://www.data.gov/

•	https://opendata.cityofnewyork.us/

•	https://datasetsearch.research.google.com/

•	https://archive.ics.uci.edu/ml/index.php

### **Resources:**

•	https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

•	https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html

•	https://www.data-to-viz.com/



### **Headings or comments**
**You are required to make use of comments, or headings for each section.  You must explain what your code is doing, and the results of running your code.**  Act as if you were giving this assignment to your manager - you must include clear and descriptive information for each section.

### **You may work as a group or indivdually on this assignment.**

# Introduction

In this section, please describe the dataset you are using.  Include a link to the source of this data.  You should also provide some explanation on why you choose this dataset.

______________
# Data Exploration
Import your dataset into your .ipynb, create dataframes, and explore your data.  

Include:

* Summary statistics means, medians, quartiles,
* Missing value information
* Any other relevant information about the dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('https://raw.githubusercontent.com/Jennyjjxxzz/Data602_Assignment_08/refs/heads/main/weather.csv')
print(df.head())

df.rename(columns={'visib': 'visible'},inplace=True)
print(df)

"""# Data Wrangling

Perform data wrangling.  You are free to use your best judgment here.  If you are stuck, look at previous assignment.

Check and change structure of the data.
"""

print(df.dtypes)

df['month']= df['month'].astype('Int64')
df['day']= df['day'].astype('Int64')
df['hour']= df['hour'].astype('Int64')

"""Remove or fill the na value with median."""

missing_values = df.isnull()
print(missing_values)

df ['pressure'] = df['pressure'].fillna(df['pressure'].median())

df['wind_dir'] = df['wind_dir'].fillna(df['wind_dir'].median())

df['pressure'] = df['pressure'].fillna(df['pressure'].median())

df = df.dropna(subset=['temp'])

df.drop(columns=['Unnamed: 0'], inplace=True)

df = df[df['wind_speed'] >= 0]
print(df)

"""Reate new columns based on existing columns or calculations."""

df['feels_like_temp'] = df['temp'] - ((100 - df['humid']) / 5)
print(df)

"""# Visualizations

The main purpose of this assignment is to practice creating various visualizations using the matplotlib and seaborn library.

### **Part 1:**
Using matplotlib, create ***two or more plots*** that incorporate at least **5** of the following properties:

Note: these properties vary based on your data.  The goal is to practice creating visualizations and modifying its properties.

*   Use and change a legend position
*   Change a legend font size
*   Place a legend outside of the plot
*   Create a single legend for all subplots
*   Change the title and x/y labels
*   Change the marker, line colors, and line width
*   Add annotations
*   Modify Axis Text Ticks/Labels
*   Change size of axis Labels
*   Your own choice not included above


Plots that you can create **include**:

*   Scatter Plot
*   Bar plot
*   Line Chart
*   Multi Plots (e.g. using .subplot()
*   Histogram

You can add another plot not listed here if it works better for your data.  This is not a complete list of plots to create.

### **Part 2:**

Recreate the visualizations above using the Seaborn library as best as possible.  


**You are required to explain what each of your plots is representing. Plots without comments will not be accepted.**  In addition, please explain the properties you are showcasing.


### **Part 3:**
In a comment or text box, explain the differences between creating a plot in matplotlib and seaborn, based on your above plots.

##Part 1:
1.Bar Chart - Average Wind Speed by Origin
"""

origin_wind_speed = df.groupby('origin')['wind_speed'].mean().reset_index()
plt.bar(origin_wind_speed.origin, origin_wind_speed.wind_speed, color='orange', label='Avg Wind Speed by Origin')
plt.xlabel('Origin')
plt.ylabel('Wind Speed (mph)')
plt.title('Average Wind Speed by Origin', fontsize=16)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.show()

"""2.Line Chart - Average Temperature by Hour"""

avg_temp_by_hour = df.groupby('hour')['feels_like_temp'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(avg_temp_by_hour.hour, avg_temp_by_hour.feels_like_temp, marker='o', linestyle='-', linewidth=2, color='blue', label='Avg Temp')
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Feels Like Temperature (°F)', fontsize=12)
plt.title('Average Feels Like Temperature by Hour', fontsize=16)

plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

"""##Part2:
1.Bar Chart - Average Wind Speed by Origin(By using Seaborn). The origin:JFK got average high wind speed than other origins.
"""

origin_wind_speed = df.groupby('origin')['wind_speed'].mean().reset_index()
sns.barplot(data=origin_wind_speed, x= 'origin', y= 'wind_speed', hue= "origin")

plt.xlabel('Origin', fontsize=12)
plt.ylabel('Wind Speed (mph)', fontsize=12)
plt.title('Average Wind Speed by Origin (Seaborn)', fontsize=16)

plt.show()

"""2. Line Chart- Average Tempearature (By using Seaborn). The plot shows the temperature during the afternoon feels like temperature is lower than during evening."""

avg_temp_by_hour = df.groupby('hour')['feels_like_temp'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=avg_temp_by_hour, x='hour', y='feels_like_temp', marker='o', color='orange', label='Avg Temp')

plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Feels Like Temperature (°F)', fontsize=12)
plt.title('Average Feels Like Temperature by Hour', fontsize=16)

plt.show()

"""# Conclusions  

After working with both Matplotlib and Seaborn, I found that Seaborn requires less code and allows for quicker creation of visualizations. However, Matplotlib offers flexibility for creating more complex and highly customized plots.
"""