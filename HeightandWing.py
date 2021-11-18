import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


nba = pd.read_csv('2012_nba_draft_combine.csv') # using panda to read the csv file


wingspan=nba['Wingspan'] #setting my columns to different variable
height=nba['Height (With Shoes)']
listplayer=nba['List']


plt.style.use('ggplot')   # setting the style to ggplot from matploblib
              
plt.plot(wingspan,'o-',ms=4,label="Wingspan") # plot my wingspan with marksize 4

plt.plot(height,'bo-',ms=4,label="Height") # same principle from wingspan for height



plt.xlabel("Player List")  #labelling my plot including the legends
plt.ylabel("Length in inches")
plt.title("Wingspan and Height")

plt.legend()