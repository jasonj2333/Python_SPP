//sito Eratostenesa - generowanie liczb pierwszych
#include <iostream>
using namespace std;
const int MAX=10000;

void generuj (int T[], int n)
{
 int i, m;
 for (i=2;i<=n;i++) T[i]=1;
 i=2;
 while (i<=n)
 {
  m=2*i;
  while (m<=n)
  {
   T[m]=0;
   m+=i;
  }
  do i++; while (T[i]==0 && i<=n);
 }
}

int main()
{
 int n, T[MAX];
 cout<<"podaj liczbe naturalna: ";
 cin>>n;
 generuj(T,n);
 for (int i=2;i<=n;i++)
  if (T[i]==1) cout<<i<<"\t";
 cout<<endl;
 return 0;
}
