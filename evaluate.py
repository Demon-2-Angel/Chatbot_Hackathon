import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()

# Function to evaluate user input
def evaluate_user_response(user_input):
    evaluation = {
        "length_score": len(user_input) / 50,  # Normalize by max expected length
        "sentiment_score": sia.polarity_scores(user_input)["compound"],  # Sentiment analysis
        "negotiation_tone": "good" if "discount" in user_input.lower() else "needs improvement",
    }
    return evaluation
