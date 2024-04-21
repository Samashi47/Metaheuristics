import matplotlib.pyplot as plt
import numpy as np
from ALO import ALO
import sys
sys.path.insert(1, 'common')
from Get_Functions_details import Get_Functions_details # type: ignore

# Number of search agents
SearchAgents_no = 40

# Name of the test function that can be from F1 to F23 (Table 1,2,3 in the paper)
Function_name = 'F1'

# Maximum number of iterations
Max_iteration = 500

# Load details of the selected benchmark function
fobj, lb, ub, dim = Get_Functions_details(Function_name)

Best_score, Best_pos, cg_curve = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)

# # Create figure
# fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# # Draw search space
# axs[0].func_plot(Function_name)
# axs[0].set_title('Test function')
# axs[0].set_xlabel('x_1')
# axs[0].set_ylabel('x_2')
# axs[0].set_zlabel(f'{Function_name}( x_1 , x_2 )')
# axs[0].grid(False)

# # Draw objective space
# axs[1].semilogy(cg_curve, color='r')
# axs[1].set_title('Convergence curve')
# axs[1].set_xlabel('Iteration')
# axs[1].set_ylabel('Best score obtained so far')
# axs[1].axis('tight')
# axs[1].grid(False)
# axs[1].legend(['ALO'])

# plt.show()

print(f'The best solution obtained by ALO is : {Best_pos}')
print(f'The best optimal value of the objective function found by ALO is : {Best_score}')