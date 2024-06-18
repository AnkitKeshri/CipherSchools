#Introduction to Matplotlib and Seaborn

#Matplotlib : Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
#It provides anobject-oriented API for embedding plots into applications using general-purpose GUI toolkits.


#Seaborn : Seaborn is a Python data visualization library based on Matplotlib.
#It provides a high-level interface for drawing attractive andinformative statistical graphics.


#Use Case in Real Life:

#Data Exploration: Create various plots to visualize data distributions and relationships between variables during the exploratory data analysis (EDA) phase.

#Statistical Analysis: Use visualizations to understand statistical properties of datasets, such as distribution plots, histograms, and pair plots to identify correlations and patterns.

#Business Reporting: Generate business reports with visualizations that provide insights into sales performance, customer behavior, and market trends.


pip install matplotlib #first install the matplotlib library
import matplotlib.pyplot as plt

#data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

#Creating a line plot
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylable('Y-axis')
plt.title('Simple Line Plot')
plt.show()












