

#ifndef _fonc_hpp
#define _fonc_hpp

#include "chromosome.hpp"

long double objfonc(chromosome &x);
double trap(int k, int ones);
extern long double objective_fonc(char *chrom, int lchrom);
int unitation(char *chrom, int debutBit, int finBit);
long double objective_fonc(char *chrom, int lchrom);
long double objective_Mich1(char *chrom, int lchrom);
long double objective_Mich2(char *chrom, int lchrom);
long double objective_Shubert(char *chrom, int lchrom);
long double objective_Rastrigin(char *chrom, int lchrom);
long double objective_De_Jong2(char *chrom, int lchrom);
long double objective_Schwefel(char *chrom, int lchrom);
long double objective_Mexican_Hat(char *chrom, int lchrom);
long double objective_Modal1(char *chrom, int lchrom);
long double objective_AB1(char *chrom, int lchrom);
long double objective_AB2(char *chrom, int lchrom);
long double objective_AB3(char *chrom, int lchrom);
long double objective_AB4(char *chrom, int lchrom);
#endif
