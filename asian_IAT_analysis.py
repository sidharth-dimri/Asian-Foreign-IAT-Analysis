import geopandas
import geodatasets
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import pandas as pd

#methods

#find average asian american sentiment in entire dataset
def findavg(csvFile):
    index = 0;
    avg = 0
    for x in csvFile['D_biep.White_American_all']:
        index = index + 1
        avg = avg + x

    avg = avg/index
    #to put it into percentage
    avg = avg*100
    avg = round(avg, 2)
    return avg

#method to find the average in a state
def avginstate(state, csvFile):
    index = 0;
    avg = 0;
    for x in csvFile["STATE"]:
        if(x==state):
            index = index + 1

    for x in range(len(csvFile)):
        if(csvFile.iloc[x, 'D_biep.White_American_all']==state):
            avg = avg + csvFile.iloc[x, 17]

    avg = avg/index
    return avg
        

#Load US Map
states = geopandas.read_file('usa.shx')
type(states)
#mercator projection
states = states.to_crs("EPSG:3395")
#remove nonstates
states = states.drop(2)
states = states.drop(7)
states = states.drop(36)
states = states.drop(43)
states = states.drop(51)
states = states.drop(53)
states = states.drop(54)
states = states.drop(55)
states = states.drop(56)
states.reset_index(drop=True, inplace=True)



#organizing states in geopandas by name
states = states.sort_values(by='NAME')
#custom colormap
blue_to_red = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#0000ff", "#fefefe", "#ff0000"])

#read in dataset
csv2019 = pd.read_csv('Asian_IAT.public.2019.csv')
csv2021 = pd.read_csv('Asian_IAT.public.2021.csv')

"""
D_biep.White_American_all is the correct label

positive seems to be european american, while negative seems to be
asian american association

values are from -1 to 1 with -1 being strongly asian, 1 being strongly white
and 0 being neither

there are some values with more than 1, but we will discredit those because
if you look at the latency times, they are way off. 900 latency
times for one side and then 2000 for the other is a large discrepancy. Discredit those and focus on the others
cuz no way those ones are valid
"""

#drop nans
csv2019.dropna(subset=['D_biep.White_American_all'], inplace=True)
csv2019.dropna(subset=['STATE'], inplace=True)
csv2021.dropna(subset=['D_biep.White_American_all'], inplace=True)
csv2021.dropna(subset=['STATE'], inplace=True)


#calculating average asian sentiment in 2019
avg2019 = findavg(csv2019)
if(avg2019>0):
    print(f"America on average in 2019 considered asians less american than europeans, and did so by {avg2019}%")

elif(avg2019<0):
    print(f"America on average in 2019 considered asians more american than europeans, and did so by {avg2019}%")

else:
    print(f"America on average in 2019 considered asians and europeans equally american")

#in 2021
avg2021 = findavg(csv2021)
if(avg2021>0):
    print(f"America on average in 2021 considered asians less american than europeans, and did so by {avg2021}%")

elif(avg2021<0):
    print(f"America on average in 2021 considered asians more american than europeans, and did so by {avg2021}%")

else:
    print(f"America on average in 2021 considered asians and europeans equally american")

#percent change from 2019 to 2021
change19to21 = ((avg2021 - avg2019)/avg2021)*100
if change19to21 < 0:
    change19to21 = change19to21 - (2*change19to21)

change19to21 = round(change19to21,2)
print(f"percent change from 2019 to 2021 in asian perception was by {change19to21}%")

#collecting data by state 2019 (alphabetical order)
statelist = []
statelist.append(avginstate("Alabama", csv2019))
statelist.append(avginstate("Alaska", csv2019))
statelist.append(avginstate("Arizona", csv2019))
statelist.append(avginstate("Arkansas", csv2019))
statelist.append(avginstate("California", csv2019))
statelist.append(avginstate("Colorado", csv2019))
statelist.append(avginstate("Connecticut", csv2019))
statelist.append(avginstate("Delaware", csv2019))
statelist.append(avginstate("Florida", csv2019))
statelist.append(avginstate("Georgia", csv2019))
statelist.append(avginstate("Hawaii", csv2019))
statelist.append(avginstate("Idaho", csv2019))
statelist.append(avginstate("Illinois", csv2019))
statelist.append(avginstate("Indiana", csv2019))
statelist.append(avginstate("Iowa", csv2019))
statelist.append(avginstate("Kansas", csv2019))
statelist.append(avginstate("Kentucky", csv2019))
statelist.append(avginstate("Louisiana", csv2019))
statelist.append(avginstate("Maine", csv2019))
statelist.append(avginstate("Maryland", csv2019))
statelist.append(avginstate("Massachusetts", csv2019))
statelist.append(avginstate("Michigan", csv2019))
statelist.append(avginstate("Minnesota", csv2019))
statelist.append(avginstate("Mississippi", csv2019))
statelist.append(avginstate("Missouri", csv2019))
statelist.append(avginstate("Montana", csv2019))
statelist.append(avginstate("Nebraska", csv2019))
statelist.append(avginstate("Nevada", csv2019))
statelist.append(avginstate("New Hampshire", csv2019))
statelist.append(avginstate("New Jersey", csv2019))
statelist.append(avginstate("New Mexico", csv2019))
statelist.append(avginstate("New York", csv2019))
statelist.append(avginstate("North Carolina", csv2019))
statelist.append(avginstate("North Dakota", csv2019))
statelist.append(avginstate("Ohio", csv2019))
statelist.append(avginstate("Oklahoma", csv2019))
statelist.append(avginstate("Oregon", csv2019))
statelist.append(avginstate("Pennsylvania", csv2019))
statelist.append(avginstate("Rhode Island", csv2019))
statelist.append(avginstate("South Carolina", csv2019))
statelist.append(avginstate("South Dakota", csv2019))
statelist.append(avginstate("Tennessee", csv2019))
statelist.append(avginstate("Texas", csv2019))
statelist.append(avginstate("Utah", csv2019))
statelist.append(avginstate("Vermont", csv2019))
statelist.append(avginstate("Virginia", csv2019))
statelist.append(avginstate("Washington", csv2019))
statelist.append(avginstate("West Virginia", csv2019))
statelist.append(avginstate("Wisconsin", csv2019))
statelist.append(avginstate("Wyoming", csv2019))


