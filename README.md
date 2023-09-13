# text-sentiment-analysis

This code creates a simple web API that allows users to submit text for sentiment analysis and returns a sentiment category (Excellent, Good, Neutral, Bad or Terrible) based on a BERT model. To run it, follow the steps below:

1. Place in directory **./src**:
```sh
cd src
```
2. Install additional libraries:
```sh
pip install -r requirements.txt
```
3. Run the integration:
```sh
run manager.py
```
4. Execute command:
```sh
curl --location 'http://127.0.0.1:5000/sentiment' \
--header 'Content-Type: application/json' \
--data '{
    "text": "This text is excellent."
}   '
```

