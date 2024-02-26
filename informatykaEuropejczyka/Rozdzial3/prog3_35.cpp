#include <iostream>
#include <cstring>
using namespace std;

int main()
{
 string s1, s2("Ala"), s3="Ola";
 s1="Ala";
 if (s1==s2) cout<<"teksty "<<s1<<" i "<<s2<<" sa takie same"<<endl;
 else if (s1<s2) cout<<"tekst "<<s1<<" jest wczesniej w slowniku niz tekst "<<s2<<endl;
  else cout<<"tekst "<<s1<<" nie jest pozniej w slowniku niz tekst "<<s2<<endl;
 s2+='n';
 if (s1==s2) cout<<"teksty "<<s1<<" i "<<s2<<" sa takie same"<<endl;
 else if (s1<s2) cout<<"tekst "<<s1<<" jest wczesniej w slowniku niz tekst "<<s2<<endl;
  else cout<<"tekst "<<s1<<" jest pozniej w slowniku niz tekst "<<s2<<endl;
 s3+="!!!";
 cout<<s3<<endl;
 s3[1]='*';
 cout<<s3<<endl;
 return 0;
}
