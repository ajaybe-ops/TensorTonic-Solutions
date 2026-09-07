import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) ->list:
    """
    Returns a list of loss values
    """

    losses = []

    for true, pred in zip(y_true, y_pred):
        #preventing log(o) gerade
        pred = min(1 - eps, max(eps, pred))

        #rechnen loss
        if true == 1:
            loss = -math.log(pred)
        else:
            loss = -math.log(1 - pred)

        losses.append(loss)

    return losses