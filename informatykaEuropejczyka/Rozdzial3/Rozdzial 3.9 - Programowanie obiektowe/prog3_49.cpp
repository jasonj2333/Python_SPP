#include<iostream>
#include <cstring>
using namespace std;

class sklep
{
  char nazwa_sklepu[50];
  int ilosc_pracownikow;
  float obroty_miesieczne;
 public:
  sklep(char *ns, int ip, float o);
  ~sklep();
  char *wyswietlNazweSklepu();
  int wyswietlIloscPracownikow();
  float wyswietlObroty();
  void wczytajNazweSklepu(char *ns);
  void wczytajIloscPracownikow(int ip);
  void wczytajObroty(float o);
};

class towar : public sklep
{
  char nazwa_towaru[50];
  int ilosc_towarow;
  float cena_towaru;
 public:
  towar(char *ns, int ip, float o, char *nt, int it, float ct);
  ~towar();
  char *wyswietlNazweTowaru();
  int wyswietlIloscTowarow();
  float wyswietlCeneTowaru();
  void wczytajNazweTowaru(char *nt);
  void wczytajIloscTowarow(int it);
  void wczytajCeneTowaru(int ct);
};

sklep::sklep(char *ns, int ip, float o)
{
 strcpy(nazwa_sklepu,ns);
 ilosc_pracownikow = ip;
 obroty_miesieczne = o;
}

sklep::~sklep()
{}

char *sklep::wyswietlNazweSklepu()
{
 return nazwa_sklepu;
}

int sklep::wyswietlIloscPracownikow()
{
 return ilosc_pracownikow;
}

float sklep::wyswietlObroty()
{
 return obroty_miesieczne;
}

void sklep::wczytajNazweSklepu(char *ns)
{
 strcpy(nazwa_sklepu,ns);
}

void sklep::wczytajIloscPracownikow(int ip)
{
 ilosc_pracownikow = ip;
}

void sklep::wczytajObroty(float o)
{
 obroty_miesieczne = o;
}

towar::towar(char *ns, int ip, float o, char *nt, int it, float ct) : sklep(ns, ip, o)
{
 strcpy(nazwa_towaru,nt);
 ilosc_towarow = it;
 cena_towaru = ct;
}

towar::~towar()
{}

char *towar::wyswietlNazweTowaru()
{
 return nazwa_towaru;
}

int towar::wyswietlIloscTowarow()
{
 return ilosc_towarow;
}

float towar::wyswietlCeneTowaru()
{
 return cena_towaru;
}

void towar::wczytajNazweTowaru(char *nt)
{
 strcpy(nazwa_towaru,nt);
}

void towar::wczytajIloscTowarow(int it)
{
 ilosc_towarow = it;
}

void towar::wczytajCeneTowaru(int ct)
{
 cena_towaru = ct;
}

int main()
{
 return 0;
}
