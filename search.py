def search(query, inv_idx, documents):
  if len(query) == 0: 
    return []

  query = query.split()
  docs = inv_idx[query[0]]

  for qw in query[1:]:
    di = inv_idx[qw] 
    docs = docs.intersection(di)
  results = list()
  for i in docs: 
    results.append(documents[i-1])
  return results
