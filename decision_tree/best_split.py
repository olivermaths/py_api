from decision_tree.gini import gini
from decision_tree.partition import partition
from decision_tree.info_gain import info_gain
from decision_tree.question import Question

def find_best_split(rows):
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1
    for col in range(n_features):
        values = set([row[col] for row in rows])
        for val in values:
          question = Question(col, val)
          true_rows, false_rows = partition(rows, question)
          if len(true_rows) == 0 or len(false_rows) == 0:
            continue
          gain = info_gain(true_rows, false_rows, current_uncertainty)
          if gain >= best_gain:
              best_gain, best_question = gain, question
    return best_gain, best_question