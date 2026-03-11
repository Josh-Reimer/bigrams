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
        # add code here
        #print(window[0])
        #print(successor_map)  
            
        successor_map[window[0]].append(window[1])
      window.pop(0)


print(successor_map['thank'])
print(successor_map['peace'])