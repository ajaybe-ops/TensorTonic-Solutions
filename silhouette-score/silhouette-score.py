import numpy as np 

def silhouette_score(X: list, labels: list[int]) -> float:
    X = np.array(X, dtype=float)
    labels = np.array(labels)

    scores = []

    for i in range(len(X)):
        #what about points in the same cluster, excluding itself
        same_cluster = [
            j for j in range(len(X))
            if labels[j] == labels[i] and j != i
        ]

        #a(i): average that distance within its own cluster
        a = np.mean([
            np.linalg.norm(X[i] - X[j])
            for j in same_cluster
        ])

        #b(i): minimum average distance to another cluster here
        other_clusters = set(labels)
        other_clusters.remove(labels[i])

        distances = []

        for cluster in other_clusters:
            cluster_points = [
                j for j in range(len(X))
                if labels[j] == cluster
            ]

            avg_distance = np.mean([
                np.linalg.norm(X[i] - X[j])
                for j in cluster_points
            ])

            distances.append(avg_distance)

        b = min(distances)

        #setting silhouette score gerade for this point
        s = (b - a) / max(a, b)
        scores.append(s)

    #returning now mean silhouette score gerade
    return float(np.mean(scores))