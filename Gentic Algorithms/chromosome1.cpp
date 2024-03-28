

#include <iostream>
#include <iomanip>
#include <assert.h>

#include "alea.hpp"
#include "chromosome.hpp"
#include "gene.hpp"
#include "param.hpp"
#include "fonc.hpp"
#include "general.hpp"
extern alea RANDOM;
using namespace std;
// initialiser un chromosome. allele non initialisée.
chromosome::chromosome(int ell)
{
  Longueur = ell;
  genes = new gene[Longueur]; // alloué la mémoire
  Fitness = 0;
}

// copie constructor
chromosome::chromosome(const chromosome &chrom)
{
  genes = new gene[chrom.Longueur]; // alloué la mémoire

  for (int i = 0; i < chrom.Longueur; i++) // copie de gene
    genes[i] = chrom.genes[i];

  Longueur = chrom.Longueur;
  Fitness = chrom.Fitness;
}

// destructor
chromosome::~chromosome()
{
  delete[] genes; // libére la mémoire
}

// donner des genes d'un chromosome utilisant la méthode random()
void chromosome::random()
{
  for (int i = 0; i < Longueur; i++)
    genes[i].random(); // genes[i].random()
}
void chromosome::init(std::ifstream &in1)
{
  int j, val;
  char s[200] = "";
  in1.getline(s, 200);
  for (j = 0; j < para->lchrom; j++) // strlen(s)
  {
    // if (s[j]
    genes[j].init(s[j]);
  }

  std::cout << std::endl;
}

// definir l'opérateur = pour les chromosomes
chromosome &chromosome::operator=(const chromosome &chrom)
{
  if (this == &chrom)
    return *this;

  for (int i = 0; i < chrom.Longueur; i++) // copie des genes
    genes[i] = chrom.genes[i];

  Longueur = chrom.Longueur;
  Fitness = chrom.Fitness;

  return *this;
}

// mutation aléatoire des genes.
void chromosome::mutation(double pmut)
{
  for (int i = 0; i < Longueur; i++)
    if (RANDOM.flip(pmut))
      genes[i].mutation(); // inverse le bit
}

void chromosome::mutation1bit(double pmut)
{
  int position = 1;
  position = RANDOM.entre_alea_int(0, Longueur - 1);
  genes[position].mutation();
}
//

void chromosome::hamming_mutation(double pmut)
{
  int i, k, j, dham, l;
  int *temp, *ham, *poly;
  int mini, maxi;
  mini = 0;
  maxi = para->lchrom;
  maxi--;
  k = RANDOM.entre_alea_int(mini, maxi) + 1;
  j = RANDOM.entre_alea_int(mini, maxi) + 1;
  dham = maxi - k;
  temp = new int[k];
  ham = new int[dham];
  poly = new int[j];
  for (i = mini; i < dham; i++)
    ham[i] = 1;
  for (i = mini; i < k; i++)
  {
    l = RANDOM.entre_alea_int(mini, maxi) + 1;

    j = RANDOM.entre_alea_int(mini, maxi) + 1;
    if (j > l)
      poly[i] = 0;
    else
      poly[i] = 1;
  }
  for (i = 0; i <= maxi; i++)
    temp[i] = 0;
  for (i = 0; i < dham; i++)
  {
    j = int(pow(2, i));
    if (j < dham)
      temp[j] = ham[i];
  }
  for (i = 0; i < maxi; i++)
    if (!(temp[i]))
      temp[i] = poly[i % k];
  for (i = 0; i < maxi; i++)
    if (temp[i])
      genes[i].mutation();
}
// Convertir le chromosome en une chaîne de caractères.

//
void chromosome::bin2string(char *str)
{
  int size = Longueur;
  for (int i = 0; i < size; i++)
    if (genes[i] == 1)
      str[i] = '1';
    else
      str[i] = '0';
}

//
// copie 'n' genes specifiés par 'locus' de gene pour chromosome 'C'
//
void chromosome::copieGene(chromosome &C, int *locus, int n)
{
  for (int i = 0; i < n; i++)
    genes[locus[i]] = C.genes[locus[i]];
}

// affiche le chromosome
std::ostream &operator<<(std::ostream &out, chromosome &chrom)
{
  if (para->rapport_string)
    for (int i = 0; i < chrom.Longueur; i++)
    {
      out << chrom.genes[i];
    }

  if (para->rapport_fitness)
    out << "    F= " << chrom.Fitness;
  para->frm_fit = chrom.Fitness;
  return out;
}

// evaluer fonction de fitness
void chromosome::evaluer()
{
  if (para->Type_Optim)

  {
    Fitness = objfonc(*this);
  }
  else
  {
    Fitness = -objfonc(*this);
  }
}
