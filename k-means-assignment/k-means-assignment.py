def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """

    assignments = []

    for point in points:
        distances = []

        for centroid in centroids:
            distance = sum(
                (p - c) ** 2
                for p, c in zip(point, centroid)
            )

            distances.append(distance)

        nearest_index = distances.index(min(distances))
        assignments.append(nearest_index)

    return assignments