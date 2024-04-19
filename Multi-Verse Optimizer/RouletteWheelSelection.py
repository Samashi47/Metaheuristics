import numpy as np

def RouletteWheelSelection(weights):
    accumulation = np.cumsum(weights)
    p = np.random.rand() * accumulation[-1]
    chosen_index = -1
    for index in range(len(accumulation)):
        if accumulation[index] > p:
            chosen_index = index
            break
    choice = chosen_index
    return choice
