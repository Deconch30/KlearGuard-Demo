from flask import Flask
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to KlearGuard AI!"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Your sentiment analysis logic here
    return "Sentiment analysis results"

if __name__ == "__main__":
    # Get the port from the environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
