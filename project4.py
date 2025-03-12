import pandas as pd
from matplotlib import pyplot as plt
import vizLibrary as viz

file = 'seasonal-temp-anomaly-us.csv'
df = pd.read_csv(file)

winter = df[df["Entity"] == 'Winter']
summer = df[df["Entity"] == 'Summer']
spring = df[df["Entity"] == 'Spring']
fall = df[df["Entity"] == 'Fall']

plt.figure(figsize=(15,10))

def subplot(number, season,sname):
    plt.subplot(2,2,number)
    plt.scatter(season['Year'], season['Temperature anomaly'])
    plt.plot(season['Year'], season['Temperature anomaly (smoothed)'])
    plt.ylim(-6,6)
    plt.grid(True)
    viz.makeChartManual('Year', 'Temp Anomaly (C)', 'Temp Anomaly ('+sname+')')

subplot(1,winter,'winter')
subplot(2,summer,'summer')
subplot(3,spring,'spring')
subplot(4,fall,'fall')

plt.tight_layout()
plt.show()
