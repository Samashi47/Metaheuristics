#include "population.hpp"

population::population(int Pop_taille)
{
    this->Pop_taille = Pop_taille;
    Chromosomes = new chromosome[Pop_taille];
    MatingPool = new int[Pop_taille];
    Selectionner = new Selection();
    croiser = new Crossover();
    genes = new gene();
    Best = 0;
    Worst = 0;
    MaxFit = 0;
    MinFit = 0;
    MoyFit = 0;
}
population::population(population &pop)
{
    Pop_taille = pop.Pop_taille;
    Chromosomes = new chromosome[Pop_taille];
    MatingPool = new int[Pop_taille];
    Selectionner = new Selection();
    croiser = new Crossover();
    genes = new gene();
    Best = pop.Best;
    Worst = pop.Worst;
    MaxFit = pop.MaxFit;
    MinFit = pop.MinFit;
    MoyFit = pop.MoyFit;
    for (int i = 0; i < Pop_taille; i++)
    {
        Chromosomes[i] = pop.Chromosomes[i];
    }
}
population::~population()
{
    delete[] Chromosomes;
    delete[] MatingPool;
    delete Selectionner;
    delete croiser;
    delete genes;
}
void population::selection(population *npop)
{
    Selectionner.selection(npop);
}
void population::selectionnement(population *npop)
{
    Selectionner.selectionnement(npop);
}
void population::croisement(void)
{
    croiser.croisement();
}
void population::mutate(void)
{
    for (int i = 0; i < Pop_taille; i++)
    {
        Chromosomes[i].mutation(para->proba_mutation);
    }
}
void population::evaluer()
{
    for (int i = 0; i < Pop_taille; i++)
    {
        Chromosomes[i].evaluer();
    }
}
population &population::operator=(population &pop)
{
    if (this == &pop)
        return *this;
    Pop_taille = pop.Pop_taille;
    Best = pop.Best;
    Worst = pop.Worst;
    MaxFit = pop.MaxFit;
    MinFit = pop.MinFit;
    MoyFit = pop.MoyFit;
    for (int i = 0; i < Pop_taille; i++)
    {
        Chromosomes[i] = pop.Chromosomes[i];
    }
    return *this;
}
bool population::converge()
{
    int i;
    double fit;
    double moy = 0;
    Best = 0;
    Worst = 0;
    MaxFit = Chromosomes[0].fitness();
    MinFit = Chromosomes[0].fitness();
    for (i = 0; i < Pop_taille; i++)
    {
        fit = Chromosomes[i].fitness();
        moy += fit;
        if (fit > MaxFit)
        {
            MaxFit = fit;
            Best = i;
        }
        if (fit < MinFit)
        {
            MinFit = fit;
            Worst = i;
        }
    }
    MoyFit = moy / Pop_taille;
    return (MaxFit - MinFit) < para->stop_critere;
}
std::ostream &operator<<(std::ostream &out, population &pop)
{
    out << "pop_taille: " << pop.Pop_taille << std::endl;
    out << "MaxFit: " << pop.MaxFit << " Chrom_id: " << pop.Best << std::endl;
    out << "MinFit: " << pop.MinFit << " Chrom_id: " << pop.Worst << std::endl;
    out << "MoyFit: " << pop.MoyFit << std::endl;
    return out;
}