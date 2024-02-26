#include <iostream>
using namespace std;

void funkcja (int n)
{
 n=n+2;
 cout<<"wewnatrz funkcji: "<<n<<endl;
}

int main()
{
 int a=5;
 funkcja(a);
 cout<<"na zewnatrz funkcji: "<<a<<endl;
 return 0;
}
