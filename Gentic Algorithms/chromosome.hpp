#ifndef _chromosome_hpp
#define _chromosome_hpp

#include <assert.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include "gene.hpp"
#include "param.hpp"
#include "alea.hpp"

extern param *para;
class chromosome
{
private:
  gene *genes; // les genes
  int Longueur;
  double Fitness; // valeur de fitness
public:

  chromosome(int ell = para->lchrom): Longueur(ell), Fitness(0)
  {
    genes = new gene[Longueur];
  };
  chromosome( const chromosome &chrom );
  ~chromosome();
  inline void metvaleur(const int &locus, const int &value) { genes[locus] = int(value); }
  double fitness() { return Fitness; }

  void met_fitness(double fit) { Fitness = fit; }
  void evaluer(); // evaluer Chromosome
  void random();
  void init(std::ifstream &in1);      // initialisation à partir d'un fichier
  void mutation(double pmut);         // mutation aléatoire des genes.
  void mutation1bit(double pmut);     // muter un seul bit de façon aléatoire
  void hamming_mutation(double pmut); //  chercher dans le net

  int longueur() { return Longueur; }
  void bin2string(char *str);                       // Convertir le chromosome en une chaîne de caractères.
  void copieGene(chromosome &C, int *locus, int n); // copie 'n' genes specifiés par 'locus' de gene pour chromosome 'C'

  chromosome &operator=(const chromosome &chrom);
  gene &operator[](int loci) { return genes[loci]; }
  friend std::ostream &operator<<(std::ostream &out, chromosome &chrom);
};

#endif
