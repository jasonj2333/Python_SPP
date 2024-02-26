//wyznaczanie minimum z n liczb wczytywanych na biezaco z klawiatury
#include <iostream>
using namespace std;

double oblicz (int n)
{
 double k, minimum;
 cout<<"podaj liczbe: ";
 cin>>k;
 minimum=k;
 while (n>1)
 {
  cout<<"podaj liczbe: ";
  cin>>k;
  if (k<minimum) minimum=k;
  n--;
 }
 return minimum;
}

int main()
{
 int n;
 cout<<"podaj liczbe elementow: ";
 cin>>n;
 cout<<oblicz(n)<<endl;
 return 0;
}
