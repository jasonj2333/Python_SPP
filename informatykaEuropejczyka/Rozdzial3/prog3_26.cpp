#include <iostream>
using namespace std;

void dane (int *n)
{
 cout<<"podaj liczbe naturalna n: ";
 cin>>*n;
}

int obliczSume (int n)
{
 int s=0;
 for (int i=1;i<=n;i++) s+=i;
 return s;
}

double obliczIloczyn (int n)
{
 double s=1;
 for (int j=1;j<=n;j++) s*=(double)j/2;
 return s;
}

double oblicz (int n)
{
 return 2.*n/obliczSume(n)-obliczIloczyn(n);
}

int main()
{
 int n;
 dane(&n);
 cout<<"w = "<<oblicz(n)<<endl;
 return 0;
}
