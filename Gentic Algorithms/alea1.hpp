

#ifndef _ALEA_H
#define _ALEA_H

#define Nmt 624
#define Mmt 397
#define vecteur 0x9908b0dfUL    /* vecteur constant*/
#define bps_masque 0x80000000UL /* les bits les plus significatis */
#define bms_masque 0x7fffffffUL /* lles bits les moins significatifs */

static unsigned long mt[Nmt]; /* le tableau du vecteur d'etat  */
static int mti = Nmt + 1;     /* si mti==N+1  alors mt[N] non initialiser */

const int non_badra = -1;

class alea
{
private:
  unsigned long Badra;

protected:
public:
  alea() { randomize(non_badra); }

  void init_Mersenne();
  unsigned long metbadra();
  void randomize(int badra);
  void randomize(double badra);

  double uniform01();
  double uniform(double a, double b);
  int uniform(int a, int b);
  double exponentiel(double mu);
  bool bernoulli(double p);
  bool flip(double p) { return bernoulli(p); }
  long geometrique(double p);
  void melanger(int *tab, int ltab);
  double normal01();
  double normal(double mean, double variance);
  double entre_alea_double(double minimum, double maximum);
  int entre_alea_int(int minimum, int maximum);
  unsigned long genrand_int32();
  long genrand_int31();
  double genrand_real1();
  double genrand_real2();
  double genrand_real3(void);
  double genrand_res53(void);
  ~alea() {}
};

#endif
