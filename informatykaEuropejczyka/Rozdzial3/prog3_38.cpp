#include<iostream>
using namespace std;

struct element
{
 int wartosc;
 element *nastepny;
};

element *dodaj (int liczba, element *koniec)
{
 element *wsk;
 wsk = new element;
 wsk->wartosc=liczba;
 wsk->nastepny=NULL;
 if (koniec) koniec->nastepny=wsk;
 return wsk;
}

element *usun (int *liczba, element *poczatek)
{
 if (poczatek)
 {
  element *wsk;
  *liczba=poczatek->wartosc;
  wsk=poczatek->nastepny;
  delete poczatek;
  return wsk;
 }
 else return NULL;
}

void wypisz (element *wsk)
{
 cout<<"kolejka : ";
 while (wsk!=NULL)
 {
  cout<<wsk->wartosc<<"\t";
  wsk=wsk->nastepny;
 }
 cout<<endl;
}

int main()
{
 int n, k;
 element *poczatek, *koniec;
 cout<<"TWORZENIE KOLEJKI"<<endl;
 cout<<"podaj, ile elementow dodac do kolejki = ";
 cin>>n;
 cout<<"podaj liczbe calkowita = ";
 cin>>k;
 poczatek=koniec=dodaj(k,NULL);
 wypisz(poczatek);
 for(int i=1;i<n;i++)
 {
  cout<<"podaj liczbe calkowita = ";
  cin>>k;
  koniec=dodaj(k,koniec);
  wypisz(poczatek);
 }
 cout<<"\nUSUWANIE ELEMENTOW Z KOLEJKI"<<endl;
 while (poczatek!=NULL)
 {
  poczatek=usun(&k,poczatek);
  cout<<"zdejmowany element to = "<<k<<endl;
  wypisz(poczatek);
 }
 return 0;
}

