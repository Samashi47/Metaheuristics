from MVO import MVO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

Universes_no = 60
Function_name = 'F1'
Max_iteration = 500
utils = Utils()

fobj, lb, ub, dim = utils.Get_Functions_details(Function_name)
mvo_optimizer = MVO(Universes_no, Max_iteration, lb, ub, dim, fobj)
Best_score, Best_pos, cg_curve = mvo_optimizer.optimize()

utils.func_plot(Function_name, Best_pos, 'Multi-Verse Optimizer')

print(f'The best solution obtained by MVO is : {Best_pos}')
print(f'The best optimal value of the objective function found by MVO is : {Best_score}')
