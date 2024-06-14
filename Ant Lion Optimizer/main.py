from ALO import ALO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

SearchAgents_no = 40
Function_name = 'F1'
Max_iteration = 500
utils = Utils()

fobj, lb, ub, dim = utils.Get_Functions_details(Function_name)
alo_optimizer = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)
Best_score, Best_pos, cg_curve = alo_optimizer.optmize()

utils.func_plot(Function_name, Best_pos, 'Ant Lion Optimizer')

print(f'The best solution obtained by ALO is : {Best_pos}')
print(f'The best optimal value of the objective function found by ALO is : {Best_score}')