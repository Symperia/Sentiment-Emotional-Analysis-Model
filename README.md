# Hybrid Sentiment/Emotional Analysis Project

## Introduction
Assigning emotional labels becomes a complex task for machine learning algorithms due to nuance and sarcasm.
This project attempts to reach accuracy using a heuristic sorting method from pretrained llm outputs to run bulk messages at fast speeds.

## To-Do
- Sort complex vs straightforward emotions into a pi chart
- Add sliding window chunking to bypass 512 token limit
- Do runtime tests on more advanced models for higher accuracy
- Fine tune (LoRA) llms through imessage metadata
- Consider more heuristic approaches to implementing meta data to final label

## Pretrained LLMs Used
- https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
- https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment

## How To Run
For now the code samples individual conversations and documentation and functionality is limited. 
To run at minimum, a path to a .csv file with headers specifically "Message Text" and "Is New Conersation" are needed.
