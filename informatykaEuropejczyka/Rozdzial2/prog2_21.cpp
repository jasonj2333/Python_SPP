//sortowanie babelkowe
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

void sortuj (double T[], int n)
{
 double pom;
 for (int j=n-1;j>0;j--)
  for (int i=0; i<j; i++)
   if (T[i]>T[i+1])
   {
    pom=T[i];
    T[i]=T[i+1];
    T[i+1]=pom;
   }
}

int main()
{
 double T[MAX];
 int n;
 dane(n);
 wczytaj(T,n);
 wyswietl(T,n);
 sortuj(T,n);
 wyswietl(T,n);
 return 0;
}
