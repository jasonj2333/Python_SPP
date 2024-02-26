//algorytm obliczajacy sume n kolejnych liczb naturalnych: 1, 2, ..., n
#include <iostream>
using namespace std;
int main()
{
 int n, s;
 cout<<"podaj n: ";
 cin>>n;
 if (n>=1) {s=n*(n+1)/2;  cout<<"s = "<<s<<endl;}
 else cout<<"n<1"<<endl;
 return 0;
}
