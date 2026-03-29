file = open('recording.txt').readlines()
successor_map = {}


window = []

for line in file:
    for word in line.split():
        clean_word = word.strip('.;,-“’”:?—‘!()_').lower()

        window.append(clean_word)
        
        if(len(window) == 3):
            if (window[0],window[1]) not in successor_map:
                window1 = window[1]
                window0 = window[0]
                key = (window0, window1)
                successor_map[key] = [window[2]]
                
            else:
                
                successor_map[(window0,window1)].append(window[2])
            window.pop(0)


max = 0
max_name = None
for s in successor_map:
    if len(successor_map[s]) > max:
        max = len(successor_map[s])
        max_name = f"{s} *** {successor_map[s]}"

print(max)
print(max_name)