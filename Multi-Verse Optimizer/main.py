from MVO import MVO
import sys
sys.path.insert(1, 'common')
from Get_Functions_details import Get_Functions_details # type: ignore
from func_plot import func_plot # type: ignore

# Number of search agents (universes)
Universes_no = 60

# Name of the test function that can be from F1 to F23 (Table 1,2,3 in the paper)
Function_name = 'F17'

# Maximum number of iterations
Max_iteration = 500

# Load details of the selected benchmark function
fobj, lb, ub, dim = Get_Functions_details(Function_name)

# Run MVO
Best_score, Best_pos, cg_curve = MVO(Universes_no, Max_iteration, lb, ub, dim, fobj)

# Create function plot

func_plot(Function_name, Best_pos, 'Multi-Verse Optimizer')

print(f'The best solution obtained by MVO is : {Best_pos}')
print(f'The best optimal value of the objective function found by MVO is : {Best_score}')
