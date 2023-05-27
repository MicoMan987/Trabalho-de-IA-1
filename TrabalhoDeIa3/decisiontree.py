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
		self.total_examples_in_dataset = data[2]
		probability_list = data[3]
		self.entropy_of_output_variable = self.entropy(probability_list)

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
		attribute_values = dict() # se o atributo fosse Patrons do dataset restaurant teriamos um dicionário assim: attribute_values = {'None': {'Yes':0, 'No':2}, 'Full': {'Yes':2, 'No':4}, 'Some': {'Yes':4, 'No':0}}
		for attribute_value in attribute[1]:
			attribute_values[attribute_value] = dict()

		for example in examples:
			attribute_value = example[attribute_name]
			output_value = example[class_key]
			try: attribute_values[attribute_value][output_value] += 1
			except: attribute_values[attribute_value][output_value] = 1
		return self.information_gain(attribute, attribute_values)


	def information_gain(self, attribute, attribute_values):
		remainder = 0.0
		for attribute_value in attribute[1]:
			# (output value, value frequency)
			output_values_list = list(attribute_values[attribute_value].items()) # .items() retorna um set de tuplos(chave,valor), daí output_values_list é uma lista de tuplos - algo como isso por exemplo: [('Yes', 0), ('No', 2)]
			if not output_values_list: continue
			total_examples = sum([value_frequency := pair[1] for pair in output_values_list]) # total de exemplos que tem esse attribute_value 
			probability_list = list() # lista com as probabilidades de cada output_value(Ex: 'Yes', 'No') para esse attribute_value(Ex: 'Some')
			for pair in output_values_list:
				probability_list.append(pair[1]/total_examples)

			remainder+=(total_examples)/(self.total_examples_in_dataset)*self.entropy(probability_list)
		gain = self.entropy_of_output_variable - remainder # quanto menor for o remainder maior é o ganho
		return gain

	def entropy(self, probability_list):
		entropy = 0.0
		for probability in probability_list:
			if probability != 0.0:
				entropy += probability*log2(probability)
		return -entropy


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
