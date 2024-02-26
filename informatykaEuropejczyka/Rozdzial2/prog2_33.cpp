//sortowanie tekstu przez wybor
#include <iostream>
#include <cstring>
using namespace std;

string sortuj (string s)
{
 int dl=s.size(), k;
 char pom;
 for (int i=0;i<dl-1;i++)
 {
  k=i;
  for (int j=i+1;j<dl;j++)
   if (s[j]<s[k]) k=j;
  pom=s[k];
  s[k]=s[i];
  s[i]=pom;
 }
 return s;
}

int main()
{
 string s;
 cout<<"podaj tekst bez spacji:"<<endl;
 cin>>s;
 cout<<"posortowany tekst:\n"<<sortuj(s)<<endl;
 return 0;
}
