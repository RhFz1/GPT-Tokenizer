import os
from dotenv import load_dotenv

load_dotenv()


data_path = os.environ.get("DATA_PATH") + '/merges_dict.txt'

merges = {}

with open(data_path, 'r') as file:
    for line in file:
        pair, idx = line.split(':')
        pair = tuple(map(int, pair.split(',')))
        idx = int(idx)
        merges[pair] = idx
file.close()