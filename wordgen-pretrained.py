from collections import Counter
import random
import time



import pickle

def save(var, filename="data.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(var, f)

def load(filename="data.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)






try:
	load()
except:
	print('failed to load vars because they dont exist yet')


start_time = time.perf_counter()

import os
rootdir = "gutenberg-dammit-files-v002/gutenberg-dammit-files/"
#print(os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files"))




# generate bi-grams
bi_counter = Counter()
bigrams = []
successor_map = load()	# successor_map stores a list of every unique word with every possible unique word that comes after it in the original text
window = []

#print(len(successor_map['the']))

		


previous_word = ''
sentence = "the "
word0 = "the"

i = 0
while i <= 200:
     word1 = random.choice(successor_map[word0])
     word0 = str(word1)
    
     if word0 not in successor_map or previous_word == word0:
          random.seed(3.14159)
          continue
     previous_word = word0
     sentence += word1+" "
     i += 1
	
print(sentence)

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.4f} seconds")