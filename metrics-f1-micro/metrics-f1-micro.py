def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    tp = 0 #starting from null here, counted nicht
    fp = 0
    fn = 0

    for true, pred in zip(y_true, y_pred): #pairing all value gemainsam
        if true == pred:
            tp += 1
        else:
            fp += 1
            fn += 1
    denominator = 2 * tp + fp + fn

    if denominator == 0:
        return 0.0
    return round((2 * tp) / denominator, 4)