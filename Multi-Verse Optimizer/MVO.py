import numpy as np
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

class MVO:
    def __init__(self, N, Max_time, lb, ub, dim, fobj):
        self.N = N
        self.Max_time = Max_time,
        self.Max_time = self.Max_time[0]
        self.lb = lb
        self.ub = ub
        self.dim = dim
        self.fobj = fobj
        self.utils = Utils()

    def optimize(self):
        # Two variables for saving the position and inflation rate (fitness) of the best universe
        Best_universe = np.zeros(self.dim)
        Best_universe_Inflation_rate = float('inf')

        # Initialize the positions of universes
        Universes = self.utils.initialization(self.N, self.dim, self.ub, self.lb)

        # Minimum and maximum of Wormhole Existence Probability (min and max in Eq.(3.3) in the paper
        WEP_Max = 1
        WEP_Min = 0.2

        Convergence_curve = np.zeros(self.Max_time)

        # Iteration(time) counter
        Time = 1

        # Main loop
        while Time < self.Max_time + 1:
            # Eq. (3.3) in the paper
            WEP = WEP_Min + Time * ((WEP_Max - WEP_Min) / self.Max_time)

            # Travelling Distance Rate (Formula): Eq. (3.4) in the paper
            TDR = 1 - ((Time) ** (1 / 6) / (self.Max_time) ** (1 / 6))

            # Inflation rates (I) (fitness values)
            Inflation_rates = np.zeros(Universes.shape[0])

            for i in range(Universes.shape[0]):
                # Boundary checking (to bring back the universes inside search space if they go beyond the boundaries
                Flag4ub = Universes[i, :] > self.ub
                Flag4lb = Universes[i, :] < self.lb
                Universes[i, :] = (Universes[i, :] * (~(Flag4ub + Flag4lb))) + self.ub * Flag4ub + self.lb * Flag4lb

                # Calculate the inflation rate (fitness) of universes
                Inflation_rates[i] = self.fobj(Universes[i, :])

                # Elitism
                if Inflation_rates[i] < Best_universe_Inflation_rate:
                    Best_universe_Inflation_rate = Inflation_rates[i]
                    Best_universe = Universes[i, :]

            sorted_indexes = np.argsort(Inflation_rates)
            sorted_Inflation_rates = np.sort(Inflation_rates)

            Sorted_universes = np.zeros_like(Universes)
            for newindex in range(self.N):
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
                        White_hole_index = self.utils.RouletteWheelSelection(-sorted_Inflation_rates)  # for maximization problem -sorted_Inflation_rates should be written as sorted_Inflation_rates
                        if White_hole_index == -1:
                            White_hole_index = 0
                        # Eq. (3.1) in the paper
                        Universes[Back_hole_index, j] = Sorted_universes[White_hole_index, j]

                    if isinstance(self.lb, (int, float)):
                        # Eq. (3.2) in the paper if the boundaries are all the same
                        r2 = np.random.rand()
                        if r2 < WEP:
                            r3 = np.random.rand()
                            if r3 < 0.5:
                                Universes[i, j] = Best_universe[j] + TDR * ((self.ub - self.lb) * np.random.rand() + self.lb)
                            if r3 > 0.5:
                                Universes[i, j] = Best_universe[j] - TDR * ((self.ub - self.lb) * np.random.rand() + self.lb)

                    if isinstance(self.lb, list):
                        # Eq. (3.2) in the paper if the upper and lower bounds are different for each variables
                        r2 = np.random.rand()
                        if r2 < WEP:
                            r3 = np.random.rand()
                            if r3 < 0.5:
                                Universes[i, j] = Best_universe[j] + TDR * ((self.ub[j] - self.lb[j]) * np.random.rand() + self.lb[j])
                            if r3 > 0.5:
                                Universes[i, j] = Best_universe[j] - TDR * ((self.ub[j] - self.lb[j]) * np.random.rand() + self.lb[j])

            # Update the convergence curve
            Convergence_curve[Time - 1] = Best_universe_Inflation_rate

            # Print the best universe details after every 50 iterations
            if Time % 50 == 0:
                print('At iteration ', str(Time), ' the best universes fitness is ', str(Best_universe_Inflation_rate))

            Time = Time + 1

        return Best_universe_Inflation_rate, Best_universe, Convergence_curve
