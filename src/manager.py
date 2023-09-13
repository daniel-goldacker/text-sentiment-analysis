from flask import Flask, request, jsonify
from transformers import pipeline
from config import ConfigParameters

app = Flask(__name__)

# Inicialize o pipeline de análise de sentimento
nlp = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Star Mapping to Sentiment Categories
sentimentMapping = ConfigParameters.SENTIMENT_MAPPING

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data['text']
        
        # Performs sentiment analysis using the BERT model
        results = nlp(text)
        sentimentStar = results[0]['label']
        
        # Map star rating to sentiment category
        sentiment = sentimentMapping.get(sentimentStar, "unknown")
        
        # Returns the result in JSON format
        result = {
            "text": text,
            "sentiment": sentiment
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
