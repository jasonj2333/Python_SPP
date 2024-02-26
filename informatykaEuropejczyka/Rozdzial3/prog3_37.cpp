#include <iostream>
using namespace std;

struct element
{
 int wartosc;
 element *poprzedni;
};

element *dodaj (int liczba, element *wierzcholek)
{
 element *wsk;
 wsk = new element;
 if (!wsk) return 0;
 wsk->wartosc=liczba;
 wsk->poprzedni=wierzcholek;
 return wsk;
}

element *usun (int *liczba, element *wierzcholek)
{
 if (!wierzcholek) return 0;
 element *wsk;
 *liczba=wierzcholek->wartosc;
 wsk=wierzcholek->poprzedni;
 delete wierzcholek;
 return wsk;
}

void wypisz (element *wsk)
{
 cout<<"aktualny stos: ";
 while (wsk!=NULL)
 {
  cout<<wsk->wartosc<<"\t";
  wsk=wsk->poprzedni;
 }
 cout<<endl;
}

int main()
{
 int n, k;
 element *wierzcholek;
 wierzcholek=NULL;
 cout<<"WKLADANIE ELEMENTOW NA STOS"<<endl;
 cout<<"podaj, ile elementow wlozyc na stos: ";
 cin>>n;
 for(int i=0;i<n;i++)
 {
  cout<<"podaj liczbe calkowita: ";
  cin>>k;
  wierzcholek=dodaj(k,wierzcholek);
  wypisz(wierzcholek);
 }
 cout<<"\n\nUSUWANIE ELEMENTOW ZE STOSU"<<endl;
 while (wierzcholek!=NULL)
 {
  wierzcholek=usun(&k,wierzcholek);
  cout<<"zdejmowany element to: "<<k<<endl;
  wypisz(wierzcholek);
 }
 return 0;
}

