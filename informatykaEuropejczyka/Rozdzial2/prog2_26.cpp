//sortowanie szybkie - rekurencja
#include <iostream>
using namespace std;
const int MAX = 100;

void dane (int &n)
{
 cout<<"podaj liczbe elementow tablicy: ";
 cin>>n;
}

void wczytaj (double T[], int n)
{
 cout<<"podaj elementy tablicy:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
}

void wyswietl (double T[], int n)
{
 cout<<"wczytana tablica:"<<endl;
 for (int i=0;i<n;i++) cout<<T[i]<<"\t";
 cout<<endl;
}

void sortuj (double T[], int lewy, int prawy)
{
 int i=lewy, j=prawy;
 double srodek=T[(lewy+prawy)/2], pom;
 do
 {
  while (T[i]<srodek) i++;
  while (T[j]>srodek) j--;
  if (i<=j)
  {
   pom=T[i];
   T[i]=T[j];
   T[j]=pom;
   i++;
   j--;
  }
 }
 while (i<=j);
 if (lewy<j) sortuj(T,lewy,j);
 if (prawy>i) sortuj(T,i,prawy);
}

int main()
{
 double T[MAX];
 int n;
 dane(n);
 wczytaj(T,n);
 wyswietl(T,n);
 sortuj(T,0,n-1);
 wyswietl(T,n);
 return 0;
}
