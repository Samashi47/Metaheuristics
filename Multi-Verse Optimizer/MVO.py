import numpy as np
from RouletteWheelSelection import RouletteWheelSelection
import sys
sys.path.insert(1, 'common')
from initialization import initialization # type: ignore

def MVO(N, Max_time, lb, ub, dim, fobj):
    # Two variables for saving the position and inflation rate (fitness) of the best universe
    Best_universe = np.zeros(dim)
    Best_universe_Inflation_rate = float('inf')

    # Initialize the positions of universes
    Universes = initialization(N, dim, ub, lb)

    # Minimum and maximum of Wormhole Existence Probability (min and max in Eq.(3.3) in the paper
    WEP_Max = 1
    WEP_Min = 0.2

    Convergence_curve = np.zeros(Max_time)

    # Iteration(time) counter
    Time = 1

    # Main loop
    while Time < Max_time + 1:
        # Eq. (3.3) in the paper
        WEP = WEP_Min + Time * ((WEP_Max - WEP_Min) / Max_time)

        # Travelling Distance Rate (Formula): Eq. (3.4) in the paper
        TDR = 1 - ((Time) ** (1 / 6) / (Max_time) ** (1 / 6))

        # Inflation rates (I) (fitness values)
        Inflation_rates = np.zeros(Universes.shape[0])

        for i in range(Universes.shape[0]):
            # Boundary checking (to bring back the universes inside search space if they go beyond the boundaries
            Flag4ub = Universes[i, :] > ub
            Flag4lb = Universes[i, :] < lb
            Universes[i, :] = (Universes[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb

            # Calculate the inflation rate (fitness) of universes
            Inflation_rates[i] = fobj(Universes[i, :])

            # Elitism
            if Inflation_rates[i] < Best_universe_Inflation_rate:
                Best_universe_Inflation_rate = Inflation_rates[i]
                Best_universe = Universes[i, :]

        sorted_indexes = np.argsort(Inflation_rates)
        sorted_Inflation_rates = np.sort(Inflation_rates)

        Sorted_universes = np.zeros_like(Universes)
        for newindex in range(N):
            Sorted_universes[newindex, :] = Universes[sorted_indexes[newindex], :]
            
        # Normalized inflation rates (NI in Eq. (3.1) in the paper)
        normalized_sorted_Inflation_rates = sorted_Inflation_rates / np.linalg.norm(sorted_Inflation_rates)

        Universes[0, :] = Sorted_universes[0, :]

        # Update the Position of universes
        for i in range(1, Universes.shape[0]):  # Starting from 2 since the first one is the elite
            Back_hole_index = i
            for j in range(Universes.shape[1]):
                r1 = np.random.rand()
                if r1 < normalized_sorted_Inflation_rates[i]:
                    White_hole_index = RouletteWheelSelection(-sorted_Inflation_rates)  # for maximization problem -sorted_Inflation_rates should be written as sorted_Inflation_rates
                    if White_hole_index == -1:
                        White_hole_index = 0
                    # Eq. (3.1) in the paper
                    Universes[Back_hole_index, j] = Sorted_universes[White_hole_index, j]

                if len(lb) == 1:
                    # Eq. (3.2) in the paper if the boundaries are all the same
                    r2 = np.random.rand()
                    if r2 < WEP:
                        r3 = np.random.rand()
                        if r3 < 0.5:
                            Universes[i, j] = Best_universe[j] + TDR * ((ub - lb) * np.random.rand() + lb)
                        if r3 > 0.5:
                            Universes[i, j] = Best_universe[j] - TDR * ((ub - lb) * np.random.rand() + lb)

                if len(lb) != 1:
                    # Eq. (3.2) in the paper if the upper and lower bounds are different for each variables
                    r2 = np.random.rand()
                    if r2 < WEP:
                        r3 = np.random.rand()
                        if r3 < 0.5:
                            Universes[i, j] = Best_universe[j] + TDR * ((ub[j] - lb[j]) * np.random.rand() + lb[j])
                        if r3 > 0.5:
                            Universes[i, j] = Best_universe[j] - TDR * ((ub[j] - lb[j]) * np.random.rand() + lb[j])

        # Update the convergence curve
        Convergence_curve[Time - 1] = Best_universe_Inflation_rate

        # Print the best universe details after every 50 iterations
        if Time % 50 == 0:
            print('At iteration ', str(Time), ' the best universes fitness is ', str(Best_universe_Inflation_rate))

        Time = Time + 1

    return Best_universe_Inflation_rate, Best_universe, Convergence_curve
