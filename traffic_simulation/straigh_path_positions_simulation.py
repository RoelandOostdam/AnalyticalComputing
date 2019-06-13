import matplotlib.pyplot as plt
import pandas as pd

# Data uitlezen
data = pd.read_csv("verkeerssimulatie-rechteweg-posities.csv",
                   sep=";",
                   names = ["time", "car1", "car2"])
timeDF = data["time"]  # Maximale en minimale waardes voor scale
data.head()

# Posities van de auto's in verloop van tijd
plt.plot('time', 'car1', data=data, label="Auto 1")
plt.plot('time', 'car2', data=data, label="Auto 2")

plt.title('Positie van de auto\'s in verloop van tijd')
plt.ylabel('Positie op rechte weg (m?)')
plt.xlabel('Tijd (s)')
plt.xlim((min(timeDF), max(timeDF)))
plt.ylim(-50, 500)
plt.legend(loc="upper left")

plt.show()


# Snelheden van auto's
dataframe = pd.DataFrame(data)
dataframeDiff = dataframe[['car1','car2']].diff(axis=0)
dataframeSpeed = pd.concat([dataframe[['time']], dataframeDiff], axis=1)

print(dataframeSpeed)
plt.plot('time', 'car1', data=dataframeSpeed, label="Auto 1")
plt.plot('time', 'car2', data=dataframeSpeed, label="Auto 2")

plt.title("Snelheid van auto's in verloop van tijd")
plt.ylabel("Snelheid (km/u)")
plt.xlabel('Tijd (s)')
plt.xlim((min(timeDF), max(timeDF)))
plt.legend(loc="upper left")

plt.show()

# Minimale/Maximale snelheid
def calcMinMaxSpeed(dataframe, minMax):
    speed = dataframe.max() if minMax else dataframe.min()
    output = "Maximale snelheid" if minMax else "Minimale snelheid"
    print(f"{output} {dataframe.columns[1]}: {speed[1] * 10:.3f} m/s")

calcMinMaxSpeed(dataframeSpeed[['time','car1']], False)
calcMinMaxSpeed(dataframeSpeed[['time','car1']], True)
calcMinMaxSpeed(dataframeSpeed[['time','car2']], False)
calcMinMaxSpeed(dataframeSpeed[['time','car2']], True)