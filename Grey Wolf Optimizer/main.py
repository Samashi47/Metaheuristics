from GWO import GWO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

SearchAgents_no = 30
Function_name = 'F1'
Max_iteration = 500
utils = Utils()

fobj, lb, ub, dim = utils.Get_Functions_details(Function_name)
gwo_optmizer = GWO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)
Best_score, Best_pos, GWO_cg_curve = gwo_optmizer.optimize()

utils.func_plot(Function_name, Best_pos, 'Grey Wolf Optimizer')

print(f'The best solution obtained by GWO is : {Best_pos}')
print(f'The best optimal value of the objective function found by GWO is : {Best_score}')
