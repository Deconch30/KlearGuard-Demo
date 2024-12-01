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

    # Simple data privacy check
    sensitive_detected = "@" in email
    compliance_status = "Pass" if not sensitive_detected else "Fail"

    # Simple bias detection
    sentiment = analyzer.polarity_scores(text)
    bias_detected = sentiment['compound'] < -0.1

    return jsonify({
        "compliance_status": compliance_status,
        "bias_detected": bias_detected,
        "sentiment_score": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
