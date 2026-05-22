def complex_label(dominant_sentiment, dominant_emotion):
    if dominant_emotion == "surprise":
        if dominant_sentiment == 'positive':
            label = 'excitement'
        elif dominant_sentiment == 'neutral':
            label = 'ambiguous'
        elif dominant_sentiment == 'negative':
            label = 'distraught'
    if dominant_emotion == "sadness":
        if dominant_sentiment == 'positive':
            label = 'bittersweet'
        elif dominant_sentiment == 'neutral':
            label = 'sadness'
        elif dominant_sentiment == 'negative':
            label = 'sadness'
    if dominant_emotion == "neutral":
        if dominant_sentiment == 'positive':
            label = 'dry'
        elif dominant_sentiment == 'neutral':
            label = 'neutral'
        elif dominant_sentiment == 'negative':
            label = 'suppression'
    if dominant_emotion == "joy":
        if dominant_sentiment == 'positive':
            label = 'joy'
        elif dominant_sentiment == 'neutral':
            label = 'joy'
        elif dominant_sentiment == 'negative':
            label = 'sarcasm'
    if dominant_emotion == "fear":
        if dominant_sentiment == 'positive':
            label = 'excitement'
        elif dominant_sentiment == 'neutral':
            label = 'supression'
        elif dominant_sentiment == 'negative':
            label = 'fear'
    if dominant_emotion == "disgust":
        if dominant_sentiment == 'positive':
            label = 'sarcasm'
        elif dominant_sentiment == 'neutral':
            label = 'supression'
        elif dominant_sentiment == 'negative':
            label = 'disgust'
    if dominant_emotion == "anger":
        if dominant_sentiment == 'positive':
            label = 'sarcasm'
        elif dominant_sentiment == 'neutral':
            label = 'supression'
        elif dominant_sentiment == 'negative':
            label = 'anger'
    return label