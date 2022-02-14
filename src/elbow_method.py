from kmeans import Kmeans
data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]
    
for k in range(1, 11):
    initial_clusters = {}
    for i in range(0, k):
        initial_clusters[i] = []
    for i in range(0, len(data)):
        initial_clusters[i % k].append(i)
    clusters = {}
    for i in range(0, len(initial_clusters)):
        clusters[i + 1] = initial_clusters[i]
    a = Kmeans(clusters, data)
    a.run()
    print(a.clusters)
    print(a.midpoint)
    print()
    for i in range(0, len(a.clusters)):
        distance = 0
        if len(a.clusters[i + 1]) == 0:
            distance += 0
        else:
            print(a.clusters[i+ 1])
            for j in range(0, len(a.clusters[i + 1])):
                distance += a.clusters[i + 1][j] - a.midpoint[i + 1][j]
        distance = distance ** (1/2)
    print(distance)
