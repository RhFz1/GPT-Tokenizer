import os
from dotenv import load_dotenv

load_dotenv()

# Importing data paths
input_text_path = os.path.join(os.environ.get("DATA_PATH"), 'data.txt')
tokenized_text_path = os.path.join(os.environ.get("DATA_PATH"), 'tokenized.txt')

# Reading the text file.
if not os.path.exists(input_text_path):
    pass

text = ""
with open(input_text_path, 'r') as file:
    text = file.read()
file.close()

# Encoding the text contents to numbers
tokenizer = lambda s : ','.join([str(ord(c)) for c in s])
tokenized_text  = tokenizer(text)

if not os.path.exists(tokenized_text_path):
    with open(tokenized_text_path, 'w+') as file:
        file.write(tokenized_text)

# Decoding the encoded numbers

decoder = lambda s : ''.join(chr(int(c)) for c in s.split(','))
print(decoder(tokenized_text))