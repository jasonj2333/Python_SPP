//algorytm realizujacy naiwne wyszukiwanie wzorca w tekscie
#include <iostream>
#include <cstring>
using namespace std;

bool szukaj (string s, string wzorzec, int T[], int &n)
{
 int dlT=s.size(), dlW=wzorzec.size(), j;
 if (dlW>dlT) return false;
 n=0;
 for (int i=0;i<dlT-dlW+1;i++)
 {
  for (j=i;j<i+dlW;j++)
   if (s[j]!=wzorzec[j-i]) break;
  if (j==i+dlW)
  {
   T[n]=i;
   n++;
  }
 }
 if (n==0) return false;
 return true;
}

int main()
{
 string s, wzorzec;
 int n, T[256]={0};
 cout<<"podaj przeszukiwany tekst: ";
 cin>>s;
 cout<<"podaj wzorzec: ";
 cin>>wzorzec;
 if (szukaj(s,wzorzec,T,n))
 {
  cout<<"liczba wystapien wzorca: "<<n<<endl;
  cout<<"pozycje wystapienia wzorca:"<<endl;
  for (int i=0;i<n;i++) cout<<T[i]<<"\t";
  cout<<endl;
 }
 else cout<<"\nwzorzec nie wystepuje w tekscie"<<endl;
 return 0;
}

