successor_map = {}

bigram1 = ('the', 'honour')
bigram2 = ('honour', 'the')
bigram3 = ('the', 'sanity')
bigrams = (bigram1, bigram2, bigram3)

for bigram in bigrams:
  if bigram[0] not in successor_map:
    successor_map[bigram[0]] = [bigram[1]]
  else:
    print(type(successor_map[bigram[0]]))
    successor_map[bigram[0]].append(bigram[1])

print(successor_map)