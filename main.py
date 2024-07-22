from construct_merge import merges
from bytepair_tok import get_stats, merge, decode
from dotenv import load_dotenv

load_dotenv()


text = "Hey There!! I'm using WhatsApp"
tokens = text.encode('utf-8')
tokens = list(map(int, tokens))

while True:
    
    stats = get_stats(tokens)
    pair = min(stats, key= lambda x: merges.get(x, float('inf')))

    if pair not in merges:
        break # no pair found to merge
    
    tokens = merge(tokens, pair, merges[pair])

print(decode(tokens)[:100])
