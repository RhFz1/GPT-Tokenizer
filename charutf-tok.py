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
tokenized_text = text.encode('utf-8')

# Decoding the encoded numbers

print(tokenized_text.decode('utf-8'))


