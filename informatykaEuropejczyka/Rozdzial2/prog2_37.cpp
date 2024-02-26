//szyfrowanie metoda plotowa - wysokosc 3
#include <iostream>
#include <cstring>
using namespace std;

void wyswietl (string s)
{
 int dl;
 dl=s.size();
 for (int i=0;i<3;i++)
 {
  for (int j=0;j<dl;j++)
  {
   if (i==0)
    if (!(j%4)) cout<<s[j]; else cout<<" ";
   else if (i==1)
         if (j%2) cout<<s[j]; else cout<<" ";
        else
         if (!((j-2)%4)) cout<<s[j]; else cout<<" ";
  }
  cout<<endl;
 }
}

string szyfruj (string tekst)
{
 string wynik;
 int dl=tekst.size();
 for (int i=0;i<dl;i+=4) wynik+=tekst[i];
 for (int i=1;i<dl;i+=2) wynik+=tekst[i];
 for (int i=2;i<dl;i+=4) wynik+=tekst[i];
 return wynik;
}

int main()
{
 string tekst;
 cout<<"podaj tekst jawny: ";
 cin>>tekst;
 wyswietl(tekst);
 cout<<"szyfrogram: "<<szyfruj(tekst)<<endl;
 return 0;
}
