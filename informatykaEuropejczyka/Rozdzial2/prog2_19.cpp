//znajdowanie lidera w zbiorze
#include <iostream>
using namespace std;
const int MAX = 100;

void szukaj (double T[], int n)
{
 double lider=T[0];
 int pom=1, ilosc=0;
 for (int i=1;i<n;i++)
  if (pom==0)
  {
   lider=T[i];
   pom=1;
  }
  else if (T[i]==lider) pom++;
       else pom--;
 if (pom==0) cout<<"w zbiorze nie ma lidera"<<endl;
 else
 {
  for (int i=0;i<n;i++)
   if (T[i]==lider) ilosc++;
  if (ilosc>n/2) cout<<"liczba "<<lider<<" jest liderem"<<endl;
  else cout<<"w zbiorze nie ma lidera"<<endl;
 }
}

int main()
{
 double T[MAX];
 int n;
 cout<<"podaj liczbe elementow: ";
 cin>>n;
 cout<<"podaj elementy zbioru:"<<endl;
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
 szukaj(T,n);
 return 0;
}
