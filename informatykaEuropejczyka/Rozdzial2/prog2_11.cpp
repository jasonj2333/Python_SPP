//badanie, czy liczba jest pierwsza
#include <iostream>
using namespace std;

bool sprawdz (int n)
{
 for (int i=2;i<n;i++)
  if (n%i==0) return false;
 return true;
}

int main()
{
 int n;
 cout<<"podaj liczbe naturalna wieksza od 1: ";
 cin>>n;
 if (sprawdz(n)) cout<<n<<" jest liczba pierwsza"<<endl;
 else cout<<n<<" jest liczba zlozona"<<endl;
 return 0;
}
