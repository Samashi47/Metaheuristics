import numpy as np
from MVO import MVO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

# Initialize and optimize using MVO
mvo = MVO(N=200, Max_time=1000, lb=-1, ub=1)
alpha_score, Bsol, convergence_curve = mvo.optimize_tsp('eil51')

print("Best distance:", alpha_score)
print("Best tour:", Bsol)
