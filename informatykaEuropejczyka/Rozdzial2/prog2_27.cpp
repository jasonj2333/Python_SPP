//obliczanie pola ograniczonego wykresem funkcji, osia 0x i prostymi p, q - metoda prostokatow
#include <iostream>
#include <cmath>
using namespace std;

double F (double x)
{
 return pow(x,2)-x-3;
}

double oblicz (double p, double q, int n)
{
 double dl=(q-p)/n, s=0;
 for (int i=0;i<n;i++) s+=abs(F(p+dl*i+dl/2));
 return dl*s;
}

int main()
{
 double p, q;
 int n;
 cout<<"podaj przedzial [p, q]: ";
 cin>>p>>q;
 cout<<"podaj liczbe prostokatow n: ";
 cin>>n;
 cout<<"pole = "<<oblicz(p,q,n)<<endl;
 return 0;
}
