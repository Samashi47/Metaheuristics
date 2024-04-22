import numpy as np

def Random_walk_around_antlion(Dim, max_iter, lb, ub, antlion, current_iter):
    lb = np.array(lb)
    ub = np.array(ub)
    antlion = np.array(antlion)

    # Ensure lb and ub are arrays
    if np.isscalar(lb):
        lb = np.ones(Dim) * lb
        ub = np.ones(Dim) * ub

    # Ensure lb and ub are 1D arrays
    lb = lb.flatten()
    ub = ub.flatten()

    # Adjusting the intensity I based on current iteration
    I = 1
    if current_iter > max_iter / 10:
        I = 1 + 100 * (current_iter / max_iter)
    if current_iter > max_iter / 2:
        I = 1 + 1000 * (current_iter / max_iter)
    if current_iter > max_iter * 0.75:
        I = 1 + 10000 * (current_iter / max_iter)
    if current_iter > max_iter * 0.9:
        I = 1 + 100000 * (current_iter / max_iter)
    if current_iter > max_iter * 0.95:
        I = 1 + 1000000 * (current_iter / max_iter)

    # Decrease boundaries to converge towards antlion
    lb = lb.astype(float)  # Convert lb to float
    ub = ub.astype(float)  # Convert ub to float
    lb /= I
    ub /= I

    # Move the interval of [lb, ub] around the antlion
    if np.random.rand() < 0.5:
        lb = lb + antlion
    else:
        lb = -lb + antlion

    if np.random.rand() >= 0.5:
        ub = ub + antlion
    else:
        ub = -ub + antlion

    RWs = np.zeros((max_iter + 1, Dim))

    # Create random walks and normalize according to lb and ub vectors
    for i in range(Dim):
        X = np.cumsum(2 * (np.random.rand(max_iter) > 0.5) - 1)
        X = np.insert(X, 0, 0)  # Inserting 0 at the start of the walk
        a = np.min(X)
        b = np.max(X)
        c = lb[i]
        d = ub[i]
        X_norm = ((X - a) * (d - c)) / (b - a) + c
        RWs[:, i] = X_norm

    return RWs
