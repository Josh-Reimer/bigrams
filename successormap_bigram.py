import pickle

def save(var, filename="successormap1.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(var, f)

def load(filename="successormap1.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)




reader = open('recording.txt')
successor_map = {}
window = [] #window is only ever 2 words long

for line in reader:
  for word in line.split():
    clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
    window.append(clean_word)
  
    if len(window) == 2:
      if window[0] not in successor_map:
        # add code here
        #print(window[0])
        successor_map[window[0]] = [window[1]]
      else:
        successor_map[window[0]].append(window[1])
        
      window.pop(0)

max = 0
i = None

for l in successor_map:
   
   if len(successor_map[l]) > max:
      max = len(successor_map[l])
      i = [l,successor_map[l]]


print(max)
print(i)
