import os

rootdir = "gutenberg-dammit-files-v002/gutenberg-dammit-files/"
print(os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files"))

import pickle

def save(var, filename="trigram-map.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(var, f)



trigrams = []
successor_map = {}
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

				window.append(word)	
				if len(window) == 3:
						
					current_window = window	
					t_window = tuple(current_window)	
					trigrams.append(t_window)	
					
					if (window[0],window[1]) not in successor_map:	
						successor_map[(window[0],window[1])] = [window[2]]	
					else:	
						successor_map[(window[0],window[1])].append(window[2])	
					
					window.pop(0)	
			opened_file.close()
except():
	print(trigrams[::50])
	print("/n/n/n")
	print(successor_map)
	
	