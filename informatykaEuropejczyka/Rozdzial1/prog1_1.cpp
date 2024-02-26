//algorytm wyznaczajacy pierwiastki rownania liniowego ax+b=0
#include <iostream>
using namespace std;
int main()
{
 double a, b, x;
 cout<<"podaj a, b:"<<endl;
 cin>>a>>b;
 if (a!=0) {x=-b/a; cout<<"x = "<<x<<endl;}
 else if (b==0) cout<<"nieskonczenie wiele rozwiazan"<<endl;
      else cout<<"rownanie sprzeczne"<<endl;
 return 0;
}
