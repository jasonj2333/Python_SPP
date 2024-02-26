#include <iostream>
using namespace std;

int a=5;        //zmienna globalna

int oblicz (void)
{
 int b=4;        //zmienna lokalna
 return a*b;
}

int main()
{
 int c;         //zmienna lokalna
 c=oblicz();
 cout<<c<<endl;
 return 0;
}
