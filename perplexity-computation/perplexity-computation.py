import math

def perplexity(prob_distribution, actual_tokens):
    log_sum = 0
    N = len(actual_tokens)

    for i in range(N):
        token = actual_tokens[i]
        probability = prob_distribution[i][token]
        log_sum += math.log(probability)

    cross_entropy = -log_sum / N
    return math.exp(cross_entropy)