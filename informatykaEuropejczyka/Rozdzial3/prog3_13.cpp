#include <iostream>
using namespace std;
int main()
{
 int n;
 cout<<"podaj n: ";
 cin>>n;
 switch (n)
 {
  case 1: cout<<"poniedzialek"<<endl; break;
  case 2: cout<<"wtorek"<<endl; break;
  case 3: cout<<"sroda"<<endl; break;
  case 4: cout<<"czwartek"<<endl; break;
  case 5: cout<<"piatek"<<endl; break;
  case 6: cout<<"sobota"<<endl; break;
  case 7: cout<<"niedziela"<<endl; break;
  default: cout<<"podano bledna wartosc"<<endl; break;
 }
 return 0;
}
