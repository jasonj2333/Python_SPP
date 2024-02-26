//wyznaczanie miejsca zerowego funkcji w przedziale [p, q]
#include <iostream>
#include <cmath>
using namespace std;

double F (double x)
{
 return pow(x,2)-x-3;
}

double oblicz (double p, double q, double E1)
{
 double s=(p+q)/2;
 while (F(p)!=0 && F(q)!=0 && q-p>=E1)
 {
  s=(p+q)/2;
  if (F(p)*F(s)>0) p=s; else q=s;
 }
 if (F(p)==0) return p;
 if (F(q)==0) return q;
 return s;
}

int main()
{
 double p, q, E1;
 cout<<"podaj przedzial [p, q]: ";
 cin>>p>>q;
 cout<<"podaj dokladnosc E1: ";
 cin>>E1;
 cout<<"miejsce zerowe = "<<oblicz(p,q,E1)<<endl;
 return 0;
}
