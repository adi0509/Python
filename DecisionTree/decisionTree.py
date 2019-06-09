#This program uses the Machine Learning Algorithm called a Decision Tree to classify a car as 
#'unacceptable', 'accepted', 'good', or 'very good'
# The classification is based off of other features/attributes like the cars 
#'buying price', 'maintenance price', 'number of doors', 'number of passengers that fit in the car', 'size of luggage capacity', and 'safety'


# The original dataset is the car evaluation dataset from http://archive.ics.uci.edu/ml/datasets/Car+Evaluation,
# more specifically it is a .data file originally and you can download it from http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data
# We will classify the quality or values column of the car, after switching all of the values from the original dataset to integers
# except for our dependent variable 'values' column which I've already done and have a file for, the new data set.
# The new dataset with the integer values is called 'car_integer_exceptY.csv'
# Get the 'car_integer_exceptY.csv' dataset  here: https://github.com/randerson112358/Python/blob/master/DecisionTree/car_integer_exceptY.csv

# Each attribute/feature described below:
# buying (buying price): vhigh (4), high (3), med (2), low (1)
# main (maintenance price): vhigh (4), high (3), med (2), low (1)
# doors (number of doors): 2, 3, 4, 5-more (5)
# persons (number of passengers fit in a car): 2, 4, more (6)
# lug_boot (size of luggage capacity): small (1), med (2), big (3)
# safety: low (1), med (2), high (3)
# values: unacc = unaccepted, acc = accepted, good = good, vgood = very good

# How did I create the new data set ?
# By doing the following for every attribute / feature / column in the original data set (except 'values')
# The following is only one example for the column buying. Note: there are other ways to convert the categorical data to integers
#data.buying[ data.buying == 'low'] = 1
#data.buying[ data.buying == 'med'] = 2
#data.buying[ data.buying == 'high'] = 3
#data.buying[ data.buying == 'vhigh'] = 4

#read more: https://medium.com/machine-learning-guy/using-decision-tree-method-for-car-selection-problem-5272675451f9

# Import the dependencies / libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#Create a dataframe from the cars dataset / csv file
df = pd.read_csv('DataSets/Cars/car_integer_exceptY.csv')

#print the first 5 rows of the data set
print(df.head())

# Split your data into the independent variable(s) and dependent variable
X_train = df.loc[:,'buying':'safety'] #Gets all the rows in the dataset from column 'buying' to column 'safety'
Y_train = df.loc[:,'values'] #Gets all of the rows in the dataset from column 'values'

# The actual decision tree classifier
tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)

# Train the model
tree.fit(X_train, Y_train)

# Make your prediction
# input:buying=v-high, main=high, doors=2, persons=2, lug_boot=med, safety=3
# integer conversion of input: 4,3,2,2,2,3
prediction = tree.predict([[4,3,2,2,2,3]])

#Print the prediction
print('Printing the prediction: ')
print(prediction)
