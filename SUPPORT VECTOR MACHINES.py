# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:51:30 2020

@author: NARAYANA REDDY DATA SCIENTIST
"""


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# IMPORTING THE DATASET
dataset=pd.read_csv('Social_Network_Ads.csv')

# DIVIDE THE DATASET INTO X AND Y
x=dataset.iloc[:,[2,3]]
y=dataset.iloc[:,4]

# Splitting dataset into training and test dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

#BUILD YHE SVM MODEL
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(x_train,y_train)
# PREDICT THE MODEL
y_predict=classifier.predict(x_test)

#CONFUSION MATRIX FOR MODEL PERFORMANCE

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predict)


# Visualising support vector machines

from matplotlib.colors import ListedColormap
x_set,y_set=x_test,y_test
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                  np.arange(start=x_set[:,1].min()-1,stop=x_set[:,0].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i),label=j)
plt.title('Support Vector Machines graph')
plt.xlabel('Age')
plt.ylabel('Estimated salary')
plt.legend()
plt.show()


