from transformers import pipeline
import numpy as np
import time
import parsing
import heuristic_label_sorting

begin=time.time()

# metric initialization
stats = {"Simple": 0, "Complex": 0}

# model loading
sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
emotion_analysis = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

# set file path
file_path = input("Input file path as raw string.")

# conversations
conversations = parsing.parse(file_path)
conversations = conversations[3]
sentiment = sentiment_analysis(conversations, truncation=True, max_length=512)
emotion = emotion_analysis(conversations, truncation=True, max_length=512)

dominant_sentiment = sentiment[0]['label']
dominant_emotion = emotion[0][0]['label']
#emotion significance and sentiment clarity
emotion_values=[]
for i in range(6):
    emotion_values.append(emotion[0][i]['score'])
if np.std(emotion_values) > 0.15:
    emotional_significance = True
else:
     emotional_significance = False

if emotion[0][0]['score'] > 0.25:
    sentiment_clarity = True
else:
    sentiment_clarity = False
#sorting
if not sentiment_clarity and not emotional_significance:
    label = 'ambiguous'
if sentiment_clarity and not emotional_significance:
    label = heuristic_label_sorting.complex_label(dominant_sentiment, dominant_emotion)
if not sentiment_clarity and emotional_significance:
    label = heuristic_label_sorting.complex_label(dominant_sentiment, dominant_emotion)
if sentiment_clarity and emotional_significance:
    label = heuristic_label_sorting.complex_label(dominant_sentiment, dominant_emotion)

print(sentiment)
print(emotion)
print(label)