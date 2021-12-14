import math

def calc_minimum(numbers):
    a = numbers[0]
    for number in numbers:
        if number < a:
            a = number
    return a

class KNearestNeighborsClassifier:

    def __init__(self, k):
        self.k = k

    def fit(self, data, classification):
        self.data = data
        self.classification = classification

    def compute_distance(self, observation):
        distances = []
        for i in range(0, len(self.data)):
            distances.append(0)
        for row in self.data:
            for i in range(0, len(self.data[0])):
                distances[self.data.index(row)] += (observation[i] - row[i]) ** 2
        sqrts = []
        for i in range(0, len(distances)):
            sqrts.append(math.sqrt(distances[i]))
        return sqrts
    
    def classify(self, observation):
        distances  = self.compute_distance(observation)
        copy = self.compute_distance(observation)
        for i in range(0, len(distances)):
            rounded = round(distances[i], 5)
            distances[i] = rounded
        closest = []
        indexes = []
        for i in range(0, self.k):
            min = calc_minimum(copy)
            closest.append(min)
            copy.remove(min)
        print(distances)
        print(copy)
        for i in range(0, len(closest)):
            index = distances.index(closest[i])
            indexes.append(index)
        print(indexes)

        
    

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
knn.compute_distance([0.10, 0.15, 0.30, 0.45])
knn.classify([0.10, 0.15, 0.30, 0.45])