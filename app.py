from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "")
    email = data.get("email", "")

    # Introduce bias based on specific keywords or categories
    biased_words = {
        "positive_bias": ["amazing", "great", "wonderful", "success"],
        "negative_bias": ["failure", "problem", "awful", "terrible"]
    }

    # Check for biased keywords in the text
    if any(word in text.lower() for word in biased_words["positive_bias"]):
        sentiment = {
            "positive": 0.9,
            "neutral": 0.1,
            "negative": 0.0,
            "compound": 0.9
        }
        bias_detected = True
    elif any(word in text.lower() for word in biased_words["negative_bias"]):
        sentiment = {
            "positive": 0.0,
            "neutral": 0.1,
            "negative": 0.9,
            "compound": -0.9
        }
        bias_detected = True
    else:
        # Perform actual sentiment analysis
        sentiment = analyzer.polarity_scores(text)
        bias_detected = sentiment['compound'] < -0.1

    # Simple data privacy check
    sensitive_detected = "@" in email
    compliance_status = "Pass" if not sensitive_detected else "Fail"

    return jsonify({
        "compliance_status": compliance_status,
        "bias_detected": bias_detected,
        "sentiment_score": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
