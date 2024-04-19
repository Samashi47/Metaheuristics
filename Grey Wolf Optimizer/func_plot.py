import numpy as np
import matplotlib.pyplot as plt
from Get_Functions_details import Get_Functions_details
def func_plot(func_name):
    lb, ub, dim, fobj = Get_Functions_details(func_name)

    if func_name in ['F1', 'F2', 'F3', 'F4', 'F6', 'F14']:
        x = y = np.arange(-100, 101, 2)
    elif func_name == 'F5':
        x = y = np.arange(-200, 201, 2)
    elif func_name == 'F7':
        x = y = np.arange(-1, 1.01, 0.03)
    elif func_name in ['F8', 'F11']:
        x = y = np.arange(-500, 501, 10)
    elif func_name in ['F9', 'F15', 'F17', 'F19', 'F20', 'F21', 'F22', 'F23']:
        x = y = np.arange(-5, 5.1, 0.1)
    elif func_name == 'F10':
        x = y = np.arange(-20, 20.1, 0.5)
    elif func_name == 'F12':
        x = y = np.arange(-10, 10.1, 0.1)
    elif func_name == 'F13':
        x = y = np.arange(-5, 5.01, 0.08)
    elif func_name == 'F16':
        x = y = np.arange(-1, 1.01, 0.01)
    elif func_name == 'F18':
        x = y = np.arange(-5, 5.01, 0.06)

    L = len(x)
    f = np.zeros((L, L))

    for i in range(L):
        for j in range(L):
            if func_name not in ['F15', 'F19', 'F20', 'F21', 'F22', 'F23']:
                f[i, j] = fobj([x[i], y[j]])
            if func_name == 'F15':
                f[i, j] = fobj([x[i], y[j], 0, 0])
            if func_name == 'F19':
                f[i, j] = fobj([x[i], y[j], 0])
            if func_name == 'F20':
                f[i, j] = fobj([x[i], y[j], 0, 0, 0, 0])
            if func_name in ['F21', 'F22', 'F23']:
                f[i, j] = fobj([x[i], y[j], 0, 0])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, f, rstride=1, cstride=1, color='c', alpha=0.6, linewidth=0)
    plt.show()