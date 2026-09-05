import numpy as np
from typing import List
def roc_curve(y_true: list, y_score: list) -> dict:
    """
    Returns a dictionary with fpr, tpr, and thresholds.
    """
    y_true = np.array(y_true)
    y_score = np.array(y_score)

    #sorting scores in descending order
    order =  np.argsort(-y_score)
    y_true = y_true[order]
    y_score = y_score[order]

    #total postives and negatives
    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    #anfangen with the threshold gerade zum infinity
    fpr = [0.0]
    tpr = [0.0]
    thresholds = [np.inf]

    tp = 0
    fp = 0

    i = 0

    #so i am gonna process ein unique score group at a zeit
    while i < len(y_score):
        score = y_score[i]

        #all done, lassen wir uns process all samples with the same score
        while i < len(y_score) and y_score[i] == score:
            if y_true[i] == 1:
                tp += 1
            else:
                fp += 1
            i += 1
        #lassen Wir uns TPR and FPR rechnen
        tpr.append(tp / P)
        fpr.append(fp / N)
        thresholds.append(score)

    return {
        "fpr": np.array(fpr),
        "tpr": np.array(tpr),
        "thresholds": np.array(thresholds)
    }
    pass