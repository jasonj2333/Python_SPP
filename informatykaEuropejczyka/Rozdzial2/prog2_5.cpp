//algorytm Euklidesa wykorzystujacy operacje odejmowania - iteracja
#include <iostream>
using namespace std;

void dane (int &n, char nazwa)
{
 cout<<"podaj "<<nazwa<<": ";
 cin>>n;
}

int nwd (int a, int b)
{
 while (a!=b)
  if (a>b) a-=b;
  else b-=a;
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
