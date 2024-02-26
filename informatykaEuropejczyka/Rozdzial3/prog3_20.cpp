#include <iostream>
using namespace std;

void funkcja1 (void)
{
 cout<<"uruchomienie funkcji 1"<<endl;
}

void funkcja2 (int a, int b)
{
 cout<<"uruchomienie funkcji 2:"<<endl;
 cout<<a+b<<endl;
}

int funkcja3 (int a, int b)
{
 return a+b;
}

int main()
{
 int x=2, y=8, z;
 funkcja1();
 funkcja2(x,y);
 cout<<"uruchomienie funkcji 3:"<<endl;
 z=funkcja3(x,y);
 cout<<"suma = "<<z<<endl;
 if (funkcja3(x,y)>0) cout<<"wieksze od 0"<<endl;
 return 0;
}
