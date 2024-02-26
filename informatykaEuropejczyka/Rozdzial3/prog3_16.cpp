#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 int a=7;
 do
 {
  cout<<setw(6)<<a;
  a+=2;
 }
 while (a<=17);
 cout<<endl;
 return 0;
}
