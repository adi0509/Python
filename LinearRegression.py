# Import the libraries
from random import randint
from sklearn.linear_model import LinearRegression

# Create a range limit for random numbers in the training set, and a count of the number of rows in the training set
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100


# Create an empty list of the input training set 'X' and create an empty list of the output for each training set 'Y'
TRAIN_INPUT = list()
TRAIN_OUTPUT= list()

#Create and append a randomly generated data set to the input and output
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    #Create a linear function for the output dataset 'Y'
    op = (10*a) + (2*b) + (3*c)
    TRAIN_INPUT.append([a,b,c])
    TRAIN_OUTPUT.append(op)

predictor = LinearRegression(n_jobs=-1) #Create a linear regression object NOTE n_jobs = the number of jobs to use for computation, -1 means use all processors
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)  #fit the linear model (approximate a target function)

X_TEST = [[10,20,30]] #Create our testing data set, the ouput should be 10*10 + 2*20 + 3*30 = 230
outcome = predictor.predict(X=X_TEST) # Predict the ouput of the test data using the linear model

coefficients = predictor.coef_  #The estimated coefficients for the linear regression problem.

print('Outcome: {} \n Coefficients: {}'.format(outcome, coefficients))
