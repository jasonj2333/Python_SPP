#include <iostream>
using namespace std;

int oblicz (int a, int b=-3, int c=-4)
{
 return a+b+c;
}

int main()
{
 int a=2, b=3, c=4;
 cout<<"\nbrak parametrow domyslnych: "<<oblicz(a,b,c)<<endl;
 cout<<"\ndomyslny parametr c: "<<oblicz(a,b)<<endl;
 cout<<"\ndomyslne parametry b i c: "<<oblicz(a)<<endl;
 return 0;
}
