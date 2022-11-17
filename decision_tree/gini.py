def gini(rows):
  counts = class_counts(rows)
  impurity = 1
  for lbl in counts:
      prob_of_lbl = counts[lbl]/float(len(rows))
      impurity -= prob_of_lbl**2
  return impurity
  
def class_counts(rows):
  counts = {}
  for row in rows:
    label = row[-1]
    if label not in counts:
      counts[label] = 0
    counts[label] += 1
  return counts