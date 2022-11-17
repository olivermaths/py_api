from decision_tree.constants import header
class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value
    def match(self, example):
        val = example[self.column]
        if self.is_numeric(val):
            return val >= self.value
        else:
            return val == self.value
    def __repr__(self):
        condition = "=="
        if self.is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (header[self.column], condition, str(self.value))
    def is_numeric(self, value):
        return isinstance(value, int) or isinstance(value, float)

