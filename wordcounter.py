from collections import Counter


file = open("recording.txt","r")
filebuffer = file.read()

counter = Counter()

for word in filebuffer.split():
	cleanword = word.strip("!?.()&@#-;:/").lower()
	counter[cleanword] += 1
	
print(counter.most_common()[0:10])
print()
print(counter["jesus"])


# generate bi-grams
bi_counter = Counter()
bigrams = []
window = []
successor_map = {}


for word in filebuffer.split():
	window.append(word)
	if len(window) >= 2:
		current_window = window
		t_window = tuple(current_window)
		bigrams.append(t_window)
		bi_counter[t_window] += 1
		#print(window)
		window.pop(0)
		
		
print(bigrams[0:100])
print("/n/n")
print(bi_counter.most_common()[0:10])
file.close()