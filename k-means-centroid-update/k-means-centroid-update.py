def k_means_centroid_update(
    points: list,
    assignments: list,
    k: int
) -> list:
    """
    Returns one updated centroid for each cluster.
    """

    if not points:
        return [[] for _ in range(k)]

    dimensions = len(points[0])

    centroids = []

    for cluster in range(k):

        cluster_points = [
            point
            for point, assignment in zip(points, assignments)
            if assignment == cluster
        ]

        if not cluster_points:
            centroids.append([0.0] * dimensions)
            continue

        centroid = [
            sum(point[d] for point in cluster_points)
            / len(cluster_points)
            for d in range(dimensions)
        ]

        centroids.append(centroid)

    return centroids