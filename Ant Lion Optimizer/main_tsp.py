import numpy as np
from ALO import ALO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

# Initialize and optimize using ALO
alo = ALO(N=200, Max_iter=1000, lb=-1, ub=1)
alpha_score, Bsol, convergence_curve = alo.optimize_tsp('eil51')

print("Best distance:", alpha_score)
print("Best tour:", Bsol)
