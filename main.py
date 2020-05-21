#!/usr/bin/env python
from board import Board
from solver import GraphSolver

b = Board('./webster_dictionary.json', letters = ['a','r','t','n','t','s','e','d','e','r','s','o','h','w','p','h'])
s = GraphSolver(b)

print(b)
s.solve()
