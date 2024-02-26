//algorytm Euklidesa wykorzystujacy operacje reszty z dzielenia - rekurencja
#include <iostream>
using namespace std;

void dane (int &n, char nazwa)
{
 cout<<"podaj "<<nazwa<<": ";
 cin>>n;
}

int nwd (int a, int b)
{
 if (b==0) return a;
 return nwd(b,a%b);
}

int main()
{
 int a, b;
 dane(a,'a');
 dane(b,'b');
 cout<<"NWD("<<a<<","<<b<<") = "<<nwd(a,b)<<endl;
 return 0;
}
