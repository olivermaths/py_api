from decision_tree.decision_tree import Leaf
def classify(data, tree):
    if isinstance(tree, Leaf):
        return tree.predictions
    if tree.question.match(data):
        return classify(data, tree.true_branch)
    else:
        return classify(data, tree.false_branch)
