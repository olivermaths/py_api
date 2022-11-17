import decision_tree.gini as gini
def info_gain(left, right, current_uncertainty):
    p = float(len(left)/(len(left) + len(right)))
    return current_uncertainty - (p * gini.gini(left)) - ((1 - p) * gini.gini(right))