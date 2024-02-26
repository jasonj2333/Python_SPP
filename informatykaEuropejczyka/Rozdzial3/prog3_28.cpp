#include <iostream>
using namespace std;

int obliczSume(int a)
{
  return a;
}

int obliczSume(int a, int b)
{
  return a+b;
}

int obliczSume(int a, int b, int c)
{
  return a+b+c;
}

int main()
{
 int x=1, y=2, z=4;
 cout<<obliczSume(x,y)<<endl;
 cout<<obliczSume(x)<<endl;
 cout<<obliczSume(z,x)<<endl;
 cout<<obliczSume(x,y,z)<<endl;
 cout<<obliczSume(y)<<endl;
 return 0;
}
