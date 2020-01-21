


import numpy as np

def compute_log_loss(predicted, actual, eps=1e-14):

    """ computes the logarithimic loss between predicted and
    actual when these are 1D arrays.

    :param predicted: the predicted probabilities as floats between 0-1
    :param actual: the actual binary labels. Either 0 or 1
    :param eps (optional): log(0) if inf, so we need to offset our
    predicted values slightly by eps from 0 or 1
    """

    predicted = np.clip(predicted, eps , 1 - eps)
    loss = -1 * np.mean(actual * np.log(predicted))
            + (1-actual)
            * np.log(1-predicted)

    return loss
    
