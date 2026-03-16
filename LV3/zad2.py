import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('LV3/data_C02_emission.csv')
plt.figure()
plt.hist(data['CO2 Emissions (g/km)'], bins = 30)
plt.title('Emisija CO2 plinova')
plt.show()

fuels = {'X':'blue', 'Z':'yellow', 'D':'green', 'E':'red', 'N':'purple'}
for fuel_type, color in fuels.items():
    subset = data[data['Fuel Type'] == fuel_type]
    plt.scatter(subset['Fuel Consumption City (L/100km)'], subset['CO2 Emissions (g/km)'],
                color=color, label=fuel_type)
plt.legend(title='Fuel Type')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.show()

data.boxplot(column = 'Fuel Consumption Hwy (L/100km)', by = 'Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Fuel Consumption Hwy (L/100km)')
plt.show()

cars_groupedbyfuel = data.groupby('Fuel Type').size()
cars_groupedbyfuel.plot(kind='bar', color = 'blue')
plt.xlabel('Tip goriva')
plt.ylabel('Broj vozila')
plt.show()

cars_bycylinders=data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cars_bycylinders.plot(kind='bar',color='blue')
plt.xlabel('Broj cilindara')
plt.ylabel('CO2 emisija')
plt.show()
