#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 for (int k=10; k<100; k+=5)
 {
  cout<<setw(6)<<k;
  if (k==50) break;
 }
 cout<<endl;
 return 0;
}
