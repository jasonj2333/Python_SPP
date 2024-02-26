//algorytm rekurencyjny - przeszukiwanie binarne ciagu uporzadkowanego
#include <iostream>
using namespace std;
const int MAX = 100;

int szukaj (double T[], int lewy, int prawy, double szukana)
{
 if (lewy<=prawy)
 {
  int srodek=(lewy+prawy)/2;
  if (T[srodek]==szukana) return srodek;
  if (T[srodek]<szukana) return szukaj(T,srodek+1,prawy,szukana);
  return szukaj(T,lewy,srodek-1,szukana);
 }
 return -1;
}

int main()
{
 double T[MAX], szukana;
 int n, wynik;
 cout<<"podaj liczbe elementow tablicy: ";
 cin>>n;
 cout<<"podaj elementy tablicy:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
 cout<<"podaj szukany element: ";
 cin>>szukana;
 wynik=szukaj(T,0,n-1,szukana);
 if (wynik>-1) cout<<"T["<<wynik<<"] = "<<T[wynik]<<endl;
 else cout<<"NIE"<<endl;
 return 0;
}
