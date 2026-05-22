from transformers import pipeline
import numpy as np
import time
import parsing

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

#emotion standard deviation
emotion_values=[]
for i in range(6):
    emotion_values.append(emotion[i]['label'])

if np.std(emotion_values)>0.15:
    emotional_significance = True
else:
     emotional_significance = False




print(sentiment)
print(emotion)
