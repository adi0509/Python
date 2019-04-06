#import pandas library
import pandas as pd

#Create a file handler for our csv file in read mode
file_handler = open("car.csv", "r")

#Create a Pandas DataFrame using read_csv function that reads from a csv file
data = pd.read_csv(file_handler, sep=",")

#close file_handler
file_handler.close()

# traverse through the buying column of dataframe and write the values where conditions match
# buying values: low, med, high, vhigh

data.buying[ data.buying == 'low'] = 1
data.buying[ data.buying == 'med'] = 2
data.buying[ data.buying == 'high'] = 3
data.buying[ data.buying == 'vhigh'] = 4

#write the dataframe to a csv file
data.to_csv("car_example.csv")
