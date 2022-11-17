from decision_tree.gini import class_counts
from decision_tree.best_split import find_best_split
from decision_tree.partition import partition


class Decision_Node:
    def __init__(self, question, gain, true_branch, false_branch):
      self.question = question
      self.gain = gain
      self.true_branch = true_branch
      self.false_branch = false_branch

class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)

def build_tree(rows):
  gain, question = find_best_split(rows)
  if gain == 0:
    return Leaf(rows)
  true_rows, false_rows = partition(rows, question)
  true_branch = build_tree(true_rows)
  false_branch = build_tree(false_rows)
  return Decision_Node(question,gain, true_branch, false_branch)