def decision_tree_split(X: list, y: list) -> list:
    def gini(labels):
        if not labels:
            return 0

        counts = {}
        for label in labels:
            counts[label] = counts.get(label, 0) + 1

        n = len(labels)
        return 1 - sum((count / n) ** 2 for count in counts.values())

    parent_gini = gini(y)

    best_gain = -1
    best_feature = None
    best_threshold = None

    n_features = len(X[0])

    for feature in range(n_features):
        values = sorted(set(row[feature] for row in X))

        for i in range(len(values) - 1):
            threshold = (values[i] + values[i + 1]) / 2

            left_y = []
            right_y = []

            for row, label in zip(X, y):
                if row[feature] <= threshold:
                    left_y.append(label)
                else:
                    right_y.append(label)

            if not left_y or not right_y:
                continue

            weighted_gini = (
                len(left_y) / len(y) * gini(left_y)
                + len(right_y) / len(y) * gini(right_y)
            )

            gain = parent_gini - weighted_gini

            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

    return [best_feature, best_threshold]