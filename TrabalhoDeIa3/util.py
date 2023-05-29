# utility functions

import math
import re # regular expression

def readInput():
	data = read_input()
	examples = data[0]
	attributes = data[1]
	example = examples[0]

	# regex matching
	int_pattern = re.compile(r'^[0-9]+$')
	float_pattern = re.compile(r'^[0-9]+\.[0-9]+$')

	for attribute in example:
		if float_pattern.match(example[attribute]) or int_pattern.match(example[attribute]):
			intervals = define_intervals(examples, attribute)
			attributes[attribute] = set() # limpar os valores guardados
			for e in examples:
				interval = discretize_variable(float(e[attribute]), intervals)
				e[attribute] = interval # mudar o valor que está lá atualmente, por um intervalo
				attributes[attribute].add(interval) # agora o atributo passa a possuir um conjunto de intervalos e não de valores
	return data


def read_input():
	examples = list()
	attributes = dict()
	output_values_frequency = dict()
	probability_list = list()

	filename = input('Enter the name of a file with a dataset (training examples): ')

	with open(filename) as file:
		attribs = file.readline().strip().split(',')
		attribs.pop(0)
		classification = attribs[len(attribs)-1]

		for attr in attribs:
			attributes[attr] = set()

		thereIsInput = True
		values = file.readline().strip().split(',')

		while(thereIsInput):
			values.pop(0)
			example = dict()
			for k in range(len(values)):
				example[attribs[k]] = values[k]
				attributes[attribs[k]].add(values[k])
				if attribs[k] == classification:
					try: output_values_frequency[values[k]] += 1
					except: output_values_frequency[values[k]] = 1
			examples.append(example)
			values = file.readline().strip()
			if not values: thereIsInput = False
			else: values = values.split(',')
		del attributes[classification]

	total_examples_in_dataset = len(examples)

	for output_value in output_values_frequency:
		frequency = output_values_frequency[output_value]
		probability_list.append(frequency/total_examples_in_dataset)
	return (examples, attributes, total_examples_in_dataset, probability_list)


# Função para discretizar os valores de uma variável(atributo)
def discretize_variable(value, intervals):
	for interval in intervals:
		if interval[0] <= value <= interval[1]:
			return f'{interval[0]},{interval[1]}'
	return None


# Função para definir os intervalos de um atributo com base nos valores presentes nos dados.
# Os intervalos criados são usados na função discretize_variable() para converter os valores contínuos em intervalos discretos
def define_intervals(examples, attribute):
	values = [float(example[attribute]) for example in examples]
	min_value = min(values)
	max_value = max(values)

	n = len(examples)
	num_intervals = int(1 + 3.322 * math.log10(n)) # cálcula o número adequado de intervalos necessários usando a fórmula de Sturges

	# step é a diferença entre os valores inicial e final de um intervalo. Ela representa o tamanho de cada intervalo, cada intervalo terá um tamanho igual a step.
	# é calculado dividindo a diferença entre o valor máximo e mínimo da variável(atributo) pelo número de intervalos(num_intervals). Isso garante que os intervalos sejam criados de forma uniforme.
	step = (max_value - min_value) / num_intervals
	intervals = []
	for i in range(num_intervals): # itera num_intervals vezes para criar os intervalos, armazenando-os em uma lista de tuplas (start, end).
		start = round(min_value + i * step, 3)
		end = round(min_value + (i + 1) * step, 3) # arredondar os valores longos para somente três casas decimais
		intervals.append((start, end))
	return intervals
