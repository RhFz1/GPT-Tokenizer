import os 
from dotenv import load_dotenv
from typing import List, Dict, Tuple

load_dotenv()

# Defining vobab parameters
vocab_size = 1024
native_vocab = 768
num_merges = vocab_size - native_vocab

# Importing data paths
input_text_path = os.environ.get("DATA_PATH")

text = ""
with open(input_text_path, 'r') as file:
    text = file.read()
file.close()

tokens = text.encode('utf-8')
tokens = list(map(int, tokens))

print(f"Total tokens: {len(tokens)}")

# this function will take a list of tokens and return a dictionary with the counts of each token pair
def get_stats(tokens: List) -> Dict:
    counts = {}
    for pair in zip(tokens, tokens[1: ]):
        counts[pair] = counts.get(pair , 0) + 1
    
    return counts

def merge(ids: List, pair: Tuple, idx: int) -> List:

    new_ids = []

    i = 0

    while i < len(ids):

        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    
    return new_ids

# this is the function where we will be compressing the tokens
def encode(ids: List, num_merges: int) -> Tuple[List, Dict]:
    
    merges = {}

    for i in range(num_merges):
        counts = get_stats(ids)
        pair = max(counts, key=counts.get)
        ids = merge(ids, pair, native_vocab + i)

        print(f"pair: {pair},{counts[pair]} -> {native_vocab + i}")
    
    print(f"Token length: {len(tokens)}")
    print(f"ids length: {len(ids)}")
    print(f"Compression rate: {len(tokens) / len(ids)}")
        
    return ids, merges

ids, merges = encode(tokens, num_merges)