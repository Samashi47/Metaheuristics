from ALO import ALO
import sys
sys.path.insert(1, 'common')
from Get_Functions_details import Get_Functions_details # type: ignore
from func_plot import func_plot # type: ignore

# Number of search agents
SearchAgents_no = 40

# Name of the test function that can be from F1 to F23 (Table 1,2,3 in the paper)
Function_name = 'F1'

# Maximum number of iterations
Max_iteration = 500

# Load details of the selected benchmark function
fobj, lb, ub, dim = Get_Functions_details(Function_name)

Best_score, Best_pos, cg_curve = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)

# Create function plot
func_plot(Function_name, Best_pos, 'Ant Lion Optimizer')

print(f'The best solution obtained by ALO is : {Best_pos}')
print(f'The best optimal value of the objective function found by ALO is : {Best_score}')