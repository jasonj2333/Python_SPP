//sortowanie przez zliczanie
#include <iostream>
using namespace std;
const int MAX = 100;

void dane (int &n, char* komunikat)
{
 cout<<"podaj "<<komunikat<<": ";
 cin>>n;
}

void wczytaj (int T[], int n)
{
 cout<<"podaj elementy tablicy:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
}

void wyswietl (int T[], int n)
{
 cout<<"wczytana tablica:"<<endl;
 for (int i=0;i<n;i++) cout<<T[i]<<"\t";
 cout<<endl;
}

void sortuj (int T[], int n, int m)
{
 int P[MAX]={0};
 for (int i=0;i<n;i++) P[T[i]]++;
 int k=0;
 for (int i=0;i<m;i++)
  for (int j=P[i];j>=1;j--)
  {
   T[k]=i;
   k++;
  }
}

int main()
{
 int T[MAX], n, m;
 dane(n,"liczbe elementow");
 dane(m,"wartosc, od ktorej wszystkie elementy sa mniejsze");
 wczytaj(T,n);
 wyswietl(T,n);
 sortuj(T,n,m);
 wyswietl(T,n);
 return 0;
}
