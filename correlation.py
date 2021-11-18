import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import seaborn as sns


nba = pd.read_csv('2012_nba_draft_combine.csv') # using panda to read the csv file


wingspan=nba['Wingspan'] # setting my columns to variables such as wingspan and height
height=nba['Height (With Shoes)']



plt.style.use('fivethirtyeight')      #changing my style of plot to look nicer    
plt.scatter(height,wingspan)  #scatter plot of my column

m,b=np.polyfit(height,wingspan,1)    #polynomial fit of my plot for line of best fit
plt.plot(height, m*height+b,color="red")


plt.xlabel("Height in Inches")
plt.ylabel("Wingspan in Inches")   #labelling my plot to tell what the plot is showing
plt.title("Wingspan and Height Correlation")


r,p= stats.pearsonr(height,wingspan)  #pearson correlation coefficient 
print("pearson correlation coefficient r:", r)
print("pearson probability p:", p)

f,b= stats.spearmanr(height, wingspan) # spearman's correlation coefficient
print("spearman correlation coefficient r:", f)
print("spearman probability p:", b)

