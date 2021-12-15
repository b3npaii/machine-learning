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
        for i in range(0, len(sqrts)):
            rounded = round(sqrts[i], 3)
            sqrts[i] = rounded
        return sqrts
    
    def classify(self, observation):
        distances  = self.compute_distance(observation)
        copy = self.compute_distance(observation)

        for i in range(0, len(distances)):
            rounded = round(distances[i], 5)
            distances[i] = rounded
            copy[i] = rounded

        closest = []
        indexes = []
        for i in range(0, self.k):
            min = calc_minimum(copy)
            closest.append(min)
            copy.remove(min)

        for i in range(0, len(closest)):
            index = distances.index(closest[i])
            indexes.append(index)

        classifications = []
        for index in indexes:
            classifications.append(self.classification[index])

        counts = {}
        for each in classifications:
            if each not in counts:
                counts[each] = 1
            elif each in counts:
                counts[each] += 1
        answer = max(counts, key=counts.get)
        return answer
