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
d = graph([[4, 1], [4, 2], [4, 8], [4, 7], [1, 2], [1, 11], [11, 12], [12, 11], [7, 3], [7, 9]])

if d.depth_first(4) != [4, 7, 9, 3, 8, 2, 1, 11, 12]:
    print("dsf false")
if d.breadth_first(4) != [4, 1, 2, 8, 7, 11, 3, 9, 12]:
    print("bsf fail")
