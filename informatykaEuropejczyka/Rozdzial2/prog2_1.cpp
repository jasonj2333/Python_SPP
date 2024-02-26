//algorytm sprawdzajacy, czy punkt P lezy na prostej 3x+4y–4 = 0
#include <iostream>
#include <cmath>
using namespace std;

bool szukaj (double x0, double y0)
{
 double d=abs(3*x0+4*y0-4)/sqrt(pow(3.0,2)+pow(4.0,2));
 if (d==0) return true;
 else return false;
}

int main()
{
 double x0, y0;
 cout<<"podaj wspolrzedne punktu: ";
 cin>>x0>>y0;
 if (szukaj(x0,y0)) cout<<"punkt P=("<<x0<<";"<<y0<<") lezy na prostej 3x+4y-4=0"<<endl;
 else cout<<"punkt P=("<<x0<<";"<<y0<<") nie lezy na prostej 3x+4y-4=0"<<endl;
 return 0;
}
