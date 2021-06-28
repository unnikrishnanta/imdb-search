from collections import defaultdict

def build_inverted_idx(documents):
  inv_idx = defaultdict(set)
  i = 1;
  for d in documents: 
    for word in d.split():
      inv_idx[word].add(i)
    i += 1
  return inv_idx

