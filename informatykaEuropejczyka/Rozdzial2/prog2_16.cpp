//liniowe przeszukiwanie ciagu liczbowego z wartownikiem
#include <iostream>
using namespace std;
const int MAX = 100;

bool szukaj (double T[], int n, double szukana)
{
 T[n]=szukana;
 int i=0;
 while (T[i]!=szukana) i++;
 if (i<n) return true;
 return false;
}

int main()
{
 double T[MAX], szukana;
 int n;
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
 if (szukaj(T,n,szukana)) cout<<"TAK"<<endl;
 else cout<<"NIE"<<endl;
 return 0;
}
