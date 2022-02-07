import math
from matrix import Matrix

class Kmeans:
    def __init__(self, cluster, data):
        self.clusters = cluster
        self.data = data
        self.copy = self.clusters.copy()
    
    def getmidpoints(self, cluster_index):
        values = list(self.copy.values())
        averages = []
        for i in range(0, len(self.data[0])):
            averages.append(0)
        for index in values[cluster_index]:
            for i in range(0, len(self.data[index])):
                averages[i] += self.data[index][i]
        for i in range(0, len(averages)):
            averages[i] = averages[i] / len(values[cluster_index])
        return averages

    def euclidian(self, midpoint, index, cluster_index):
        average = 0
        for i in range(0, len(self.data[index])):
            average += (self.data[index][i] - midpoint[cluster_index][i]) ** 2
        average = math.sqrt(average)
        return average
    
    def run(self):
        cluster = {}
        midpoints = []
        cluster_nums = list(self.copy.keys())
        indexes = list(self.copy.values())

        for index in range(0, len(indexes)):
            midpoints.append(self.getmidpoints(index))
        
        for i in range(0, len(midpoints)):
            cluster[i + 1] = []
        for i in range(0, len(self.data)):
            euclid = []
            for j in range(0, len(midpoints)):
                euclid.append(self.euclidian(midpoints, i, j))
            minimum = min(euclid)
            cluster[euclid.index(minimum) + 1].append(i)
        if cluster != self.copy:
            self.copy = cluster
            self.run()
        else:
            self.clusters = cluster
            self.midpoint = midpoints

