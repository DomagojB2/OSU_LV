import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score

data = pd.read_csv('LV4/data_C02_emission.csv')

X = data[['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'Fuel Consumption Comb (mpg)']]
y = data['CO2 Emissions (g/km)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

plt.scatter(X_train['Fuel Consumption Comb (L/100km)'], y_train, color = 'blue', label = 'Training data')
plt.scatter(X_test['Fuel Consumption Comb (L/100km)'], y_test, color = 'red', label = 'Testing data')
plt.xlabel('Fuel Consumption Comb (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.legend()
plt.show()

plt.hist(X_train['Fuel Consumption City (L/100km)'], color = 'green')
plt.title('Fuel Consumption City (L/100km) before scalling')
plt.show()

sc = MinMaxScaler()
X_train_s = sc.fit_transform(X_train)
X_train_s = pd.DataFrame(X_train_s, columns = X_train.columns)
X_test_s = sc.transform(X_test)
X_test_s = pd.DataFrame(X_test_s, columns = X_test.columns)

plt.hist(X_train_s['Fuel Consumption City (L/100km)'], color = 'red')
plt.title('Fuel Consumption City (L/100km) after scalling')
plt.show()

linearModel = lm.LinearRegression()
linearModel.fit(X_train_s, y_train)
print('Coefficients of the linear model', linearModel.coef_)

y_test_p = linearModel.predict(X_test_s)
plt.scatter(X_test_s['Fuel Consumption City (L/100km)'], y_test, color = 'blue', label = 'Real values')
plt.scatter(X_test_s['Fuel Consumption City (L/100km)'], y_test_p, color = 'red', label = 'Predicted values')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.legend()
plt.show()

MAE = mean_absolute_error(y_test, y_test_p)
print('Mean absolute error: ', MAE)
MSE = mean_squared_error(y_test, y_test_p)
print('Mean squared error: ', MSE)
RMSE = math.sqrt(MSE)
print('Root mean squared error: ', RMSE)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
print('Mean absolute percentage error: ', MAPE)
R2 = r2_score(y_test, y_test_p)
print('R2 score: ', R2)
