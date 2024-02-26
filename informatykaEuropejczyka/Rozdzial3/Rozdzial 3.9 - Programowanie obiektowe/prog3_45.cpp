#include <iostream>
#include <cstring>
using namespace std;

class osoba                                 //definicja klasy
{
  char nazwisko[25];                        //sekcja prywatna
  char imie[20];
  int wiek;
 public:                                    //sekcja publiczna
  void wczytaj(char *n, char *i, int w);    //deklaracja metody
  void wypisz()                             //definicja metody wewn¹trz klasy
  {
   cout<<"\n"<<imie<<" "<<nazwisko<<endl;
   cout<<"wiek: "<<wiek<<endl;
  }
};                                          //koniec definicji klasy

void osoba::wczytaj (char *n, char *i, int w)//definicja metody poza klas¹
{
 strcpy(nazwisko,n);
 strcpy(imie,i);
 wiek=w;
}

int main()
{
 osoba O1, O2;
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
 O2.wczytaj("Kowalski","Jan",24);
 cout<<"\nwyswietlenie danych wszystkich osob:"<<endl;
 O1.wypisz();
 O2.wypisz();
 return 0;
}
