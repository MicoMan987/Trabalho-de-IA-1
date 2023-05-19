from typing import *
from tree import Tree

class DecisionTree:
	def __init__(self):
		self.classification = False
		self.tree = None

	def learn_decision_tree(self, examples: List[dict], attributes: Dict[str,str], parent_examples: List[dict]):
		if not examples: return self.most_common_output_value(parent_examples)
		if self.all_have_same_classification(examples): return Tree(self.classification)
		if not attributes: return self.most_common_output_value(examples)
		attribute = max(attributes.items(), key=lambda attribute: importance(attribute, examples))[0] # pega o atributo(chave) mais importante segunda a função 'importance()'
		tree = Tree(attribute)
		values_set = attributes[attribute]
		del attributes[attribute]
		for value in values_set:
			exs = [example for example in examples if example[attribute] == value]
			subtree = learn_decision_tree(exs, attributes, examples)
			tree.add_branch(value, subtree)
		self.tree = tree

	def most_common_output_value(self, parent_examples: List[dict]):
		output = dict()
		class_key = list(parent_examples[0].keys())[-1]  # Obter a chave da classificação (última chave)
		for example in parent_examples:
			value = example[class_key] # Obter a classificação/valor associada
			try: output[value] += 1
			except: output[value] = 1
		output_value = max(output.items(), key=lambda x: x[1])[0] # pega a chave(output value) mais frequente segundo o valor(contagem) de cada par
		return Tree(output_value)
	
	def all_have_same_classification(self, examples: List[dict]):
		class_key = list(examples[0].keys())[-1]  # Obter a chave da classificação (última chave)
		classification = examples[0][class_key] # Obter a classificação do primeiro exemplo
		for example in examples:
			if (example[class_key] != classification):
				return False
		self.classification = classification
		return True

	def importance(self, attribute, examples):
		return 0

	def newExample(self):
		tmpNode = self.tree
		classification = str()
		while(not tmpNode.isLeaf()):
			self.printOptions(tmpNode)
			branch_name = input()
			tmpNode = tmpNode.branches[branch_name]
		return tmpNode.name

	def printOptions(self, node):
		text = node.name+'? ('
		branches_name = list(node.branches.keys())
		for i in range(len(branches_name)):
			text+=branches_name[i]
			if (i < len(branches_name)-1): text+='/'
		text+='): '
		print(text)

	def printTree(self):
		pass