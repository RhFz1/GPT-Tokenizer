import os 
from dotenv import load_dotenv

load_dotenv()

# Importing data paths
input_text_path = os.path.join(os.environ.get("DATA_PATH"), 'data.txt')

# this function will take a list of tokens and return a dictionary with the counts of each token pair
def get_stats(tokens):
    counts = {}
    for pair in zip(text, text[1: ]):
        counts[pair] = counts.get(pair , 0) + 1
    
    return counts

text = ""
with open(input_text_path, 'r') as file:
    text = file.read()
file.close()

tokens = text.encode('utf-8')
tokens = list(map(lambda x: int(x), tokens))

counts = get_stats(tokens)

# print(sorted(((v , k) for k, v in counts.items()), reverse=True))

# here im supposed to get the key which has the highest frequency

top_pair = max(counts, key = counts.get)

print(top_pair)