def interaction_features(X: list) -> list:
    result = []

    for row in X:
        interactions = []

        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                interactions.append(row[i] * row[j])

        result.append(row + interactions)
        
    return result