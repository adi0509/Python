# Import the libraries
from random import randint
from sklearn.linear_model import LinearRegression
import numpy as np

# Create a range limit for random numbers in the training set, and a count of the number of rows in the training set
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

# Create an empty numpy array of shape (TRAIN_SET_COUNT, 3) for the input training set 'X' and create an empty numpy array for the output for each training set 'y'
TRAIN_INPUT = np.empty((TRAIN_SET_COUNT, 3))
TRAIN_OUTPUT = np.empty(TRAIN_SET_COUNT)

#Create and append a randomly generated data set to the input and output
for i in range(TRAIN_SET_COUNT):
    a, b, c = randint(0, TRAIN_SET_LIMIT), randint(0, TRAIN_SET_LIMIT), randint(0, TRAIN_SET_LIMIT)
    #Create a linear function for the output dataset 'y'
    op = (10*a) + (2*b) + (3*c)
    TRAIN_INPUT[i] = [a, b, c]
    TRAIN_OUTPUT[i] = op

predictor = LinearRegression(n_jobs=-1) #Create a linear regression object with all processors
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)  #fit the linear model (approximate a target function)

X_TEST = np.array([[10, 20, 30]]) #Create our testing data set, the ouput should be 10*10 + 2*20 + 3*30 = 230
outcome = predictor.predict(X=X_TEST) # Predict the output of the test data using the linear model

coefficients = predictor.coef_  #The estimated coefficients for the linear regression problem.

print(f"Outcome: {outcome} \nCoefficients: {coefficients}")
