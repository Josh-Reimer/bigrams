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
print(os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files"))


# generate bi-grams
bi_counter = Counter()
bigrams = []
successor_map = {}	# successor_map stores a list of every unique word with every possible unique word that comes after it in the original text
window = []

try:
	for dir in sorted(os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files")):
		if "006" in dir:
			print('breaking...')
			
			save(successor_map)
			
			break
		for file in sorted(os.listdir(rootdir+dir)):
			print(file)
			opened_file = open(rootdir+dir+"/"+file)
			for word in opened_file.read().split():	#this loops through every word in a single text file

				window.append(word)	# add the word to the 2-word 'window' 
				if len(window) >= 2:	# then check if the window is longer or equal 2 words
					current_window = window	# if the window is longer or equal than 2 words update the current window to the window
					t_window = tuple(current_window)	# convert the current window to a tuple for counter support
					bigrams.append(t_window)	# add the tupled window to the bigrams list
					bi_counter[t_window] += 1	# update the counter (the counter ignores duplicate data)
					if window[0] not in successor_map:	# if the first word in the window is not in the preceding words dictionary
						successor_map[window[0]] = [window[0]]	# add the first word to the preceding words dictionary
					else:	# if the first word is in the successor map then: ...
						successor_map[window[0]].append(window[1])	# add the second word to the list of preceding words for the first word
					
					window.pop(0)	# remove the last element from the window so the window 'slides' over the text 2 words at a time
			opened_file.close()
except():
	print(bigrams[::50])
	print("/n/n/n")
	print(successor_map)
	print("/n/n/n")
	print(bi_counter)
	print("/n/n/n")
	print(window)
	print()
		
#print(bigrams[0:100])
#print("/n/n")
#print(bi_counter.most_common()[0:10])


sentence = "the "
word0 = "the"
#print(word0)
for i in range(10):
	word1 = random.choice(successor_map[word0])
	word0 = str(word1)
	sentence += word1+" "
	#print(word1)
print(sentence)

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.4f} seconds")