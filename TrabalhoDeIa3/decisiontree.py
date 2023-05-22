import re # regular expression
from typing import *
from math import log2
from tree import Tree

class DecisionTree:
	def __init__(self, data: tuple):
		self.tree = None
		self.classification = False
		self.examples = data[0]
		self.attributes = data[1]
		self.p = data[2] 	# p -> n° de exemplos com output positivo
		self.n = data[3] 	# n -> n° de exemplos com output negativo
		self.entropy_of_output = self.entropy(self.p/(self.p+self.n))


	def learn_decision_tree(self):
		self.tree = self.learnDecisionTree(self.examples, self.attributes.copy(), None)


	def learnDecisionTree(self, examples: List[dict], attributes: Dict[str,set], parent_examples: List[dict]):
		if not examples: return self.most_common_output_value(parent_examples)
		if self.all_have_same_classification(examples): return Tree(self.classification)
		if not attributes: return self.most_common_output_value(examples)
		attribute = max(attributes.items(), key=lambda attribute: self.importance(attribute, examples))[0] # pega o atributo(chave) mais importante segunda a função 'importance()'
		tree = Tree(attribute)
		values_set = attributes[attribute]
		del attributes[attribute]
		for value in values_set:
			exs = [example for example in examples if example[attribute] == value]
			subtree = self.learnDecisionTree(exs, attributes, examples)
			tree.addBranch(value, subtree)
		return tree


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
		attribute_name = attribute[0] # pegando a chave(nome do atributo)
		class_key = list(examples[0].keys())[-1]  # Obter a chave da classificação (última chave)
		
		dictionary = dict()
		for attribute_value in attribute[1]:
			dictionary[attribute_value] = dict()

		for example in examples:
			attribute_value = example[attribute_name]
			output_value = example[class_key]
			try: dictionary[attribute_value][output_value] += 1
			except: dictionary[attribute_value][output_value] = 1
		return self.information_gain(attribute, dictionary)


	def information_gain(self, attribute, dictionary):
		remainder = 0.0
		for attribute_value in attribute[1]:
			item_list = list(dictionary[attribute_value].items()) # .items() retorna um set de tuplos(chave,valor), daí item_list é uma lista de tuplos - algo como isso: [('yes', 5), ('no', 4)]
			if not item_list: continue
			if item_list[0][0] == 'yes':
				pk = item_list[0][1]
				nk = 0
				try: nk = item_list[1][1]
				except: pass
				remainder+=(pk+nk)/(self.p+self.n)*self.entropy(pk/(pk+nk))
			else:
				pk = 0
				nk = item_list[0][1]
				try: pk = item_list[1][1]
				except: pass
				remainder+=(pk+nk)/(self.p+self.n)*self.entropy(pk/(pk+nk))
		gain = self.entropy_of_output - remainder # entropy remaining
		return gain
	

	def entropy(self, q): # q = probability
		if q==0 or (1-q)==0: return 0 
		return -(q*log2(q) + (1-q)*log2(1-q)) 


	def read_test_set(self):
		filename = input('\nEnter the name of the file with the corresponding test set: ')
		with open(filename) as file:
			example = file.readline().strip()
			while example:
				classification = self.classify(example.split(','), self.tree)
				print(example.split(',')[0] + ' -> ' + classification)
				example = file.readline().strip()


	def classify(self, example, tree):
		index = list(self.attributes.keys()).index(tree.name)+1
		branch_name = example[index]
		if re.fullmatch(r'^[0-9]+\.[0-9]+$', branch_name) or re.fullmatch(r'^[0-9]+$', branch_name):
			for branch in tree.branches:
				interval = branch.split(',')
				if float(interval[0]) <= float(branch_name) <= float(interval[1]): 
					branch_name = branch
					break	
		subtree = tree.branches[branch_name]
		if subtree.isLeaf():
			return subtree.name
		return self.classify(example, subtree)


	def printTree(self):
		self.print_tree(self.tree, self.examples, 0)

	
	def print_tree(self, tree, examples, tab):
		tabs = tab*'\t'
		print(f'{tabs}<{tree.name}>')
		for branch_name in tree.branches:
			subtree = tree.branches[branch_name]
			if subtree.isLeaf():
				tabs = (tab+1)*'\t'
				classification = subtree.name
				counter = self.counter(examples, tree.name, branch_name, classification)
				print(f'{tabs}{branch_name}: {classification} ({counter})')
			else:
				tabs = (tab+1)*'\t'
				print(f'{tabs}{branch_name}:')
				self.print_tree(subtree, [example for example in examples if example[tree.name]==branch_name], tab+2)


	def counter(self, examples, attribute, value, classification):
		counter = 0
		class_key = list(examples[0].keys())[-1]  # Obter a chave da classificação (última chave)
		for example in examples:
			if example[class_key] == classification and example[attribute] == value: 
				counter+=1 
		return counter