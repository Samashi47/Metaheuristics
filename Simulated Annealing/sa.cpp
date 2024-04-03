#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <climits>
#include <random> // Added missing include directive for the <random> library

#define maxITER 1000

using namespace std;

double f1(vector<double> x)
{
    return pow(x[0], 3) - 60*pow(x[0], 2) + 900*x[0] + 100;
}

double uniform_rand()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> d(0, 1);
    return d(gen);
}

vector<double> generate(double upper, double lower, int dim)
{
    vector<double> x(dim); // Initialize the vector x with the correct size
    double alpha = uniform_rand();
    for (int i = 0; i < dim; i++)
    {
        x[i] = (lower + alpha * (upper - lower));
    }
    return x;
}
vector<double> gneighbor(vector<double> x)
{
    vector<double> neighbor = x;
    double alpha = uniform_rand();
    double epsilon = uniform_rand() / RAND_MAX;
    for (int i = 0; i < x.size(); i++)
    {
        neighbor[i] += (2 * epsilon - 1) * alpha;
    }
    return neighbor;
}
double prob(double delta, double T)
{
    if (delta < 0)
        return 1;
    return exp(-delta / T);
}
vector<double> SA(double upper, double lower, double Tmax, double Tmin, int dim)
{
    vector<double> x_0 = generate(upper, lower, dim);
    vector<double> neighbor, best;
    double fitness, fitness_best, fitness_x0;
    fitness = f1(x_0);
    best = x_0;
    fitness_best = fitness;
    double T = Tmax;
    for(int i = 0; i < maxITER; i++)
    {
        neighbor = gneighbor(x_0);
        fitness_x0 = f1(x_0);
        double delta = f1(neighbor) - fitness_x0;
        if (prob(delta, T) > uniform_rand())
        {
            x_0 = neighbor;
            fitness_x0 = f1(x_0);
        }
        double cool = pow(Tmax / Tmin, 1 / maxITER);
        T *= cool;
    }
    return best;
}

int main()
{
    int dim = 2;
    double upper = 20;
    double lower = -20;
    double Tmax = 100;
    double Tmin = 0.1;
    vector<double> best = SA(upper, lower, Tmax, Tmin, dim);
    for (int i = 0; i < best.size(); i++)
    {
        cout << best[i] << " ";
    }
    cout << "fitness_best= " << f1(best) << endl;
    return 0;
}