# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import json
import requests

# Load Dataset
dataset = pd.read_csv('heart.csv')

# Selecting Features
X = dataset.iloc[:, :-1]

# Selecting Target
y = dataset.iloc[:, -1]

# Printing Features And Target names
# print('Features :' , X)
# print('Target :', y)

# Printing Shapes
print(X.shape)
print(y.shape)

# Splitting Training and testing Data
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
train_X = sc_X.fit_transform(train_X)
test_X = sc_X.transform(test_X)
sc_y = StandardScaler()
train_y = sc_y.fit_transform(train_y)

# KNeighborsClassifier Training Model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(train_X, train_y)

# Predicting value from test set
test_prediction = knn.predict(test_X)

# Accuracy Score
from sklearn import metrics
print("AUC score: {:.5f}".format(metrics.accuracy_score(test_y, test_prediction)))  # OUTPUT: AUC score: 0.81319
print("MAE score: {:.5f}".format(metrics.mean_absolute_error(test_y, test_prediction)))  # OUTPUT: MAE score: 0.18681

# Plotting best K value for KNN
v = []
k_range = list(range(1,50))
for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    # fit the model with training data
    knn.fit(train_X, train_y)
    pred = knn.predict(test_X)
    # adding all accuracy result to list
    v.append(metrics.accuracy_score(test_y, pred))

plt.plot(k_range, v, c='orange')
plt.show()


# Training model with best K value
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(train_X, train_y)
test_prediction = knn.predict(test_X)

# Dumping file to pickle to make python instances
pickle.dump(knn, open('model.pkl', 'wb'))

print("AUC score: {:.5f}".format(metrics.accuracy_score(test_y, test_prediction)))  # OUTPUT: AUC score: 0.86813
print("MAE score: {:.5f}".format(metrics.mean_absolute_error(test_y, test_prediction)))  # OUTPUT: MAE score: 0.13187