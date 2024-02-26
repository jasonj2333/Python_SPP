//wyznaczanie wartosci wielomianu schematem Hornera - iteracja
#include <iostream>
using namespace std;
const int MAX = 100;

double oblicz (double A[], int n, double x)
{
 double w=A[0];
 for (int i=1;i<=n;i++) w=w*x+A[i];
 return w;
}

int main()
{
 double A[MAX], x;
 int n;
 cout<<"podaj wartosc argumentu x: ";
 cin>>x;
 cout<<"podaj stopien wielomianu n: ";
 cin>>n;
 cout<<"podaj "<<n+1<<" wspolczynnikow wielomianu:"<<endl;
 for (int i=0;i<=n;i++)
 {
  cout<<"A["<<i<<"] = ";
  cin>>A[i];
 }
 cout<<"iteracyjnie: wynik = "<<oblicz(A,n,x)<<endl;
 return 0;
}
