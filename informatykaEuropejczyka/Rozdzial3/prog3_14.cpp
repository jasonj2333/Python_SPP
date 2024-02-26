#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 int a=5;
 while (a<10)
 {
  cout<<setw(6)<<a;
  a++;
 }
 cout<<endl;
 return 0;
}
