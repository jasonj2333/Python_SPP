//algorytm wyznaczajacy najmniejsza wspolna wielokrotnosc
#include <iostream>
using namespace std;

void dane (int &n, char nazwa)
{
 cout<<"podaj "<<nazwa<<": ";
 cin>>n;
}

int nwd (int x, int y)
{
 if (x==y) return x;
 if (x>y) return nwd(x-y,y);
 return nwd(x,y-x);
}

int nww (int a, int b)
{
 return a*b/nwd(a,b);
}

int main()
{
 int a,b;
 dane(a,'a');
 dane(b,'b');
 cout<<"NWW("<<a<<","<<b<<") = "<<nww(a,b)<<endl;
 return 0;
}
