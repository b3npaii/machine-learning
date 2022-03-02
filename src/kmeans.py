import math

class Kmeans:
    def __init__(self, clusters, data):
        self.initial = clusters
        self.data = data
    
    def getmidpoints(self):
        length = len(self.data[0])
        centers = {}
        for cluster in self.clusters:
            centers[cluster] = [0]
            for i in range(length):
                centers[cluster].append(0)
        for index, cluster in self.clusters.items():
            num_points = len(cluster)
            for point in cluster:
                for coord in range(0, length):
                    centers[index][coord] += self.data[point][coord] / num_points
        self.centers = centers

    def euclidian(self, point_index, cluster):
        center = self.centers[cluster]
        point = self.data[point_index]
        distance = 0
        for i in range(0, len(point)):
            distance += (point[i] - center[i]) ** 2
        distance  = distance ** 0.5
        return distance
    
    def reassign_centers(self):
        new_clusters = {}
        for index in self.clusters.keys():
            new_clusters[index] = []
        for point in range(0, len(self.data)):
            distances = {}
            for cluster in self.clusters:
                distances[cluster] = self.euclidian(point, cluster)
            closest = min(distances, key=distances.get)
            new_clusters[closest].append(point)
        self.clusters = new_clusters

    def run(self):
        previous = {}
        removed = []
        self.clusters = self.initial
        while previous != self.clusters:
            previous = self.clusters
            for cluster_index in list(self.clusters.keys()):
                if len(self.clusters[cluster_index]) == 0:
                    self.clusters.pop(cluster_index)
                    removed.append(cluster_index)
            self.getmidpoints()
            self.reassign_centers()
        for index in removed:
            self.clusters[index] = []
