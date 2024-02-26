#include <iostream>
using namespace std;

double oblicz (int a, double b)
{
 return a+b;
}

double oblicz (double a, double b)
{
 return a*b;
}

double oblicz (int a, int b, double c)
{
 return a+b+c;
}

double oblicz (int a, double b, double c)
{
 return a*b*c;
}

int main()
{
 int x=2;
 double y=3.5, z=1.2;
 cout<<oblicz(y,z)<<endl;
 cout<<oblicz(x,x,z)<<endl;
 cout<<oblicz(x,y)<<endl;
 cout<<oblicz(x,z,y)<<endl;
 cout<<oblicz(x,x,y)<<endl;
 cout<<oblicz(x,z)<<endl;
 return 0;
}
