//wyznaczanie maksimum w n elementowym ciagu liczb
#include <iostream>
using namespace std;
const int MAX = 100;

int oblicz (int T[], int n)
{
 int maksimum=T[0];
 for (int i=1;i<n;i++)
  if (T[i]>maksimum) maksimum=T[i];
 return maksimum;
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
 cout<<"maksimum = "<<oblicz(T,n)<<endl;
 return 0;
}
