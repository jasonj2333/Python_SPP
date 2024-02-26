//konwersja systemu dwojkowego na dziesietny z zastosowaniem schematu Hornera - iteracja
#include <iostream>
using namespace std;
const int MAX = 100;

long oblicz (int A[], int n)
{
 long w=A[0];
 for (int i=1;i<=n;i++) w=w*2+A[i];
 return w;
}

int main()
{
 int A[MAX];
 long w;
 int n;
 cout<<"podaj liczbe cyfr wczytywanej liczby binarnej: ";
 cin>>n;
 cout<<"podaj "<<n<<" cyfr liczby (od lewej):"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"A["<<i<<"] = ";
  cin>>A[i];
 }
 cout<<"iteracyjnie: wynik = "<<oblicz(A,n-1)<<"(10)"<<endl;
 return 0;
}
