//sprawdzanie, czy slowo jest palindromem
#include <iostream>
#include <cstring>
using namespace std;

bool sprawdz (string s)
{
 int dl=s.size();
 for (int i=0;i<dl/2;i++)
  if (s[i]!=s[dl-i-1]) return false;
 return true;
}

int main()
{
 string s;
 cout<<"podaj wyraz: ";
 cin>>s;
 if (sprawdz(s)) cout<<"\nslowo "<<s<<" jest palindromem"<<endl;
 else cout<<"\nslowo "<<s<<" nie jest palindromem"<<endl;
 return 0;
}

