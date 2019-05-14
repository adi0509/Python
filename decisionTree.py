# For mathematical calculation
import numpy as np

# The original dataset is the car evaluation dataset from http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
# We will classify the quality or values column of the car, after switching all of the values
# except for our dependent variable 'values' column to integer values

# Each attribute described below:
# buying (buying price): v-high (4), high (3), med (2), low (1)
# main (maintenance price): v-high (4), high (3), med (2), low (1)
# door: 2, 3, 4, 5-more (5)
# persons (number of passengers fit in a car): 2, 4, more (6)
# lug_boot (size of luggage capacity): small (1), med (2), high (3)
# safety: low (1), med (2), high (3)
# unacc = unaccepted, acc = accepted, good = good, vgood = very good

#read more: https://medium.com/machine-learning-guy/using-decision-tree-method-for-car-selection-problem-5272675451f9

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

#Create a dataframe from the cars dataset / csv file
df = pd.read_csv('DataSets/Cars/car_integer_exceptY.csv')

#print the first 5 rows of the data set
print(df.head())

X_train = df.loc[:,'buying':'safety'] #Gets all the rows in the dataset from column 'buying' to column 'safety'
Y_train = df.loc[:,'values'] #Gets all of the rows in the dataset from column 'values'

# The actual decision tree classifier
tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)


tree.fit(X_train, Y_train)

#data.buying[ data.buying == 'low'] = 1
#data.buying[ data.buying == 'med'] = 2
#data.buying[ data.buying == 'high'] = 3
#data.buying[ data.buying == 'vhigh'] = 4
prediction = tree.predict([[4,3,2,1,2,3]])

print('Printing the prediction: ')
print(prediction)
