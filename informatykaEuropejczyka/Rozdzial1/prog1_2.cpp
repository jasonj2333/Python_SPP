//algorytm obliczajacy sume n kolejnych liczb naturalnych: 1, 2, ..., n (n>0)
#include <iostream>
using namespace std;
int main()
{
 int n, s;
 cout<<"podaj n: ";
 cin>>n;
 s=n*(n+1)/2;
 cout<<"s = "<<s<<endl;
 return 0;
}
