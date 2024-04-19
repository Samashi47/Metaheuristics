import numpy as np
import matplotlib.pyplot as plt
from MVO import MVO
import sys
sys.path.insert(1, 'common')
from Get_Functions_details import Get_Functions_details # type: ignore
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

# # Create figure
# fig, axs = plt.subplots(1, 2, figsize=(9, 4))

# # Draw the search space
# axs[0].func_plot(Function_name)
# axs[0].set_title('Test function')
# axs[0].set_xlabel('x_1')
# axs[0].set_ylabel('x_2')

# # Draw the convergence curve
# axs[1].semilogy(cg_curve, color='r')
# axs[1].set_title('Convergence curve')
# axs[1].set_xlabel('Iteration')
# axs[1].set_ylabel('Best score obtained so far')
# axs[1].legend(['MVO'])

# plt.tight_layout()
# plt.show()

print(f'The best solution obtained by MVO is : {Best_pos}')
print(f'The best optimal value of the objective function found by MVO is : {Best_score}')
