//szyfr Cezara
#include <iostream>
#include <cstring>
using namespace std;

string szyfruj (string tekst, string alfabet, int klucz)
{
 string wynik;
 int dlT=tekst.size(), dlA=alfabet.size();
 for (int i=0;i<dlT;i++)
  for (int j=0;j<dlA;j++)
   if (tekst[i]==alfabet[j]) wynik+=alfabet[(j+klucz)%dlA];
 return wynik;
}

int main()
{
 string tekst, alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 int klucz;
 cout<<"podaj tekst jawny: ";
 cin>>tekst;
//cout<<"podaj alfabet jawny: ";
//cin>>alfabet;
 cout<<"podaj klucz: ";
 cin>>klucz;
 cout<<"szyfrogram: "<<szyfruj(tekst,alfabet,klucz)<<endl;
 return 0;
}
