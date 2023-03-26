# -*- coding: utf-8 -*-
"""knn_pr.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ycKhOeaoUdJWrcQm1EpIXLEa_N7rp6qn
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

from google.colab import files
up=files.upload()

ds = pd.read_csv("diabetes.csv")
print(len(ds))
print(ds.head())

zero_not_accepted = ['Glucose','BloodPressure','SkinThickness','BMI','Insulin']

for column in zero_not_accepted:
   ds[column]=ds[column].replace(0,np.NaN)
   mean = int(ds[column].mean(skipna=True))
   ds[column]=ds[column].replace(np.NaN,mean)

print(ds['Glucose'])

#split dataset
x = ds.iloc[:,0:8]
y = ds.iloc[:,8]
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0,test_size = 0.2)

#feature scaling
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors = 11,p=2,metric = 'euclidean')

classifier.fit(x_train,y_train)

import math
math.sqrt(len(y_test))

y_pred = classifier.predict(x_test)
y_pred

cm = confusion_matrix(y_test,y_pred)
print(cm)

print(f1_score(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.show()
