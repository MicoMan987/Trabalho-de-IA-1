from util import *
from decisiontree import DecisionTree

data = readInput() # contagem de positive_examples, negative_examples precisa ser mudado para funcionar com datasets multiclasses(que não tem como output apenas YES ou NO)

decision_tree = DecisionTree(data)

decision_tree.learn_decision_tree()

decision_tree.printTree()

decision_tree.read_test_set()
