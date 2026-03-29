import random

import pickle

def load(filename="trigram-map.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)


successor_map = load()
try:
    sentence = ""
    wordpair0 = ('of', 'the')

    for i in range(100):
        word1 = random.choice(successor_map[wordpair0])
        wordpair0 = (wordpair0[1],word1)
        sentence += word1+" "

    print(sentence)
except:
    print(sentence)

