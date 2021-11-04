import sys
sys.path.append('src')

from graph import graph

a = graph([[1, 2], [1, 3], [1, 5], [0, 1,], [0, 9], [5, 8], [5, 2]])
if a.get_children(1) != [2, 3, 5]:
    print("false 1")
if a.get_parents(2) != [1, 5]:
    print("false 1.5")
b = graph([[7, 4], [4, 7], [5, 7], [4, 5], [1, 3]])
if b.get_children(4) != [7, 5]:
    print("false 2")
if b.get_parents(7) != [4, 5]:
    print("false 2.5")
c = graph([[8.1, -3], [4, 8.1], [-3, 4], [8.1, 4]])
if c.get_children(8.1) != [-3, 4]:
    print("false 3")
if c.get_parents(4) != [-3, 8.1]:
    print("false 3.5")
print(a.breadth_first(1))