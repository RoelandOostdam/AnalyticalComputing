import matplotlib.pyplot as plt
import pandas as pd

# Data uitlezen
data = pd.read_csv("verkeerssimulatie-rechteweg-snelheden.csv",
                   sep=";",
                   names = ["time", "car1", "car2", "car3"])

timeDF = data['time'].iloc[1:]
startPositions = data.iloc[0]  # StartPositie van iedere auto
startPositions = startPositions.to_frame().T  # Series omzetten en transposen naar DataFrame
data.head()

# Snelheden van de auto's in verloop van tijd
plt.plot('time', 'car1', data=data, label="Auto 1")
plt.plot('time', 'car2', data=data, label="Auto 2")
plt.plot('time', 'car3', data=data, label="Auto 3")

plt.title('Snelheid van de auto\'s in verloop van tijd\n(m/s) geplot per miliseconde')
plt.ylabel('Snelheid (m/s)')
plt.xlabel('Tijd (s)')
plt.xlim(0, 10)
plt.ylim(0, 15)
plt.legend(loc="upper right")

plt.show()

# Afgelegde afstand per 0.1s optellen
dataCumSum = data.cumsum()
dataCumSum = dataCumSum[["car1", "car2", "car3"]]
dataCumSum = dataCumSum.multiply(0.1)  # van (m/s) naar (m/miliseconde)
dataCumSum = pd.concat([timeDF, dataCumSum], axis=1)

plt.plot('time', 'car1', data=dataCumSum, label="Auto 1")  # Plot de lijn van auto 1
plt.plot('time', 'car2', data=dataCumSum, label="Auto 2")  # Plot de lijn van auto 2
plt.plot('time', 'car3', data=dataCumSum, label="Auto 3")  # Plot de lijn van auto 3

plt.title('Afgelegde afstand van de auto\'s in verloop van tijd\n(m) geplot per miliseconde')
plt.ylabel('Afstand (m/miliseconde)')
plt.xlabel('Tijd (s)')
plt.xlim(0, 120)
plt.ylim(0, 1000)
plt.legend()

plt.show()

for x in range(1, dataCumSum.shape[0]):  # Telt de startpositie op bij de auto's waardoor
    # bijvoorbeeld auto 3 'achteraan' start maar door de hoge snelheid auto 1 inhaalt/botst
    dataCumSum.at[x, 'car1'] += startPositions['car1']
    dataCumSum.at[x, 'car2'] += startPositions['car2']
    dataCumSum.at[x, 'car3'] += startPositions['car3']

plt.plot('time', 'car1', data=dataCumSum, label="Auto 1")
plt.plot('time', 'car2', data=dataCumSum, label="Auto 2")
plt.plot('time', 'car3', data=dataCumSum, label="Auto 3")

plt.title('Afgelegde afstand van de auto\'s in verloop van tijd')
plt.ylabel('Afstand (m)')
plt.xlabel('Tijd (s)')
plt.xlim(0, 4)
plt.ylim(-10, 40)
plt.legend(loc = "upper left")
plt.show()