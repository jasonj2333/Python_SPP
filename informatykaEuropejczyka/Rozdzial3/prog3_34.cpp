#include <iostream>
#include <cstring>
using namespace std;

void wczytaj (char s[])
{
 cout<<"podaj tekst: ";
 cin.getline(s,256);
}

char *zamien1 (char s[])
{
 int dl=strlen(s);
 for (int i=0;i<dl;i++)
  if (s[i]=='a') s[i]='*';
 return s;
}

char *zamien2 (char s[])
{
 int dl=strlen(s);
 for (int i=0;i<dl;i++)
  if (s[i]!='m'&&s[i]!='n') s[i]='U';
 return s;
}

int main()
{
 char s[256];
 wczytaj(s);
 cout<<"\ntekst po zamianie 1: "<<zamien1(s)<<endl;
 cout<<"tekst po zamianie 2: "<<zamien2(s)<<endl;
 return 0;
}
