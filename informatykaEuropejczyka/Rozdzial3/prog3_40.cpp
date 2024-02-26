#include<iostream>
using namespace std;

struct element
{
 int wartosc;
 element *lewy;
 element *prawy;
};

void dodajWierzcholek (int liczba, element **wierzcholek)
{
 if (*wierzcholek==NULL)
 {
  *wierzcholek = new element;
  (*wierzcholek)->wartosc=liczba;
  (*wierzcholek)->lewy=NULL;
  (*wierzcholek)->prawy=NULL;
 }
 else
  if (liczba<=(*wierzcholek)->wartosc) dodajWierzcholek(liczba,&(*wierzcholek)->lewy);
  else dodajWierzcholek(liczba,&(*wierzcholek)->prawy);
}

void wypiszDrzewo (element *wierzcholek)
{
 if (wierzcholek!=NULL)
 {
  wypiszDrzewo(wierzcholek->lewy);
  cout<<wierzcholek->wartosc<<"\t";
  wypiszDrzewo(wierzcholek->prawy);
 }
}

int main()
{
 int n, k;
 element *wierzcholek;
 wierzcholek=NULL;
 cout<<"podaj liczbe elementow: ";
 cin>>n;
 for (int i=0;i<n;i++)
 {
  cout<<"podaj liczbe calkowita: ";
  cin>>k;
  dodajWierzcholek(k,&wierzcholek);
 }
 cout<<"posortowane nierosnaco binarne drzewo przeszukiwan:"<<endl;
 wypiszDrzewo(wierzcholek);
 cout<<endl;
 return 0;
}
