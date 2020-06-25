import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import combinations

# Posities stuk
df = pd.read_csv("verkeerssimulatie-rechteweg-snelheden.csv", sep=';')
df.columns = ['time', 'car1', 'car2', 'car3']

def calculate_positions(df, car):
    positions = None
    for i,x in df.iterrows():
        if positions == None:
            positions = [x[car]]
        else:
            if i>=600 and car == "car3":
                positions.append(positions[-1] - x[car])
            else:
                positions.append(positions[-1] + x[car])
    return positions

def detect_collisions(df, column1, column2):
    car1 = calculate_positions(df, column1)
    car2 = calculate_positions(df, column2)
    for x in range(2,len(car2)):
        if car2[x-1] >= car1[x] >= car2[x] or car2[x-1] <= car1[x] <= car2[x] or car1[x-1] >= car2[x] >= car1[x] or car1[x-1] <= car2[x] <= car1[x]:
            print("Collision at step {}, cars involved={}".format(x, (column1,column2)))

def detect_all_collisions(df, columns_names):
    combos = list(combinations(columns_names, 2))
    for combo in combos:
        detect_collisions(df,combo[0],combo[1])


detect_all_collisions(df,['car1','car2','car3'])

for car in ['car1','car2','car3']:
    plt.plot(df.time, calculate_positions(df, car), label=car)
plt.legend()
plt.show()