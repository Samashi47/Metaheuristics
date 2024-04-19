import numpy as np
import sys
sys.path.insert(1, 'common')
from initialization import initialization

def GWO(SearchAgents_no, Max_iter, lb, ub, dim, fobj):
    # Initialize alpha, beta, and delta_pos
    Alpha_pos = np.zeros(dim)
    Alpha_score = float('inf')  # Change this to -inf for maximization problems

    Beta_pos = np.zeros(dim)
    Beta_score = float('inf')  # Change this to -inf for maximization problems

    Delta_pos = np.zeros(dim)
    Delta_score = float('inf')  # Change this to -inf for maximization problems

    # Initialize the positions of search agents
    Positions = initialization(SearchAgents_no, dim, ub, lb)

    Convergence_curve = np.zeros(Max_iter)

    l = 0  # Loop counter

    # Main loop
    while l < Max_iter:
        for i in range(np.shape(Positions)[0]):

            # Return back the search agents that go beyond the boundaries of the search space
            Flag4ub = Positions[i, :] > ub
            Flag4lb = Positions[i, :] < lb
            Positions[i, :] = (Positions[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb

            # Calculate objective function for each search agent
            fitness = fobj(Positions[i, :])

            # Update Alpha, Beta, and Delta
            if fitness < Alpha_score:
                Alpha_score = fitness  # Update alpha
                Alpha_pos = Positions[i, :]

            if fitness > Alpha_score and fitness < Beta_score:
                Beta_score = fitness  # Update beta
                Beta_pos = Positions[i, :]

            if fitness > Alpha_score and fitness > Beta_score and fitness < Delta_score:
                Delta_score = fitness  # Update delta
                Delta_pos = Positions[i, :]

        a = 2 - l * ((2) / Max_iter)  # a decreases linearly from 2 to 0

        # Update the Position of search agents including omegas
        for i in range(np.shape(Positions)[0]):
            for j in range(np.shape(Positions)[1]):

                r1 = np.random.rand()  # r1 is a random number in [0,1]
                r2 = np.random.rand()  # r2 is a random number in [0,1]

                A1 = 2 * a * r1 - a  # Equation (3.3)
                C1 = 2 * r2  # Equation (3.4)

                D_alpha = abs(C1 * Alpha_pos[j] - Positions[i, j])  # Equation (3.5)-part 1
                X1 = Alpha_pos[j] - A1 * D_alpha  # Equation (3.6)-part 1

                r1 = np.random.rand()
                r2 = np.random.rand()

                A2 = 2 * a * r1 - a  # Equation (3.3)
                C2 = 2 * r2  # Equation (3.4)

                D_beta = abs(C2 * Beta_pos[j] - Positions[i, j])  # Equation (3.5)-part 2
                X2 = Beta_pos[j] - A2 * D_beta  # Equation (3.6)-part 2

                r1 = np.random.rand()
                r2 = np.random.rand()

                A3 = 2 * a * r1 - a  # Equation (3.3)
                C3 = 2 * r2  # Equation (3.4)

                D_delta = abs(C3 * Delta_pos[j] - Positions[i, j])  # Equation (3.5)-part 3
                X3 = Delta_pos[j] - A3 * D_delta  # Equation (3.5)-part 3

                Positions[i, j] = (X1 + X2 + X3) / 3  # Equation (3.7)

        Convergence_curve[l] = Alpha_score
        l = l + 1

    return Alpha_score, Alpha_pos, Convergence_curve