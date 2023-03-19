#pip install TextBlob

#import TextBlob

from textblob import TextBlob

def calculate_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

if __name__ == "__main__":
    text = input("Enter the text: ")
    try:
        sentiment = calculate_sentiment(text)
        print(f"Sentiment: {sentiment:.2f}")
    except Exception as e:
        print(f"Error: {e}")
