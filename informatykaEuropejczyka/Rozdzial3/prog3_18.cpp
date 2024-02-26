#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 int k=0;
 while (k<9)
 {
  k++;
  if (k==4||k==6) continue;
  cout<<setw(5)<<k;
 }
 cout<<endl;
 return 0;
}
