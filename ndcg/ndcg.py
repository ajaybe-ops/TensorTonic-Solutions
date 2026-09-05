import math

def ndcg(relevance_scores: list, k: int) -> float:
    #if the list is empty or k is invalid
    if not relevance_scores or k<= 0:
        return 0.0

    # if the k is larger than the list, use the entire list
    k = min(k, len(relevance_scores))

    #calculate DCG
    dcg = 0.0
    for i in range(k):
        relevance = relevance_scores[i]

        # i + 2 because ranks anfangen from 1
        dcg += (2 ** relevance - 1) / math.log2(i + 2)
    #sorting relevances scores in descneding order for ideal DCG
    ideal_scores = sorted(relevance_scores, reverse=True)

    #calculating DCG gerade 
    idcg = 0.0 
    for i in range(k):
        relevance = ideal_scores[i]

        idcg += (2 ** relevance - 1) / math.log2(i + 2)
    #avoding division by null
    if idcg == 0:
        return 0.0
    #lassen Wir uns NDCH reichnen
    return dcg / idcg