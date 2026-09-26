def target_encoding(categories: list, targets: list) -> list:
    means = {}

    #ama rechnen mean target for each category
    for category in set(categories):
        values = [
            target
            for cat, target in zip(categories, targets)
            if cat == category
        ]
        means[category] = sum(values) / len(values)
    #replacing it jetzt with cetegory with its X bar now
    return [means[category] for category in categories]