//konwersja systemu dziesietnego na dwojkowy
#include <iostream>
using namespace std;
const int MAX = 100;

void oblicz (long liczba, int &i, int W[])
{
 i=0;
 do
 {
  W[i]=liczba % 2;
  liczba=liczba/2;
  i++;
 }
 while (liczba!=0);
}

int main()
{
 int W[MAX], dl;
 long liczba;
 cout<<"podaj liczbe w systemie dziesietnym do zamiany: ";
 cin>>liczba;
 oblicz(liczba,dl,W);
 cout<<liczba<<"(10) = ";
 for (int i=dl-1;i>=0;i--) cout<<W[i];
 cout<<"(2)"<<endl;
 return 0;
}
