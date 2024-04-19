import numpy as np

def initialization(SearchAgents_no, dim, ub, lb):
    # Boundary_no = len(ub)  # number of boundaries
    # If the boundaries of all variables are equal and user enter a single
    # number for both ub and lb
    if isinstance(ub, (int, float)):
        Positions = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb

    # If each variable has a different lb and ub
    if isinstance(ub, list):
        Positions = np.zeros((SearchAgents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            Positions[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

    return Positions
