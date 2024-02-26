#include <iostream>
#include <cstring>
using namespace std;

class osoba
{
  char nazwisko[25];
  char imie[20];
  int wiek;
 public:
  osoba(char *n, char *i, int w);
  ~osoba();					            //deklaracja destruktora
  void wypisz();
};

osoba::osoba (char *n, char *i, int w)
{
  strcpy(nazwisko,n);
  strcpy(imie,i);
  wiek=w;
}

osoba::~osoba ()				        //definicja destruktora
{}

void osoba::wypisz (void)
{
 cout<<imie<<" "<<nazwisko<<endl;
 cout<<"wiek: "<<wiek<<endl;
}

int main()
{
 osoba *wsk;
 wsk = new osoba("Kowalski","Jan",24);	//uruchomienie konstruktora
 wsk->wypisz();
 delete wsk;					        //uruchomienie destruktora
 return 0;
}
