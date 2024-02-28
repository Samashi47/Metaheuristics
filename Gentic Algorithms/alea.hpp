#ifndef _alea_hpp
#define _alea_hpp

#include <random>
#include <iostream>

class alea{
    private:
        double prob;
    public:
        alea(double p = 0.5) : prob(p) {};
        ~alea() {};
        bool flip(double p);
        double bernoulli_rand();
        double uniform_rand();
        double normal_rand();
        int uniform_rand_int(int l);
};
extern alea RANDOM;
#endif