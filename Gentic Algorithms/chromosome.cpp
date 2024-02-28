#include "chromosome.hpp"

extern alea RANDOM;
param* para = new param;
chromosome::chromosome( const chromosome &chrom ) {
    Longueur = chrom.Longueur;
    genes = new gene[Longueur];
    for ( int i = 0; i < Longueur; i++ ) {
        genes[i] = chrom.genes[i];
    }
    Fitness = chrom.Fitness;
}
chromosome::~chromosome()
{
    delete[] genes;
}
// void chromosome::evaluer()
// {
//     if(para->type_option){
//         Fitness = objfunc(*this);
//     } else {
//         Fitness = -objfonc(*this);
//     }
// }
void chromosome::random()
{
    int i;
    for (i = 0; i < Longueur; i++)
        genes[i].random();
}
void chromosome::init(std::ifstream &in1)
{
    char s[200] = "";
    in1.getline(s,200);
    for (int i = 0; i < para->lchrom; i++)
    {
        genes[i].init(s[i]);
    }
}
void chromosome::mutation(double pmut)
{
    for (int i = 0; i < Longueur; i++)
        if (RANDOM.flip(pmut))
            genes[i].mutation();
}

void chromosome::mutation1bit(double pmut)
{
    int i;
    i = RANDOM.uniform_rand_int(Longueur-1);
    genes[i].mutation();
}

void chromosome::bin2string(char *str)
{
    for (int i = 0; i < Longueur; i++)
        str[i] = genes[i].allele() + '0';
    str[Longueur] = '\0';
}

void chromosome::copieGene(chromosome &C, int *locus, int n)
{
    for (int i = 0; i < n; i++)
        genes[locus[i]] = C.genes[locus[i]];
}
chromosome &chromosome::operator=(const chromosome &chrom){
    if(this==&chrom){
        return *this;
    }
    delete[] genes;
    genes = new gene[chrom.Longueur];
    for (int i = 0; i < chrom.Longueur; i++)
      genes[i] = chrom.genes[i];
    Longueur = chrom.Longueur;
    Fitness = chrom.Fitness;
    return *this;
}
std::ostream &operator<<(std::ostream &out, chromosome &chrom)
{
    for(int i = 0; i < chrom.Longueur; i++)
        out << chrom.genes[i];
    return out;
}