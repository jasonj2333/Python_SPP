#include <iostream>
#include <iomanip>
using namespace std;

void wczytaj (int *T, int n)
{
 cout<<"podaj elementy tablicy:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
}

void wypisz (int T[], int n)
{
 cout<<"\nwczytana tablica:"<<endl;
 for (int i=0;i<n;i++) cout<<setw(7)<<T[i];
 cout<<endl;
}

void wypiszOdwrotnie (int T[], int n)
{
 cout<<"\nwczytana tablica w odwrotnej kolejnosci:"<<endl;
 for (int i=n-1;i>=0;i--) cout<<setw(7)<<T[i];
 cout<<endl;
}

int main()
{
 int T[8];
 wczytaj(T,8);
 wypisz(T,8);
 wypiszOdwrotnie(T,8);
 return 0;
}
