//algorytm "delty" rozwiazujacy rownanie kwadratowe
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
 double a, b, c, delta, x1, x2;
 cout<<"podaj wspolczynniki rownania a, b, c:"<<endl;
 cin>>a>>b>>c;
 if (a==0) cout<<"to nie jest rownanie kwadratowe"<<endl;
 else
 {
  delta=b*b-4*a*c;
  if (delta<0) cout<<"rownanie nie ma pierwiastkow"<<endl;
  else if (delta==0) {x1=-b/(2*a); cout<<"x="<<x1<<endl;}
       else
       {
        x1=(-b-sqrt(delta))/(2*a);
        x2=(-b+sqrt(delta))/(2*a);
        cout<<"x1="<<x1<<"\tx2="<<x2<<endl;
       }
 }
 return 0;
}
