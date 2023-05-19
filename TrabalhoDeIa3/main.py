import test
from decisiontree import DecisionTree

def readInput():
	examples = list()
	attributes = dict()

	attribs = input().split(',')
	attribs.pop(0)
	classification = attribs[len(attribs)-1]

	for attr in attribs:
		attributes[attr] = set()

	thereIsInput = True
	values = input().split(',')

	while(thereIsInput):
		values.pop(0)
		example = dict()
		for k in range(len(values)):
			example[attribs[k]] = values[k]
			attributes[attribs[k]].add(values[k])
		examples.append(example)
		try:
			values = input().split(',')
		except EOFError:
			thereIsInput = False
	del attributes[classification]
	return (examples, attributes) 

# -------------------------------------------------------------

# data = readInput()

decision_tree = DecisionTree()
decision_tree.tree = test.tree

# decision_tree.learn_decision_tree(data[0], data[1], null)

# decision_tree.printTree()

print('Want to introduce a new example? (y/n): ')
option = input().lower()
while option == 'y':
	print()
	out = decision_tree.newExample()
	print('Output: '+out)
	print('\nWant to introduce a new example? (y/n): ')
	option = input().lower()




# ------------------------------------------------
# OUT = readInput()
# examples = OUT[0]
# attributes = OUT[1]

# for attr in attributes:
# 	string = attr+': '+str(attributes[attr])
# 	print(string)

# for example in examples:
#    string = ''
#    for attr in example:
#        string += attr+': '+example[attr]+';  '
#    print(string) 