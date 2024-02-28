#include "alea.hpp"
#include <random>
#include <iostream>

bool alea::flip(double p){
    return bernoulli_rand() < p;
}
double alea::bernoulli_rand(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::bernoulli_distribution d(prob);
    return d(gen);
}
int alea::uniform_rand_int(int l){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> d(0, l);
    return d(gen);
}
double alea::uniform_rand(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> d(0, 1);
    return d(gen);
}
double alea::normal_rand(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<> d(0, 1);
    return d(gen);
}
