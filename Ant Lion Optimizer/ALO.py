import numpy as np
from Random_walk_around_antlion import Random_walk_around_antlion
import sys
sys.path.insert(1, 'common')
from initialization import initialization # type: ignore
from RouletteWheelSelection import RouletteWheelSelection # type: ignore

import numpy as np

def ALO(N, Max_iter, lb, ub, dim, fobj):
    # Initialize the positions of antlions and ants
    antlion_position = initialization(N, dim, ub, lb)
    ant_position = initialization(N, dim, ub, lb)

    # Initialize variables to save the position of elite, sorted antlions, 
    # convergence curve, antlions fitness, and ants fitness
    Sorted_antlions = np.zeros((N, dim))
    Elite_antlion_position = np.zeros(dim)
    Elite_antlion_fitness = float('inf')
    Convergence_curve = np.zeros(Max_iter)
    antlions_fitness = np.zeros(N)
    ants_fitness = np.zeros(N)

    # Calculate the fitness of initial antlions and sort them
    for i in range(N):
        antlions_fitness[i] = fobj(antlion_position[i, :])

    sorted_indexes = np.argsort(antlions_fitness)
    sorted_antlion_fitness = antlions_fitness[sorted_indexes]
    Sorted_antlions = antlion_position[sorted_indexes, :]
    
    Elite_antlion_position = Sorted_antlions[0, :]
    Elite_antlion_fitness = sorted_antlion_fitness[0]

    # Main loop start from the second iteration since the first iteration 
    # was dedicated to calculating the fitness of antlions
    Current_iter = 1
    while Current_iter < Max_iter:
        
        # This for loop simulate random walks
        for i in range(N):
            # Select ant lions based on their fitness (the better anlion the higher chance of catching ant)
            Rolette_index = RouletteWheelSelection(1.0 / sorted_antlion_fitness)
            if Rolette_index == -1:
                Rolette_index = 0
            
            # RA is the random walk around the selected antlion by roulette wheel
            RA = Random_walk_around_antlion(dim, Max_iter, lb, ub, Sorted_antlions[Rolette_index, :], Current_iter)
            
            # RE is the random walk around the elite (best antlion so far)
            RE = Random_walk_around_antlion(dim, Max_iter, lb, ub, Elite_antlion_position, Current_iter)
            
            ant_position[i, :] = (RA[Current_iter, :] + RE[Current_iter, :]) / 2  # Equation (2.13) in the paper
        
        for i in range(N):
            # Boundary checking (bring back the antlions or ants inside search space if they go beyond the boundaries)
            Flag4ub = ant_position[i, :] > ub
            Flag4lb = ant_position[i, :] < lb
            ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            
            ants_fitness[i] = fobj(ant_position[i, :])
        
        # Update antlion positions and fitnesses based on the ants (if an ant 
        # becomes fitter than an antlion we assume it was caught by the antlion  
        # and the antlion update goes to its position to build the trap)
        double_population = np.vstack((Sorted_antlions, ant_position))
        double_fitness = np.concatenate((sorted_antlion_fitness, ants_fitness))
        
        I = np.argsort(double_fitness)
        double_sorted_population = double_population[I, :]
        
        antlions_fitness = double_fitness[I][:N]
        Sorted_antlions = double_sorted_population[:N, :]
        
        # Update the position of elite if any antlions becomes fitter than it
        if antlions_fitness[0] < Elite_antlion_fitness:
            Elite_antlion_position = Sorted_antlions[0, :]
            Elite_antlion_fitness = antlions_fitness[0]
        
        # Keep the elite in the population
        Sorted_antlions[0, :] = Elite_antlion_position
        antlions_fitness[0] = Elite_antlion_fitness
        
        # Update the convergence curve
        Convergence_curve[Current_iter] = Elite_antlion_fitness

        # Display the iteration and best optimum obtained so far
        if Current_iter % 50 == 0:
            print(f"At iteration {Current_iter} the elite fitness is {Elite_antlion_fitness}")

        Current_iter += 1

    return Elite_antlion_fitness, Elite_antlion_position, Convergence_curve


