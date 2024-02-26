//algorytm sprawdzajacy, czy dwa slowa zlozone wylacznie z liter "X" i "Y" sa anagramami
#include <iostream>
#include <cstring>
using namespace std;

bool sprawdz (string s1, string s2)
{
 int dl=s1.size();
 if (dl!=s2.size()) return false;
 else
 {
  int T1[2]={0, 0}, T2[2]={0, 0};
  for (int i=0;i<dl;i++)
  {
   if (s1[i]=='X') T1[0]++;
   else T1[1]++;
   if (s2[i]=='X') T2[0]++;
   else T2[1]++;
  }
  for (int i=0;i<2;i++)
   if (T1[i]!=T2[i]) return false;
 }
 return true;
}

int main()
{
 string s1, s2;
 cout<<"podaj pierwszy wyraz: ";
 cin>>s1;
 cout<<"podaj drugi wyraz: ";
 cin>>s2;
 if (sprawdz(s1,s2)) cout<<"\nslowa sa anagramami"<<endl;
 else cout<<"\nslowa nie sa anagramami"<<endl;
 return 0;
}

