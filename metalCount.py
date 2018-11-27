import csv
import numpy as np
import matplotlib.pyplot as plt 

golds = []
silvers = []
bronzes = []

categories = [] # arrays stores data

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0: # row_count 0 is the data titles, we don't want it in our data set so we store it in the categories
            categories.append(row) # categories is empty were appending it to row_count 0 
            line_count += 1 # next time this runs increase the number so it dosen't read the catorgies
        else:
            if row[7] == "Gold":
                golds.append(row[7])
            elif row[7] == "Silver":
                silvers.append(row[7])
            else:
                bronzes.append(row[7])
        line_count  += 1

print('processed', line_count, 'rows of data')
print('gold metals won:', len(golds))
print('silver metals won:', len(silvers))
print('bronze metals won:', len(bronzes))

# getting a percent
pct_gold = len(golds) / line_count * 100
pct_silver = len(silvers) / line_count * 100
pct_bronze = len(bronzes) / line_count * 100


# making the pie chart
labels = "Gold", "Silver", "Gold"
sizes = [pct_gold, pct_silver, pct_bronze]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct= '%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title('Metals By Color')
plt.show()
