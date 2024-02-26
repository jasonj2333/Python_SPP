//algorytm rekurencyjny wyznaczajacy n-ty element ciagu Fibonacciego
#include <iostream>
using namespace std;

int oblicz (int n)
{
 if (n==1||n==2) return 1;
 return oblicz(n-1)+oblicz(n-2);
}

int main()
{
 int n;
 cout<<"podaj n: ";
 cin>>n;
 cout<<"rekurencyjnie: "<<n<<" element ciagu = "<<oblicz(n)<<endl;
 return 0;
}
