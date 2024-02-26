//algorytm sprawdzajacy, czy wszystkie elementy ciagu sa wieksze od 5
#include <iostream>
using namespace std;
const int MAX = 100;

bool szukaj (double T[], int n)
{
 for (int i=0;i<n;i++)
  if (T[i]<=5) return false;
 return true;
}

int main()
{
 double T[MAX];
 int n;
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
