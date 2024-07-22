import os 
import json
from dotenv import load_dotenv
from typing import List, Dict, Tuple

load_dotenv()

# Defining vobab parameters
vocab_size = 384
native_vocab = 256
num_merges = vocab_size - native_vocab

if os.path.isfile(os.environ.get("DATA_PATH") + '/merges_dict.txt'):
    from construct_merge import merges
else:
    merges = {}

# Importing data paths
input_text_path = os.environ.get("DATA_PATH") + '/input.txt'

text = ""
with open(input_text_path, 'r') as file:
    text = file.read()
file.close()

tokens = text.encode('utf-8')
tokens = list(map(int, tokens))

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

    for i in range(num_merges):
        counts = get_stats(ids)
        pair = max(counts, key=counts.get)
        ids = merge(ids, pair, native_vocab + i)
        merges[pair] = native_vocab + i
        print(f"pair: {pair},{counts[pair]} -> {native_vocab + i}")
    
    print(f"Token length: {len(tokens)}")
    print(f"ids length: {len(ids)}")
    print(f"Compression rate: {len(tokens) / len(ids)}")
        
    return ids

def decode(ids: List) -> str:

    vocab = {idx : bytes([idx]) for idx in range(native_vocab)}

    for (c0, c1), idx in merges.items():
        vocab[idx] = vocab[c0] + vocab[c1]
    
    tokens = b"".join(vocab[idx] for idx in ids)

    text = tokens.decode('utf-8', errors='replace')

    return text