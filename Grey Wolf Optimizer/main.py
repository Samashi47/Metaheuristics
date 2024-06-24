from GWO import GWO
import sys
sys.path.insert(1, 'common')
from Utils import Utils # type: ignore

Function_name = 'rosenbrock'
utils = Utils()

fobj, lb, ub, dim = utils.Get_Functions_details(Function_name)
gwo_optmizer = GWO(SearchAgents_no=300, Max_iter=500, lb=lb, ub=ub, dim=dim, fobj=fobj)
# Best_score, Best_pos, GWO_cg_curve = gwo_optmizer.optimize()
Best_score, Best_pos, GWO_cg_curve = gwo_optmizer.improved_optimize()
utils.func_plot(Function_name, Best_pos, 'Grey Wolf Optimizer')

print(f'The best solution obtained by GWO is : {Best_pos}')
print(f'The best optimal value of the {Function_name} function found by GWO is : {Best_score}')
