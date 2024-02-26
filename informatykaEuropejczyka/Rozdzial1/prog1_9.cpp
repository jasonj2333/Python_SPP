//algorytm rekurencyjny rozwiazujacy zagadke wiez Hanoi
#include <iostream>
using namespace std;

void oblicz (int n, char a, char b, char c)
{
 if (n>0)
 {
  oblicz(n-1,a,c,b);
  cout<<a<<" na "<<b<<endl;
  oblicz(n-1,c,b,a);
 }
}

int main()
{
 int n;
 cout<<"podaj liczbe krazkow n: ";
 cin>>n;
 cout<<"rozwiazanie zagadki WIEZE HANOI:"<<endl;
 oblicz(n,'A','B','C');
 return 0;
}
