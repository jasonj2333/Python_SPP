#include <iostream>
using namespace std;
int main()
{
 int m=8, n=0, wynik;
 wynik=m||n;
 cout<<wynik<<"\t";
 wynik=m&&n;
 cout<<wynik<<"\t";
 wynik=!m;
 cout<<wynik<<"\t";
 wynik=!n;
 cout<<wynik<<endl;
 return 0;
}
