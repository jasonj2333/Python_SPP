//obliczanie pola obszaru ograniczonego wykresem funkcji, osia 0x i prostymi p, q - metoda trapezow
#include <iostream>
#include <cmath>
using namespace std;

double F (double x)
{
 return -pow(x,3)-pow(x,2)+1;
}

double oblicz (double p, double q, int n)
{
 double dl=(q-p)/n, s=0;
 for (int i=1;i<n;i++) s+=abs(F(p+i*dl));
 return dl/2*(abs(F(p))+abs(F(q))+2*s);
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
