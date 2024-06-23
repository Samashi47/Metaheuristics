import numpy as np
import plotly.graph_objects as go
import tsplib95 as tsp

class Utils:
    def traceTour(self, problem, solution, index):
        if problem.edge_weight_type != "EXPLICIT" or (problem.edge_weight_format == "LOWER_DIAG_ROW" and problem.display_data_type == "TWOD_DISPLAY"):
                return problem.trace_tours([solution[index, :] + 1])[0]
        else:
            return problem.trace_tours([solution[index, :]])[0]
        
    def LoadProblem(self, problem='eil51'):
        try:
            tsplib = tsp.load('tsp_problems/' + problem + '.tsp')
            return tsplib
        except FileNotFoundError:
            print(f"File {problem}.tsp not found in tsp_problems directory.")
            return None
        
    def RouletteWheelSelection(self, weights):
        accumulation = np.cumsum(weights)
        p = np.random.rand() * accumulation[-1]
        chosen_index = -1
        for index in range(len(accumulation)):
            if accumulation[index] > p:
                chosen_index = index
                break
        choice = chosen_index
        return choice
    
    def initialization(self, SearchAgents_no, dim, ub, lb):
        # Boundary_no = len(ub)  # number of boundaries
        # If the boundaries of all variables are equal and user enter a single
        # number for both ub and lb
        if isinstance(ub, (int, float)):
            Positions = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb

        # If each variable has a different lb and ub
        if isinstance(ub, list):
            Positions = np.zeros((SearchAgents_no, dim))
            for i in range(dim):
                ub_i = ub[i]
                lb_i = lb[i]
                Positions[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

        return Positions
    
    def Get_Functions_details(self, F):
        switcher = {
            'bentCigar': (self.bentCigar, -100, 100, 3),
            'zakharov': (self.zakharov, -100, 100, 3),
            'rosenbrock': (self.rosenbrock, -100, 100, 3),
            'rastrigin': (self.rastrigin, -100, 100, 3),
            'schafferF6': (self.schafferF6, -100, 100, 3),
            'levy': (self.levy, -100, 100, 3),
            'HighConditionedElliptic': (self.HighConditionedElliptic, -100, 100, 3),
            'discus': (self.discus, -100, 100, 3),
            'ackley': (self.ackley, -100, 100, 3),
            'weierstrass': (self.weierstrass, -100, 100, 3),
            'griewank': (self.griewank, -100, 100, 3),
            'happyCat': (self.happyCat, -100, 100, 3),
            'F1': (self.F1, -100, 100, 30),
            'F2': (self.F2, -10, 10, 30),
            'F3': (self.F3, -100, 100, 30),
            'F4': (self.F4, -100, 100, 30),
            'F5': (self.F5, -30, 30, 30),
            'F6': (self.F6, -100, 100, 30),
            'F7': (self.F7, -1.28, 1.28, 30),
            'F8': (self.F8, -500, 500, 30),
            'F9': (self.F9, -5.12, 5.12, 30),
            'F10': (self.F10, -32, 32, 30),
            'F11': (self.F11, -600, 600, 30),
            'F12': (self.F12, -50, 50, 30),
            'F13': (self.F13, -50, 50, 30),
            'F14': (self.F14, -65.536, 65.536, 2),
            'F15': (self.F15, -5, 5, 4),
            'F16': (self.F16, -5, 5, 2),
            'F17': (self.F17, [-5,0], [10,15], 2),
            'F18': (self.F18, -2, 2, 2),
            'F19': (self.F19, 0, 1, 3),
            'F20': (self.F20, 0, 1, 6),
            'F21': (self.F21, 0, 10, 4),
            'F22': (self.F22, 0, 10, 4),
            'F23': (self.F23, 0, 10, 4)
        }
        return switcher.get(F, "Invalid function")
    
    def bentCigar(self, x):
        x = np.array(x).ravel()
        return x[0]**2 + 10**6 * np.sum(x[1:]**2)
    
    def zakharov(self, x):
        x = np.array(x).ravel()
        return np.sum(x**2) + (np.sum(0.5*x))**2 + (np.sum(0.5*x))**4
    
    def rosenbrock(self, x):
        x = np.array(x).ravel()
        return np.sum(100*(x[:-1]**2 - x[1:])**2 + (x[:-1])**2 - 1)
    
    def rastrigin(self, x):
        x = np.array(x)
        return np.sum(np.array(x)**2 - 10*np.cos(2*np.pi*x) + 10)
    
    def schafferHelper(self, x, y):
        x, y = np.array(x).ravel(), np.array(y).ravel()
        return 0.5 + ((np.sin(np.sqrt(x**2 - y**2))**2 - 0.5) / (1 + 0.001*(x**2 + y**2))**2)
    
    def schafferF6(self, x):
        x = np.array(x).ravel()
        return np.sum(self.schafferHelper(x[:-1], x[1:]))
    
    def levyW(self, x):
        return 1 + (x-1)/4
    
    def levy(self, x):
        x = np.array(x).ravel()
        w = self.levyW(x)
        return (np.sin(np.pi*w[0])**2 + np.sum((w[:-1]-1)**2 * (1 + 10*(np.sin(np.pi*w[:-1]+1)**2))) + (w[-1]-1)**2 * (1 + (np.sin(2*np.pi*w[-1])**2)))
        
    def HighConditionedElliptic(self, x):
        x = np.array(x).ravel()
        return np.sum(10**6**(np.arange(len(x)-1)/(len(x)-1)) * x[:-1]**2)
    
    def discus(self, x):
        x = np.array(x).ravel()
        return (10**6)*x[0] + np.sum(x[1:]**2)
    
    def ackley(self, x):
        dim = len(x)
        x = np.array(x).ravel()
        return -20*np.exp(-0.2*np.sqrt(np.sum(x**2)/dim)) - np.exp(np.sum(np.cos(2*np.pi*x))/dim) + 20 + np.exp(1)
    
    def weierstrass(self, x):
        a, b, kmax = 0.5, 3, 20
        return np.sum([np.sum([a**k * np.cos(2*np.pi*b**k*(x[i]+0.5)) for k in range(kmax)]) - np.sum([a**k * np.cos(2*np.pi*b**k*0.5) for k in range(kmax)])for i in range(len(x))])
    
    def griewank(self, x):
        x = np.array(x).ravel()
        return np.sum(x**2/4000) - np.prod(np.cos(x/np.sqrt(np.arange(1, len(x)+1)))) + 1
    
    def happyCat(self, x):
        dim = len(x)
        x = np.array(x).ravel()
        return np.abs(np.sum(x**2) - dim)**(1/4) + (0.5*np.sum(x**2) + np.sum(x))/dim + 0.5
    
    def F5(self, x):
        dim = len(x)
        x = np.array(x)
        return np.sum(100*(x[1:dim]-(x[0:dim-1]**2))**2 + (x[0:dim-1]-1)**2)
    
    def Ufun(x, a, k, m):
        return k*((x-a)**m)*(x>a) + k*((-x-a)**m)*(x<(-a))
    
    def F1(self, x):
        return np.sum(np.array(x)**2)

    def F2(self, x):
        return np.sum(np.abs(x)) + np.prod(np.abs(x))

    def F3(self, x):
        dim = len(x)
        return np.sum([np.sum(x[:i+1])**2 for i in range(dim)])

    def F4(self, x):
        return np.max(np.abs(x))


    def F6(self, x):
        x = np.array(x)
        return np.sum(np.abs((x+.5))**2)

    def F7(self, x):
        dim = len(x)
        return np.sum([(i+1)*(x[i]**4) for i in range(dim)]) + np.random.rand()

    def F8(self, x):
        x = np.array(x)
        return np.sum(-x*np.sin(np.sqrt(np.abs(x))))

    def F9(self, x):
        dim = len(x)
        x = np.array(x)
        return np.sum(np.array(x)**2 - 10*np.cos(2*np.pi*x)) + 10*dim

    def F10(self, x):
        dim = len(x)
        x = np.array(x)
        return -20*np.exp(-0.2*np.sqrt(np.sum(x**2)/dim)) - np.exp(np.sum(np.cos(2*np.pi*x))/dim) + 20 + np.exp(1)

    def F11(self, x):
        dim = len(x)
        x = np.array(x)
        return np.sum(np.array(x)**2)/4000 - np.prod(np.cos(x/np.sqrt([i+1 for i in range(dim)]))) + 1

    def F12(self, x):
        dim = len(x)
        x = np.array(x)
        return (np.pi/dim)*(10*((np.sin(np.pi*(1+(x[0]+1)/4)))**2) + np.sum((((x[0:dim-1]+1)/4)**2)*(1+10*((np.sin(np.pi*(1+(x[1:dim]+1)/4))))**2) + ((x[dim-1]+1)/4)**2) )+ np.sum(self.Ufun(x,10,100,4))

    def F13(self, x):
        dim = len(x)
        x = np.array(x)
        return 0.1*((np.sin(3*np.pi*x[0]))**2 + np.sum((x[0:dim-1]-1)**2*(1+(np.sin(3*np.pi*x[1:dim]))**2)) + ((x[dim-1]-1)**2)*(1+(np.sin(2*np.pi*x[dim-1]))**2)) + np.sum(self.Ufun(x,5,100,4))

    def F14(self, x):
        x = np.array(x)
        aS = np.array([[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
                    [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]])
        bS = [np.sum((x-aS[:,j])**6) for j in range(25)]
        return (1/500+np.sum(1/np.array([i+1 for i in range(25)]+bS)))**(-1)

    def F15(self, x):
        x = np.array(x)
        aK = [0.1957, 0.1947, 0.1735, 0.16, 0.0844, 0.0627, 0.0456, 0.0342, 0.0323, 0.0235, 0.0246]
        bK = [0.25, 0.5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
        bK = 1/np.array(bK)
        return np.sum((aK-((x[0]*(bK**2+x[1]*bK))/(bK**2+x[2]*bK+x[3])))**2)

    def F16(self, x):
        x = np.array(x)
        return 4*(x[0]**2)-2.1*(x[0]**4)+(x[0]**6)/3+x[0]*x[1]-4*(x[1]**2)+4*(x[1]**4)

    def F17(self, x):
        x = np.array(x)
        return (x[1]-(x[0]**2)*5.1/(4*(np.pi**2))+5/np.pi*x[0]-6)**2+10*(1-1/(8*np.pi))*np.cos(x[0])+10

    def F18(self, x):
        x = np.array(x)
        return (1+(x[0]+x[1]+1)**2*(19-14*x[0]+3*(x[0]**2)-14*x[1]+6*x[0]*x[1]+3*x[1]**2))*(30+(2*x[0]-3*x[1])**2*(18-32*x[0]+12*(x[0]**2)+48*x[1]-36*x[0]*x[1]+27*(x[1]**2)))

    def F19(self, x):
        x = np.array(x)
        aH = np.array([[3, 10, 30], [0.1, 10, 35], [3, 10, 30], [0.1, 10, 35]])
        cH = [1, 1.2, 3, 3.2]
        pH = np.array([[0.3689, 0.117, 0.2673], [0.4699, 0.4387, 0.747], [0.1091, 0.8732, 0.5547], [0.03815, 0.5743, 0.8828]])
        return np.sum([cH[i]*np.exp(-(np.sum(aH[i,:]*((x-pH[i,:])**2)))) for i in range(4)])

    def F20(self, x):
        x = np.array(x)
        aH = np.array([[10, 3, 17, 3.5, 1.7, 8], [0.05, 10, 17, 0.1, 8, 14], [3, 3.5, 1.7, 10, 17, 8], [17, 8, 0.05, 10, 0.1, 14]])
        cH = np.array([1, 1.2, 3, 3.2])
        pH = np.array([[0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886], [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991], [0.2348, 0.1415, 0.3522, 0.2883, 0.3047, 0.6650], [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381]])
        return np.sum([-cH[i]*np.exp(-np.sum(aH[i,:]*((x-pH[i,:])**2))) for i in range(4)])

    def F21(self, x):
        x = np.array(x)
        aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7]])
        cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4])
        return np.sum([-((x-aSH[i,:])@(x-aSH[i,:])+cSH[i])**(-1) for i in range(5)])

    def F22(self, x):
        x = np.array(x)
        aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3]])
        cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3])
        return np.sum([-((x-aSH[i,:])@(x-aSH[i,:])+cSH[i])**(-1) for i in range(7)])

    def F23(self, x):
        x = np.array(x)
        aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
        cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
        return np.sum([-((x-aSH[i,:])@(x-aSH[i,:])+cSH[i])**(-1) for i in range(10)])

    def func_plot(self, func_name,Best_pos,algo_name):
        fobj, lb, ub, dim = self.Get_Functions_details(func_name)
        if func_name in ['bentCigar', 'zakharov', 'rosenbrock', 'rastrigin', 'schafferF6',
         'levy', 'HighConditionedElliptic', 'discus', 'ackley', 'weierstrass',
         'griewank', 'happyCat']:
            x = y = np.arange(-100, 101, 1)
        elif func_name in ['F1', 'F2', 'F3', 'F4', 'F6', 'F14']:
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
                    
        fig = go.Figure(data=[go.Surface(z=f, x=x, y=y, colorscale="Reds", opacity=0.5)])
        fig.add_trace(go.Scatter3d(x=[Best_pos[0]], y=[Best_pos[1]], z=[fobj(Best_pos)],
                                mode='markers', marker=dict(color='blue', size=5), name=f'Optimum Found using {algo_name}'))
        fig.update_layout(
            title= f'Plot for function {func_name} and optimum found using {algo_name}',
            autosize=False,
            width=750, 
            height=750,
            margin=dict(l=65, r=50, b=65, t=90), 
            scene_aspectmode='cube',
            scene=dict(
                xaxis=dict(title='X'),
                yaxis=dict(title='Y'),
                zaxis=dict(title='Z')
            )
        )
        fig.show()