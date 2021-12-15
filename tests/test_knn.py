import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from knn import KNearestNeighborsClassifier

knn = KNearestNeighborsClassifier(5)

x = [[0.14, 0.14, 0.28, 0.44], 
    [0.10, 0.18, 0.28, 0.44], 
    [0.12, 0.10, 0.33, 0.45], 
    [0.10, 0.25, 0.25, 0.40], 
    [0.00, 0.10, 0.40, 0.50], 
    [0.00, 0.20, 0.40, 0.40], 
    [0.10, 0.08, 0.35, 0.47], 
    [0.00, 0.05, 0.30, 0.65], 
    [0.20, 0.00, 0.40, 0.40], 
    [0.25, 0.10, 0.30, 0.35], 
    [0.22, 0.15, 0.50, 0.13], 
    [0.15, 0.20, 0.35, 0.30], 
    [0.22, 0.00, 0.40, 0.38]]

y = ["Shortbread", "Shortbread", "Shortbread", "Shortbread", "Sugar", "Sugar", "Sugar", "Sugar", "Fortune", "Fortune", "Fortune", "Fortune", "Fortune"]                
knn.fit(x, y)
assert knn.compute_distance([0.10, 0.15, 0.30, 0.45]) == [0.047 ,  0.037,  0.062,  0.122 ,  0.158 , 0.158,  0.088,  0.245,  0.212,  0.187 ,  0.396 , 0.173,  0.228]
assert knn.classify([0.10, 0.15, 0.30, 0.45]) == "Shortbread"