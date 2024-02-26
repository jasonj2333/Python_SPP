//algorytm Euklidesa wykorzystujacy operacje odejmowania - rekurencja
#include <iostream>
using namespace std;

void dane (int &n, char nazwa)
{
 cout<<"podaj "<<nazwa<<": ";
 cin>>n;
}

int nwd (int a, int b)
{
 if (a==b) return a;
 if (a>b) return nwd(a-b,b);
 return nwd(a,b-a);
}

int main()
{
 int a, b;
 dane(a,'a');
 dane(b,'b');
 cout<<"NWD("<<a<<","<<b<<") = "<<nwd(a,b)<<endl;
 return 0;
}
