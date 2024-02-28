#include <iostream>
#include <fstream>
#include "chromosome.hpp"

int main()
{
    int chromosomeLength;
    std::cout << "Enter Chromosome length: " << std::endl;
    std::cin >> chromosomeLength;
    chromosome c1(chromosomeLength);
    std::cout << "Randomizing the c1:" << std::endl;
    c1.random();

    std::cout << "c1: " << c1 << std::endl;

    std::cout << "Performing mutation:" << std::endl;
    c1.mutation(0.1);

    std::cout << "Mutated c1: " << c1 << std::endl;

    std::cout << "Performing 1-bit mutation:" << std::endl;
    c1.mutation1bit(0.1);

    std::cout << "c1 after 1-bit mutation: " << c1 << std::endl;
    chromosome c2(c1);
    std::cout << "c2:" << c2 << std::endl;
    return 0;
}
