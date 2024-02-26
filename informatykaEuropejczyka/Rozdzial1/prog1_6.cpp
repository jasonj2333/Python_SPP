//algorytm obliczajacy sume liczb wczytywanych z klawiatury nie wiekszych od 50
#include <iostream>
using namespace std;
int main()
{
 double s=0, a=0;
 do
 {
  s+=a;
  cout<<"podaj liczbe rzeczywista: ";
  cin>>a;
 }
 while(a<=50);
 cout<<"suma = "<<s<<endl;
 return 0;
}

