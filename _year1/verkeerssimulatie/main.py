import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Posities stuk
positions = pd.read_csv("verkeerssimulatie-rechteweg-posities.csv", sep=';')
positions.columns = ['time', 'car1', 'car2']

def speed(data):
	speeds = []
	for i in range(0,len(data)-1):
		speeds.append(abs(data[i+1] - data[i]))
	return speeds

speeds_car1 = speed(positions['car1'])
speeds_car2 = speed(positions['car2'])

print("Top speed car 1:", max(speeds_car1))
print("Top speed car 2:", max(speeds_car2))

plt.plot(positions['time'][1:], speeds_car1, label='Car 1')
plt.plot(positions['time'][1:], speeds_car2, label='Car 2')
plt.title("Car speeds over time")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.legend()
plt.show()

# Snelheden stuk
speeds = pd.read_csv("verkeerssimulatie-rechteweg-snelheden.csv", sep=';')
plt.plot(speeds)
