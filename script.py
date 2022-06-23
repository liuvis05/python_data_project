import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

#2. Read csv
pd.read_csv('charcters_stats.csv')

#3. Show first records from csv
df = pd.read_csv('charcters_stats.csv')
df.head()

#4. Show number of rows and columns
df.shape
 
# Cleaning Empty Cells
new_df = df.dropna()
df.dropna(inplace = True)
print(new_df.to_string())

#5. You need to find the values of alignment ,can use value_counts()
df['Alignment'].value_counts().to_frame()

#6. Find out only good alignment holders superheroes
df.loc[df['Alignment'] == 'good']

#7. Show first five records which you found in point 6
df.loc[df['Alignment'] == 'good'].head(5)

#8. Show top five records having top speed of heroes of good alignment
df.loc[df['Alignment'] == 'good'].nlargest(5,'Speed')

#9. Show 5 records of super heroes who have maximum power of good alignment
df.loc[df['Alignment'] == 'good'].nlargest(5,'Power')

#10. Find out how many super heroes are there with power 100 of good alignment
super_heros=df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'good'].Power.value_counts()[100]
print(f"There are {super_heros} super heros with power 100 of good alignment")

#11. Shape them what you got in point 10
df.loc[(df['Alignment'] == 'good') & (df['Power'] == 100)].shape

#12. Show all records from point 10
df.loc[(df['Alignment'] == 'good') & (df['Power'] == 100)]

#13. Retrieve total of first five records of max power of good alignment super heroes
df.loc[df['Alignment'] == 'good'].nlargest(5,'Total')


#14. Draw a bar plot of all super heroes who are having good alignment and max power of top five only , 
#take same object of point 13 , 
#show name and total in plot with green bars

max_powers=df.loc[df['Alignment'] == 'good'].nlargest(5,'Total')


plt.bar(max_powers['Name'],max_powers['Total'], color='green')
plt.title('Top 5 ', fontsize=16)
plt.xlabel('Name', fontsize=16)
plt.ylabel('Total', fontsize=16)
plt.show()

#####extra
max_powers=df.loc[df['Alignment'] == 'good'].nlargest(5,'Speed')


plt.bar(max_powers['Name'],max_powers['Speed'], color='blue')
plt.title('Top 5 ', fontsize=16)
plt.xlabel('Name', fontsize=16)
plt.ylabel('Speed', fontsize=16)
plt.show()

#####Extra 
max_powers=df.loc[df['Alignment'] == 'good'].nlargest(5,'Power')


plt.bar(max_powers['Name'],max_powers['Power'], color='red')
plt.title('Top 5 ', fontsize=16)
plt.xlabel('Name', fontsize=16)
plt.ylabel('Power', fontsize=16)
plt.show()


#15. Extract villains having bad alignment
df.loc[df['Alignment'] == 'bad']

#16. Show first five records of point 15
df.loc[df['Alignment'] == 'bad'].head(5)

#17. Show top five fastest super villains in terms of super speed
df.loc[df['Alignment'] == 'bad'].nlargest(5,'Speed')

#####extras
#Intelligence	Strength	Speed	Durability	Power	Combat	Total
villians=df[["Speed"]].loc[df['Alignment'] == 'bad'].head()

ax = villians.plot(
    #style="ro--",
    title="Villians",
    xlabel="Total",
    ylabel="Speed",
)

#18. Top five super villains in terms of intelligence
df.loc[df['Alignment'] == 'bad'].nlargest(5,'Intelligence')

#19. Show who is most dangerous super villain after calculating their total (top 5 only)
df.loc[df['Alignment'] == 'bad'].nlargest(5,'Total')

#20. Draw a histogram for speed of super heroes having fig size 10,5 , 
#provide speed in histogram for only good alignment super heroes ,title should be "distribution of speed" , xlabel should be "speed"

heroes=df[["Alignment","Speed"]].loc[df['Alignment'] == 'good']

heroes.plot(kind='hist',
        #alpha=0.7,
        #bins=30,
        title='Distribution Of Speed',
        rot=45,
        grid=True,
        figsize=(10,5),
        fontsize=15, 
        color=['#A0E8AF'])
plt.xlabel('Speed')
plt.ylabel("Heros");

#21. Draw a histogram for combat of super villains having fig size 10,5 , 
#provide combat in histogram for only bad alignment super heroes ,title should be "distribution of combat" ,xlabel should be "combat" *** 

villians=df[["Name","Alignment","Combat"]].loc[df['Alignment'] == 'bad']

villians.plot(kind='hist',
        title='Distribution Of Combat',
        rot=45,
        grid=True,
        figsize=(10,5),
        fontsize=15, 
        color=['#FFCF56'])
plt.xlabel('Combat')
plt.ylabel("Villains");

#Name	Alignment	Intelligence	Strength	Speed	Durability	Power	Combat	Total
df.hist(figsize=(15, 10), color='pink')

villians=df[["Speed"]].loc[df['Alignment'] == 'bad']
villians.plot.hist(y='Speed', figsize=(10, 5), color='yellow')
plt.show()

#Intelligence	Strength	Speed	Durability	Power	Combat	Total
df[["Name", "Intelligence","Strength","Power","Speed","Durability","Combat"]].loc[df['Alignment'] == 'bad'].nlargest(5,'Durability')

#Intelligence	Strength	Speed	Durability	Power	Combat	Total
durability=df[["Intelligence","Strength","Power","Speed","Durability","Combat"]].loc[df['Alignment'] == 'bad'].nlargest(5,'Durability')
durability.plot.barh(figsize=(15, 10))

durability=df[["Intelligence","Strength","Power","Speed","Durability","Combat"]].loc[df['Alignment'] == 'bad'].head()
durability.plot.area()
