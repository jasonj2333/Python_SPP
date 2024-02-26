//algorytm obliczajacy iloczyn n kolejnych liczb naturalnych: 3, 4, 5, 6... (n>0)
#include <iostream>
using namespace std;
int main()
{
 int n;
 cout<<"podaj liczbe elementow n: ";
 cin>>n;
 int s=1, i=3;
 while (i<=n+2)
 {
  s=s*i;
  i++;
 }
 cout<<"s = "<<s<<endl;
 return 0;
}
