#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 double x=22.111111111, y=3.5555555555555, w, z;
 cout<<"podaj liczbe rzeczywista: ";
 cin>>w;
 cout<<"\nx = "<<setw(10)<<x<<endl;
 cout<<"\ny = "<<setfill('0')<<setw(12)<<y<<endl;
 cout<<"\ny = "<<setprecision(8)<<setfill('0')<<setw(12)<<y<<endl;
 cout<<"\nw = "<<setfill('*')<<setw(15)<<w<<endl;
 cout<<"\nx + y + w = "<<setprecision(9)<<x+y+w<<endl;
 cout<<"\nx * y = "<<setprecision(8)<<x*y<<endl;
 return 0;
}
