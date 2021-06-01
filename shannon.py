from nltk.corpus import brown
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
trimodel = defaultdict(lambda: defaultdict(lambda: 0))
bimodel = defaultdict(lambda: defaultdict(lambda: 0))
for sentence in brown.sents():
    sentence.insert(0, "<s>")
    sentence.append("</s>")
    for w1, w2, w3, in trigrams(sentence, pad_right=True, pad_left=True):
        trimodel[(w1, w2)][w3] += 1
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        bimodel[w1][w2] += 1
for w1_w2 in trimodel:
    total_count = float(sum(trimodel[w1_w2].values()))
    for w3 in trimodel[w1_w2]:
        trimodel[w1_w2][w3] /= total_count
for w1 in bimodel:
    total_count = float(sum(bimodel[w1].values()))
    for w2 in bimodel[w1]:
        bimodel[w1][w2] /= total_count

import random
text = ["<s>"]
sentence_finished = False

while not sentence_finished:
  r = random.random()
  accumulator = .0
  for word in bimodel[text[-1]].keys():
      accumulator += bimodel[text[-1]][word]
      if accumulator >= r:
          text.append(word)
          break
  if text[-1:] == ["</s>"]:
      sentence_finished = True
print("Bigram model sentence:")
print (' '.join([t for t in text if t]) + "\n")


text = ["<s>"]
sentence_finished = False

#Get initial word for trigram model
initr = random.random()
initaccumulator = .0
for word in bimodel[text[-1]].keys():
    initaccumulator += bimodel[text[-1]][word]
    if initaccumulator >= initr:
        text.append(word)
        break

#Generate sentence
while not sentence_finished:
  r = random.random()
  accumulator = .0
  for word in trimodel[tuple(text[-2:])].keys():
      accumulator += trimodel[tuple(text[-2:])][word]
      if accumulator >= r:
          text.append(word)
          break
  if text[-1:] == ["</s>"]:
      sentence_finished = True
print("Trigram model sentence:")
print (' '.join([t for t in text if t]) + "\n")
