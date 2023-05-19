from abc import ABC, abstractmethod

class Node(ABC):
	def __init__(self, name):
		self.name = name
		self.branches = dict()

	@abstractmethod
	def addBranch(self, branch_name, subtree):
		pass

	def isLeaf(self):
		return not self.branches

class Tree(Node):
	def __init__(self, name):
		super().__init__(name)

	def addBranch(self, branch_name, subtree):
		self.branches[branch_name] = subtree