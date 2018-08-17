#pip install TextBlob

#import TextBlob
from textblob import TextBlob

text = "Python is a very good language to learn"

obj = TextBlob(text)

#returns the sentiment of text
#by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity

print(sentiment)
