import pandas as pd
import matplotlib.pyplot as plt

nba = pd.read_csv('2012_nba_draft_combine.csv') # using panda to read the csv file


# adding different columns together to create a new column
nba['Best Defender'] = (nba['Height (With Shoes)'] +
                        nba['Wingspan'] +
                        nba['Vertical (Max)'] +
                        nba['Standing reach']-
                        nba['Agility']
                        )


bd=nba['Best Defender'] 
playerno=nba['List']    #setting my variable to columns
players=nba['Player'] 


plt.style.use('seaborn')    #using style of seaborn              
plt.scatter(nba['List'], nba['Best Defender'],s=25) #scatter the plot for player and new column


for x,y in zip(playerno,bd):  # this loop is for labelling the player list for each point
    
    label= format(x)
    
    plt.annotate(label,
                 (x,y),
                 textcoords="offset points",
                 xytext=(0,4),  # distance between the point and the number label
                 ha='center')

print("player 0 is :",players[0]) #checking who is the best defender which is player 0

plt.xlabel("Player List")
plt.ylabel("Defensive Rating") #labelling my plot
plt.title("Best Defender by Physique")

