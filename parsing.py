import pandas as pd
import numpy as np

# file path must be raw string
def parse(file_path):
    messages = pd.read_csv(file_path,header=0)
    messages['Message Text'] = messages['Message Text'].astype(str).fillna('')
    conversations_index = np.cumsum(messages['Is New Conversation']=='Yes')
    conversations = ['\n'.join(j.tolist()) for i,j in messages['Message Text'].groupby(conversations_index)]
    return conversations


