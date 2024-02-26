//algorytm sprawdzajacy, czy punkt P=(3;-2) nalezy do odcinka AB
#include <iostream>
#include <cmath>
using namespace std;

bool szukaj (double x1, double y1, double x2, double y2)
{
 double AB, AP, PB;
 AB=sqrt(pow(x2-x1,2)+pow(y2-y1,2));
 AP=sqrt(pow(3-x1,2)+pow(-2-y1,2));
 PB=sqrt(pow(x2-3,2)+pow(y2+2,2));
 if (AP+PB==AB) return true;
 else return false;
}

int main()
{
 double x1, y1, x2, y2;
 cout<<"podaj wspolrzedne punktu A: ";
 cin>>x1>>y1;
 cout<<"podaj wspolrzedne punktu B: ";
 cin>>x2>>y2;
 if (szukaj(x1,y1,x2,y2)) cout<<"punkt P nalezy do odcinka AB"<<endl;
 else cout<<"punkt P nie nalezy do odcinka AB"<<endl;
 return 0;
}
