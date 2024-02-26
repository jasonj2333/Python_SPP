//liniowe przeszukiwanie ciagu liczbowego
#include <iostream>
using namespace std;
const int MAX = 100;

bool szukaj (int T[], int n, int szukana)
{
 int i=0;
 while (i<n && T[i]!=szukana) i++;
 if (i==n) return false;
 return true;
}

int main()
{
 int T[MAX], n, szukana;
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
