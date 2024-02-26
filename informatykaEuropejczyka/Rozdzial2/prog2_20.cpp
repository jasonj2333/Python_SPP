//sprawdzanie, czy ciag jest rosnacy
#include <iostream>
using namespace std;
const int MAX = 100;

bool rosnacy (int T[], int n)
{
 for (int i=0;i<n-1;i++)
  if (T[i]>=T[i+1]) return false;
 return true;
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
 if (rosnacy(T,n)) cout<<"ciag jest rosnacy"<<endl;
 else cout<<"ciag nie jest rosnacy"<<endl;
 return 0;
}
