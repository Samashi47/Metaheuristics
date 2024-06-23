import numpy as np
from GWO import GWO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

# Initialize and optimize using GWO
gwo = GWO(SearchAgents_no=100, Max_iter=1000, lb=-1, ub=1)
alpha_score, Bsol, convergence_curve = gwo.optimize_tsp('brg180')

print("Best distance:", alpha_score)
print("Best tour:", Bsol)
