//algorytm Euklidesa wykorzystujacy operacje reszty z dzielenia - iteracja
#include <iostream>
using namespace std;

void dane (int &n, char nazwa)
{
 cout<<"podaj "<<nazwa<<": ";
 cin>>n;
}

int nwd (int a, int b)
{
 int r;
 while (b>0)
 {
  r=a%b;
  a=b;
  b=r;
 }
 return a;
}

int main()
{
 int a, b;
 dane(a,'a');
 dane(b,'b');
 cout<<"NWD("<<a<<","<<b<<") = "<<nwd(a,b)<<endl;
 return 0;
}
