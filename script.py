import pandas as pd
import csv
import matplotlib.pyplot as plt

#2. Read csv
df = pd.read_csv('charcters_stats.csv')
print(df.to_string())

#3. Show first records from csv
print(df.head())

#4. Show number of rows and columns
print(df.info())
 
# Cleaning Empty Cells
new_df = df.dropna()
df.dropna(inplace = True)
print(new_df.to_string())

#5. You need to find the values of alignment ,can use value_counts()
df['Alignment'].value_counts().to_frame()

#6. Find out only good alignment holders superheroes
df['Alignment'].value_counts().to_frame().loc['good']

#7. Show first five records which you found in point 6
df[["Name","Alignment"]].loc[df['Alignment'] == 'good'].head(5)

#8. Show top five records having top speed of heroes of good alignment
df[["Name","Alignment","Speed"]].loc[df['Alignment'] == 'good'].nlargest(5,'Speed')

#9. Show 5 records of super heroes who have maximum power of good alignment
df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'good'].nlargest(5,'Power')

#10. Find out how many super heroes are there with power 100 of good alignment
super_heros=df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'good'].Power.value_counts()[100]
print(f"There are {super_heros} super heros with power 100 of good alignment")

###################11. Shape them what you got in point 10


#12. Show all records from point 10
df.loc[(df['Alignment'] == 'good') & (df['Power'] == 100)]

#13. Retrieve total of first five records of max power of good alignment super heroes
# Show 5 records of super heroes who have maximum power of good alignment(same???????)
df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'good'].nlargest(5,'Power')


##################14. Draw a bar plot of all super heroes who are having good alignment and max power of top five only , 
#take same object of point 13 , 
#show name and total in plot with green bars

max_powers=df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'good'].nlargest(5,'Power')
#print(max_powers)


plt.bar([max_powers,'Name'],max_powers,['Alignment'], color='green')
plt.title('Top 10 Countries and Number of Players', fontsize=16)
plt.xlabel('Country', fontsize=16)
plt.ylabel('Number of Players', fontsize=16)
plt.grid(True)
plt.show()

#15. Extract villains having bad alignment
df[["Name","Alignment"]].loc[df['Alignment'] == 'bad']

#16. Show first five records of point 15
df[["Name","Alignment"]].loc[df['Alignment'] == 'bad'].head(5)

#17. Show top five fastest super villains in terms of super speed
df[["Name","Alignment","Speed"]].loc[df['Alignment'] == 'bad'].nlargest(5,'Speed')

#18. Top five super villains in terms of intelligence
df[["Name","Alignment","Intelligence"]].loc[df['Alignment'] == 'bad'].nlargest(5,'Intelligence')

#19. Show who is most dangerous super villain after calculating their total (top 5 only)
df[["Name","Alignment","Total"]].loc[df['Alignment'] == 'bad'].nlargest(5,'Total')

#20. Draw a histogram for speed of super heroes having fig size 10,5 , 
#provide speed in histogram for only good alignment super heroes ,title should be "distribution of speed" , xlabel should be "speed"

heroes=df[["Name","Alignment","Speed"]].loc[df['Alignment'] == 'good'].nlargest(33,'Speed')
# df.hist(column='Speed');

heroes.plot(kind='hist',
        alpha=0.7,
        bins=30,
        title='Histogram Of Speed',
        rot=45,
        grid=True,
        figsize=(10,5),
        fontsize=15, 
        color=['#A0E8AF'])#color=['#A0E8AF', '#FFCF56'])
plt.xlabel('Speed')
plt.ylabel("Distribution of speed");

#21. Draw a histogram for combat of super villains having fig size 10,5 , 
#provide combat in histogram for only bad alignment super heroes ,title should be "distribution of combat" ,xlabel should be "combat" *** 

super_heros=df[["Name","Alignment","Power"]].loc[df['Alignment'] == 'bad'].Power.value_counts()[100]

print(f"There are {super_heros} super heros with power 100 of bad alignment")

villians=df[["Name","Alignment","Total"]].loc[df['Alignment'] == 'bad'].nlargest(20,'Total')

villians.plot(kind='hist',
        alpha=0.7,
        bins=30,
        title='Histogram Of Combat',
        rot=45,
        grid=True,
        figsize=(10,5),
        fontsize=15, 
        color=['#FFCF56'])#color=['#A0E8AF', '#FFCF56'])
plt.xlabel('Combat')
plt.ylabel("Distribution of combat");
