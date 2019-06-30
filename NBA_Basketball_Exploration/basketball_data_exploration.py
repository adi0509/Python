
# This code explores the NBA players from 2013 - 2014 basketball season, and uses
# a machine learning algorithm called kMeans to group them in clusters, this will
# show which players are most similar

#Stat Glossaries: https://www.basketball-reference.com/about/glossary.html
#                 https://stats.nba.com/help/glossary/#fta

#Resource: https://www.dataquest.io/blog/python-vs-r/

#import the dependencies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load the data 
#from google.colab import files #Only use for Google Colab
#uploaded = files.upload()      #Only use for Google Colab
nba = pd.read_csv('nba_2013.csv')# the nba_2013.csv data contains data on NBA players from 2013 - 2014 season
nba.head(7)# Print the first 7 rows of data or first 7 players

#Get the number of rows and columns (481 rows or players , and 31 columns containing data on the players)
nba.shape

# Find the average value for each numeric column / feature
nba.mean() # The columns have names like 'fg' (field goals made), 'ast'(assists), here is a glossary of all of the stats https://stats.nba.com/help/glossary/

#Get the mean / average of specific columns
# mean of the specific column
nba.loc[:,"fg"].mean()

#Make pairwise scatter plots
# This is a common way to explore a data set to see how different columns correlate
# to others, we'll compare ast (assits), fg(field goals), trb (total rebound )
#NOTE: pairplot of all columns ==> sns.pairplot(nba)
sns.pairplot(nba[["ast", "fg", "trb"]])
plt.show()

#Make Heat Maps to see correlations
#Note: Heat Map of all columns ==> sns.heatmap(nba.corr())
#Note: Heat Map of all columns with annotation/numbers ==> sns.heatmap(nba.corr(), annot=True)
#Heat Map of the columns ast (assits), fg(field goals), trb (total rebound ) with annotation
correlation = nba[["ast", "fg", "trb"]].corr()
sns.heatmap(correlation, annot=True)

# Make clusters of the players using a machine learning model called kMeans
#One good way to explore this kind of data is to generate cluster plots.
#This will show which players are most similar.

from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=5, random_state=1)# Create a 5 cluster kmeans model
good_columns = nba._get_numeric_data().dropna(axis=1)#remove any non-numeric columns, or columns with missing values (NA, Nan, etc).
kmeans_model.fit(good_columns)# Train the model
labels = kmeans_model.labels_ # Get the labels or (cluster label for each player)
labels

#Plot players by cluster
#We can now plot out the players by cluster to discover patterns. 
#One way to do this is to first use PCA to make our data 2-dimensional, 
#then plot it, and shade each point according to cluster association

#NOTE: PCA Principal component analysis (PCA) is a statistical procedure that uses an orthogonal transformation to convert a set of 
#observations of possibly correlated variables (entities each of which takes on various numerical values) into a set of values of linearly 
#uncorrelated variables called principal components. A Dimensionality Reducing Algorithm

from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
plt.show()

#Show plot points
plot_columns

#Find the 'good columns' data for the player LeBron James
#again by 'good columns' I mean with only numeric values, and no missing values (NA, Nan, etc).

# Find player LeBron
LeBron = good_columns.loc[ nba['player'] == 'LeBron James',: ]

#Find player Durant
Durant = good_columns.loc[ nba['player'] == 'Kevin Durant',: ]

#print the players
print(LeBron)
print(Durant)

#Change the dataframe to a list Lebron to be able to use the kmeans model to make predictions/grouping
Lebron_list = LeBron.values.tolist()
Durant_list = Durant.values.tolist()

#Predict which group LeBron James and Kevin Durant belongs
LeBron_Cluster_Label = kmeans_model.predict(Lebron_list)
Durant_Cluster_Label = kmeans_model.predict(Durant_list)

print(LeBron_Cluster_Label)
print(Durant_Cluster_Label)

# Look at all of the column coorelations
nba.corr() #Note there is a positive coorelation between minutes played(mp) and points(pts)

# Let’s say we want to predict number of assists per player from field goals made per player.
#Split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(nba[['fg']], nba[['ast']], test_size=0.2, random_state=42)

#Create the Linear Regression Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression() # Create the model
lr.fit(x_train, y_train) #Train the model
predictions = lr.predict(x_test) #Make predictions on the test data

print(predictions)
print(y_test)

# Testing Model: Score returns the coefficient of determination R^2 of the prediction. 
# The best possible score is 1.0 (58.78% of the variance for assists is explained by the field goals players made)
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# mean squared error which tells you how close a regression line is to a set of points.
from sklearn.metrics import mean_squared_error
print("Mean Squared Error (MSE): ",mean_squared_error(y_test, predictions))
