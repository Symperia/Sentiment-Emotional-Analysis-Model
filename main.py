from transformers import pipeline
import time
import parsing

begin=time.time()

# metric initialization
stats = {"Simple": 0, "Complex": 0}

# model loading
sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
emotion_analysis = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# set file path
file_path = input("Input file path as raw string.")

# conversations
conversations = parsing.parse(file_path)
conversations = conversations[3]
sentiment = sentiment_analysis(conversations, truncation=True, max_length=512)
emotion = emotion_analysis(conversations, truncation=True, max_length=512)

print(sentiment)
print(emotion)
