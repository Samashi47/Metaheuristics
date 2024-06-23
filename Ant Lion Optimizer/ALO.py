import numpy as np
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore
class ALO:
    def __init__(self, N=50, Max_iter=100, lb=-5, ub=5, dim=0, fobj='bentCigar'):
        self.N = N
        self.Max_iter = Max_iter
        self.lb = lb
        self.ub = ub
        self.dim = dim
        self.fobj = fobj
        self.utils = Utils()
        
    def optmize(self):
        antlion_position = self.utils.initialization(self.N, self.dim, self.ub, self.lb)
        ant_position = self.utils.initialization(self.N, self.dim, self.ub, self.lb)

        Sorted_antlions = np.zeros((self.N, self.dim))
        Elite_antlion_position = np.zeros(self.dim)
        Elite_antlion_fitness = float('inf')
        Convergence_curve = np.zeros(self.Max_iter)
        antlions_fitness = np.zeros(self.N)
        ants_fitness = np.zeros(self.N)

        for i in range(self.N):
            antlions_fitness[i] = self.fobj(antlion_position[i, :])

        sorted_indexes = np.argsort(antlions_fitness)
        sorted_antlion_fitness = antlions_fitness[sorted_indexes]
        Sorted_antlions = antlion_position[sorted_indexes, :]
        
        Elite_antlion_position = Sorted_antlions[0, :]
        Elite_antlion_fitness = sorted_antlion_fitness[0]

        Current_iter = 1
        while Current_iter < self.Max_iter:
            
            for i in range(self.N):
                Rolette_index = self.utils.RouletteWheelSelection(1.0 / sorted_antlion_fitness)
                if Rolette_index == -1:
                    Rolette_index = 0
                
                RA = self.Random_walk_around_antlion(self.dim, self.Max_iter, self.lb, self.ub, Sorted_antlions[Rolette_index, :], Current_iter)
                
                RE = self.Random_walk_around_antlion(self.dim, self.Max_iter, self.lb, self.ub, Elite_antlion_position, Current_iter)
                
                ant_position[i, :] = (RA[Current_iter, :] + RE[Current_iter, :]) / 2
            
            for i in range(self.N):
                Flag4ub = ant_position[i, :] > self.ub
                Flag4lb = ant_position[i, :] < self.lb
                ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + self.ub * Flag4ub + self.lb * Flag4lb
                
                ants_fitness[i] = self.fobj(ant_position[i, :])
            
            double_population = np.vstack((Sorted_antlions, ant_position))
            double_fitness = np.concatenate((sorted_antlion_fitness, ants_fitness))
            
            I = np.argsort(double_fitness)
            double_sorted_population = double_population[I, :]
            
            antlions_fitness = double_fitness[I][:self.N]
            Sorted_antlions = double_sorted_population[:self.N, :]
            
            if antlions_fitness[0] < Elite_antlion_fitness:
                Elite_antlion_position = Sorted_antlions[0, :]
                Elite_antlion_fitness = antlions_fitness[0]
            
            Sorted_antlions[0, :] = Elite_antlion_position
            antlions_fitness[0] = Elite_antlion_fitness
            
            Convergence_curve[Current_iter] = Elite_antlion_fitness

            if Current_iter % 50 == 0:
                print(f"At iteration {Current_iter} the elite fitness is {Elite_antlion_fitness}")

            Current_iter += 1

        return Elite_antlion_fitness, Elite_antlion_position, Convergence_curve

    def Random_walk_around_antlion(self, Dim, max_iter, lb, ub, antlion, current_iter):
        lb = np.array(lb)
        ub = np.array(ub)
        antlion = np.array(antlion)

        if np.isscalar(lb):
            lb = np.ones(Dim) * lb
            ub = np.ones(Dim) * ub

        lb = lb.flatten()
        ub = ub.flatten()

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

        lb = lb.astype(float)
        ub = ub.astype(float)
        lb /= I
        ub /= I

        if np.random.rand() < 0.5:
            lb = lb + antlion
        else:
            lb = -lb + antlion

        if np.random.rand() >= 0.5:
            ub = ub + antlion
        else:
            ub = -ub + antlion

        RWs = np.zeros((max_iter + 1, Dim))

        for i in range(Dim):
            X = np.cumsum(2 * (np.random.rand(max_iter) > 0.5) - 1)
            X = np.insert(X, 0, 0)
            a = np.min(X)
            b = np.max(X)
            c = lb[i]
            d = ub[i]
            X_norm = ((X - a) * (d - c)) / (b - a) + c
            RWs[:, i] = X_norm

        return RWs

    def optimize_tsp(self, problem):
        problem = self.utils.LoadProblem(problem)
        
        if problem == None:
            print("Could not load TSP problem!!")
            
        dim = problem.dimension
        
        antlion_position = self.utils.initialization(self.N, dim, self.ub, self.lb)
        ant_position = self.utils.initialization(self.N, dim, self.ub, self.lb)

        Sorted_antlions = np.zeros((self.N, dim))
        Elite_antlion_position = np.zeros(dim)
        Elite_antlion_fitness = float('inf')
        Convergence_curve = np.zeros(self.Max_iter)
        antlions_fitness = np.zeros(self.N)
        ants_fitness = np.zeros(self.N)

        for i in range(self.N):
            sol = np.argsort(antlion_position, axis=1)
            antlions_fitness[i] = problem.trace_tours([sol[i, :] + 1])[0]

        sorted_indexes = np.argsort(antlions_fitness)
        sorted_antlion_fitness = antlions_fitness[sorted_indexes]
        Sorted_antlions = antlion_position[sorted_indexes, :]
        
        Elite_antlion_position = Sorted_antlions[0, :]
        Elite_antlion_fitness = sorted_antlion_fitness[0]

        Current_iter = 1
        while Current_iter < self.Max_iter:
            
            for i in range(self.N):
                Rolette_index = self.utils.RouletteWheelSelection(1.0 / sorted_antlion_fitness)
                if Rolette_index == -1:
                    Rolette_index = 0
                
                RA = self.Random_walk_around_antlion(dim, self.Max_iter, self.lb, self.ub, Sorted_antlions[Rolette_index, :], Current_iter)
                
                RE = self.Random_walk_around_antlion(dim, self.Max_iter, self.lb, self.ub, Elite_antlion_position, Current_iter)
                
                ant_position[i, :] = (RA[Current_iter, :] + RE[Current_iter, :]) / 2  # Equation (2.13) in the paper
            
            for i in range(self.N):
                Flag4ub = ant_position[i, :] > self.ub
                Flag4lb = ant_position[i, :] < self.lb
                ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + self.ub * Flag4ub + self.lb * Flag4lb
                sol = np.argsort(ant_position, axis=1)
                ants_fitness[i] = problem.trace_tours([sol[i, :] + 1])[0]
            
            double_population = np.vstack((Sorted_antlions, ant_position))
            double_fitness = np.concatenate((sorted_antlion_fitness, ants_fitness))
            
            I = np.argsort(double_fitness)
            double_sorted_population = double_population[I, :]
            
            antlions_fitness = double_fitness[I][:self.N]
            Sorted_antlions = double_sorted_population[:self.N, :]
            
            if antlions_fitness[0] < Elite_antlion_fitness:
                Elite_antlion_position = Sorted_antlions[0, :].copy()
                Elite_antlion_fitness = antlions_fitness[0]
            
            Sorted_antlions[0, :] = Elite_antlion_position
            antlions_fitness[0] = Elite_antlion_fitness
            
            Convergence_curve[Current_iter] = Elite_antlion_fitness
            Bsol = np.argsort(Elite_antlion_position)
            if Current_iter % 50 == 0:
                print(f"At iteration {Current_iter} the elite fitness is {Elite_antlion_fitness}")
                print(f"Best Solution: {Bsol}")
            Current_iter += 1

        return Elite_antlion_fitness, Bsol, Convergence_curve