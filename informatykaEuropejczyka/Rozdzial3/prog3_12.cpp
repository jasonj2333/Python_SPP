#include <iostream>
using namespace std;
int main()
{
 int a=1, b=2;
 while (a<10)
 {
  a+=3;
  b*=7+a;
 }
 cout<<a<<" "<<b<<endl;
 return 0;
}