statearr = np.array(statelist)
#changes a 1d array from a row to a column
#statearr = statearr.reshape(50, 1)


# Plot the map 2019
states.plot(column=statearr, cmap=blue_to_red, vmin=-1, vmax=1, legend=True)
plt.title("Asian-American sentiment in 2019")
plt.show()

#collecting data by state 2021 (alphabetical order)
statelist = []
statelist.append(avginstate("Alabama", csv2021))
statelist.append(avginstate("Alaska", csv2021))
statelist.append(avginstate("Arizona", csv2021))
statelist.append(avginstate("Arkansas", csv2021))
statelist.append(avginstate("California", csv2021))
statelist.append(avginstate("Colorado", csv2021))
statelist.append(avginstate("Connecticut", csv2021))
statelist.append(avginstate("Delaware", csv2021))
statelist.append(avginstate("Florida", csv2021))
statelist.append(avginstate("Georgia", csv2021))
statelist.append(avginstate("Hawaii", csv2021))
statelist.append(avginstate("Idaho", csv2021))
statelist.append(avginstate("Illinois", csv2021))
statelist.append(avginstate("Indiana", csv2021))
statelist.append(avginstate("Iowa", csv2021))
statelist.append(avginstate("Kansas", csv2021))
statelist.append(avginstate("Kentucky", csv2021))
statelist.append(avginstate("Louisiana", csv2021))
statelist.append(avginstate("Maine", csv2021))
statelist.append(avginstate("Maryland", csv2021))
statelist.append(avginstate("Massachusetts", csv2021))
statelist.append(avginstate("Michigan", csv2021))
statelist.append(avginstate("Minnesota", csv2021))
statelist.append(avginstate("Mississippi", csv2021))
statelist.append(avginstate("Missouri", csv2021))
statelist.append(avginstate("Montana", csv2021))
statelist.append(avginstate("Nebraska", csv2021))
statelist.append(avginstate("Nevada", csv2021))
statelist.append(avginstate("New Hampshire", csv2021))
statelist.append(avginstate("New Jersey", csv2021))
statelist.append(avginstate("New Mexico", csv2021))
statelist.append(avginstate("New York", csv2021))
statelist.append(avginstate("North Carolina", csv2021))
statelist.append(avginstate("North Dakota", csv2021))
statelist.append(avginstate("Ohio", csv2021))
statelist.append(avginstate("Oklahoma", csv2021))
statelist.append(avginstate("Oregon", csv2021))
statelist.append(avginstate("Pennsylvania", csv2021))
statelist.append(avginstate("Rhode Island", csv2021))
statelist.append(avginstate("South Carolina", csv2021))
statelist.append(avginstate("South Dakota", csv2021))
statelist.append(avginstate("Tennessee", csv2021))
statelist.append(avginstate("Texas", csv2021))
statelist.append(avginstate("Utah", csv2021))
statelist.append(avginstate("Vermont", csv2021))
statelist.append(avginstate("Virginia", csv2021))
statelist.append(avginstate("Washington", csv2021))
statelist.append(avginstate("West Virginia", csv2021))
statelist.append(avginstate("Wisconsin", csv2021))
statelist.append(avginstate("Wyoming", csv2021))


statearr = np.array(statelist)
#changes a 1d array from a row to a column
#statearr = statearr.reshape(50,1)


# Plot the map 2021
states.plot(column=statearr, cmap=blue_to_red, vmin=-1, vmax=1, legend=True)
plt.title("Asian-American sentiment in 2021")
plt.show()
