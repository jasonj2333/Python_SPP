//jednoczesne znajdowanie minimalnego i maksymalnego elementu - iteracja
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

void oblicz (double T[], int n, double &minimum, double &maksimum)
{
 int dl, i;
 if (n%2) dl=n-2; else dl=n-1;
 if (T[0]<=T[1])
 {
  minimum=T[0];
  maksimum=T[1];
 }
 else
 {
  minimum=T[1];
  maksimum=T[0];
 }
 i=2;
 while (i<dl)
 {
  if (T[i]<=T[i+1])
  {
   if (T[i]<minimum) minimum=T[i];
   if (T[i+1]>maksimum) maksimum=T[i+1];
  }
  else
  {
   if (T[i+1]<minimum) minimum=T[i+1];
   if (T[i]>maksimum) maksimum=T[i];
  }
  i+=2;
 }
 if (n%2)
 {
  if (T[n-1]<minimum) minimum=T[n-1];
  if (T[n-1]>maksimum) maksimum=T[n-1];
 }
}

int main()
{
 double T[MAX], minimum, maksimum;
 int n;
 dane(n);
 wczytaj(T,n);
 wyswietl(T,n);
 oblicz(T,n,minimum,maksimum);
 cout<<"minimum = "<<minimum<<endl;
 cout<<"maksimum = "<<maksimum<<endl;
 return 0;
}
