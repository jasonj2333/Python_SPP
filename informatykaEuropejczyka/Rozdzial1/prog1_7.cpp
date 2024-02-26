//algorytm rekurencyjny obliczajacy n! (n>=0)
#include <iostream>
using namespace std;

int oblicz (int n)
{
 if (n==0) return 1;
 return oblicz(n-1)*n;
}

int main()
{
 int n;
 cout<<"podaj n: ";
 cin>>n;
 cout<<"rekurencyjnie: "<<n<<"! = "<<oblicz(n)<<endl;
 return 0;
}
