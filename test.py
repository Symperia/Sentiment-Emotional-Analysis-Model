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
file_path = C:\Users\silym\Downloads\Angel_export.csv

# conversations
conversations = parsing.parse(file_path)
conversations = conversations[2]
sentiment = sentiment_analysis(conversations)
emotion = emotion_analysis(conversations)

print(sentiment)
print(emotion)







begin=time.time()

# metric initialization
stats = {"Simple": 0, "Complex": 0}

# model loading
sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
emotion_analysis = pipeline("emotion-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion")

# set file path
file_path = input("Input file path as raw string.")

# conversations
conversations = parsing.parse(file_path)
conversations = conversations[2]
sentiment = sentiment_analysis(conversations)
emotion = emotion_analysis(conversations)

print(sentiment)
print(emotion)



    # 5. Your Contradiction Heuristic Engine
    is_complex = False
    category = "Simple"

    # Define blatant contradictions
    if sentiment == "positive" and emotion in ["sadness", "anger", "fear"]:
        is_complex = True
        category = "Bittersweet or Suppressed"
    elif sentiment == "negative" and emotion in ["joy"]:
        is_complex = True
        category = "Irony / Sarcasm"
    elif sentiment == "neutral" and emotion in ["anger", "joy", "sadness"]:
        is_complex = True
        category = "Suppression / Ambiguous"

    # Update counts
    if is_complex:
        stats["Complex"] += 1
    else:
        stats["Simple"] += 1

    print(f"\nText: \"{text}\"")
    print(f"-> Sentiment: {sentiment.upper()} | Emotion: {emotion.upper()}")
    print(f"-> Classification: {category.upper()}")
# 6. Generate the Metrics Chart