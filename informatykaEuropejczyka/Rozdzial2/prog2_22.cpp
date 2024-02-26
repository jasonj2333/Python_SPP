//sortowanie przez wybor
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
 int k;
 double pom;
 for (int i=0;i<n-1;i++)
 {
  k=i;
  for (int j=i+1;j<n;j++)
   if (T[j]<T[k]) k=j;
  pom=T[k];
  T[k]=T[i];
  T[i]=pom;
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
