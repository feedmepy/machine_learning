import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


companies = pd.read_csv("csv\\Forbes.csv")
X = companies.iloc[:, :-1].values
y = companies.iloc[:, 4].values

# using pandas to show the heat man
sns.heatmap(companies.corr())
print(X[0])

labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])

onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]
print(X[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(y_pred)

print(regressor.coef_)
print(regressor.intercept_)

r2_score(y_test, y_pred)