from tree import Tree

# arvore de decisao do livro
tree = Tree('Pat')
tree.addBranch('Some', Tree('Yes'))
tree.addBranch('None', Tree('No'))

tree2 = Tree('Hun')
tree2.addBranch('No', Tree('No'))

tree3 = Tree('Type')
tree3.addBranch('French', Tree('Yes'))
tree3.addBranch('Italian', Tree('No'))
tree3.addBranch('Burger', Tree('Yes'))

tree4 = Tree('Fri/Sat')
tree4.addBranch('Yes', Tree('Yes'))
tree4.addBranch('No', Tree('No'))

tree3.addBranch('Thai', tree4)

tree2.addBranch('Yes', tree3)

tree.addBranch('Full', tree2)
