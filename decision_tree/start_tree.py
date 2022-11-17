import decision_tree.constants as consts
from decision_tree.decision_tree import *
from decision_tree.utils import *

def train_tree(data) -> None:
    hdata = handle_data(consts.header, data)
    consts.tree = build_tree(hdata)
    return consts.tree
