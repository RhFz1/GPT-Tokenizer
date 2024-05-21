import os 
from dotenv import load_dotenv

load_dotenv()

# Importing data paths
input_text_path = os.path.join(os.environ.get("DATA_PATH"), 'data.txt')
tokenized_text_path = os.path.join(os.environ.get("DATA_PATH"), 'tokenized.txt')

counts = {}

text = ""
with open(input_text_path, 'r') as file:
    text = file.read()
file.close()


for c, s in zip(text, text[1 :]):
    counts[(c, s)] = counts.get((c, s), 0) + 1

counts = dict(sorted(counts.items(), key=lambda x :-x[1]))

print(counts)