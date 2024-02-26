//algorytm sprawdzajacy, czy w ciagu znajduje sie liczba podzielna przez 7
#include <iostream>
using namespace std;
const int MAX = 100;

bool szukaj (int T[], int n)
{
 for (int i=0;i<n;i++)
  if (T[i]%7==0) return true;
 return false;
}

int main()
{
 int T[MAX], n;
 cout<<"podaj liczbe elementow tablicy: ";
 cin>>n;
 cout<<"podaj elementy tablicy:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
 if (szukaj(T,n)) cout<<"TAK"<<endl;
 else cout<<"NIE"<<endl;
 return 0;
}
