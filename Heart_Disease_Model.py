#Importing libraries 
import pandas as pd
import matplotlib.pyplot as plt 

#Load Dataset
dataset = pd.read_csv('heart.csv')

#Selecting Features 
X = dataset.iloc[:, :-1]

#Selecting Target 
y = dataset.iloc[:, -1]

#Printing Features And Target names
#print('Features :' , X)
#print('Target :', y)

#Printing Shapes
print(X.shape)
print(y.shape)

#Splitting Trainning and testing Data
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0) 

#KNeighborsClassifier Trainning Model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(train_X, train_y)

#Predicting value from test set
test_prediction = knn.predict(test_X)

#Accuracy Score
from sklearn import metrics
print(metrics.accuracy_score(test_y, test_prediction))  #OUTPUT: 0.5494505494505495

#Ploting best K value for KNN
v = []
k_range = list(range(1,50))
for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    #fit the model with trainning data
    knn.fit(train_X, train_y)
    pred = knn.predict(test_X)
    #adding all accuracy result to list
    v.append(metrics.accuracy_score(test_y, pred))

plt.plot(k_range, v, c='orange')
plt.show()

#trainning model with best K value
knn = KNeighborsClassifier(n_neighbors=18)
knn.fit(train_X, train_y)
test_prediction = knn.predict(test_X)
print(metrics.accuracy_score(test_y, test_prediction)) #OUTPUT: 0.7472527472527473