#include <iostream>
#include <cstring>
using namespace std;

class osoba
{
  char nazwisko[25];
  char imie[20];
  int wiek;
 public:
  osoba();						        //deklaracja konstruktora 1
  osoba(char *n, char *i, int w);		//deklaracja konstruktora 2
  void wczytaj(char *n, char *i, int w);
  void wypisz();
};

osoba::osoba ()					        //definicja konstruktora 1
{
  strcpy(nazwisko,"");
  strcpy(imie,"");
  wiek=0;
}

osoba::osoba (char *n, char *i, int w)	//definicja konstruktora 2
{
  strcpy(nazwisko,n);
  strcpy(imie,i);
  wiek=w;
}

void osoba::wypisz (void)
{
 cout<<"\n"<<imie<<" "<<nazwisko<<endl;
 cout<<"wiek: "<<wiek<<endl;
}

void osoba::wczytaj (char *n, char *i, int w)
{
  strcpy(nazwisko,n);
  strcpy(imie,i);
  wiek=w;
}

int main()
{
 osoba O1;						       //uruchomienie konstruktora 1
 osoba O2("Kowalski","Jan",24);        //uruchomienie konstruktora 2
 char na[25], im[20];
 int wi;
 cout<<"podaj dane osoby nr 1:"<<endl;
 cout<<"nazwisko: ";
 cin.getline(na,sizeof(na));
 cout<<"imie: ";
 cin.getline(im,sizeof(im));
 cout<<"wiek: ";
 cin>>wi;
 O1.wczytaj(na,im,wi);
 cout<<"\nwyswietlenie danych wszystkich osob:"<<endl;
 O1.wypisz();
 O2.wypisz();
 return 0;
}
