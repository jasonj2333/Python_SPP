#include<iostream>
using namespace std;

struct element
{
 int wartosc;
 element *nastepny;
};

element *dodajNaKoncu (int liczba, element *koniec)
{
 element *wsk;
 wsk = new element;
 wsk->wartosc=liczba;
 wsk->nastepny=NULL;
 if (koniec) koniec->nastepny=wsk;
 return wsk;
}

element *usunNaPoczatku (int *liczba, element *poczatek)
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

element *wstawElement (int liczba, element *poczatek)
{
 element *wsk, *poprzednik, *nastepnik;
 wsk = new element;
 wsk->wartosc=liczba;
 poprzednik=NULL;
 nastepnik=poczatek;
 while (nastepnik!=NULL)
  if (nastepnik->wartosc>=liczba)
  {
   wsk->nastepny=nastepnik;
   if (poprzednik!=NULL)               //dolaczanie wewnatrz listy
   {
    poprzednik->nastepny=wsk;
    return poczatek;
   }
   else return wsk;                    //dolaczanie na poczatku listy
  }
  else
  {
   poprzednik=nastepnik;
   nastepnik=poprzednik->nastepny;
  }
  wsk->nastepny=NULL;                  //dolaczanie na koncu listy
  poprzednik->nastepny=wsk;
  return poczatek;
}

int usunElement (int *liczba, element *poczatek, element *nowy)
{
 element *wsk, *poprzednik;
 poprzednik=NULL;
 wsk=poczatek;
 while (wsk!=NULL)
  if (wsk->wartosc==*liczba)
  {
   if (poprzednik!=NULL)
   {
    poprzednik->nastepny=wsk->nastepny;
    nowy=poczatek;
    return 0;
   }
   else nowy=wsk->nastepny;
   delete wsk;
   return 0;
  }
  else
  {
   poprzednik=wsk;
   wsk=poprzednik->nastepny;
  }
 nowy=poczatek;
 return 0;
}

void wypisz (element *wsk)
{
 cout<<"aktualna lista jednokierunkowa: ";
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
 cout<<"\nTWORZENIE LISTY JEDNOKIERUNKOWEJ"<<endl;
 cout<<"podaj, ile elementow dodac do listy (co najmniej jeden): ";
 cin>>n;
 cout<<"WPROWADZ LICZBY CALKOWITE UPORZADKOWANE NIEMALEJACO"<<endl;
 cout<<"podaj liczbe calkowita: ";
 cin>>k;
 poczatek=koniec=dodajNaKoncu(k,NULL);
 wypisz(poczatek);
 for(int i=1;i<n;i++)
 {
  cout<<"podaj liczbe calkowita: ";
  cin>>k;
  koniec=dodajNaKoncu(k,koniec);
  wypisz(poczatek);
 }
 cout<<"\nWSTAWIANIE ELEMENTU DO CIAGU UPORZADKOWANEGO - LISTY JEDNOKIERUNKOWEJ"<<endl;
 cout<<"podaj liczbe calkowita: ";
 cin>>k;
 poczatek=wstawElement(k,poczatek);
 wypisz(poczatek);
 cout<<"\nUSUWANIE WYBRANEGO ELEMENTU Z LISTY"<<endl;
 cout<<"podaj liczbe calkowita: ";
 cin>>k;
 usunElement(&k,poczatek,poczatek);
 wypisz(poczatek);
 cout<<"\nUSUWANIE WSZYSTKICH ELEMENTOW Z LISTY"<<endl;
 while (poczatek!=NULL)
 {
  poczatek=usunNaPoczatku(&k,poczatek);
  cout<<"zdejmowany element to: "<<k<<endl;
  wypisz(poczatek);
 }
 return 0;
}
