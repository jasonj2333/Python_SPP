#include <iostream>
using namespace std;

void wypisz (int a)
{
 cout<<"liczba calkowita: "<<a<<endl;
}

void wypisz (double a)
{
 cout<<"liczba rzeczywista: "<<a<<endl;
}

void wypisz (char a)
{
 cout<<"znak: "<<a<<endl;
}

void wypisz (char *a)
{
 cout<<"tablica znakow: "<<a<<endl;
}

int main()
{
 int x=55;
 float y=30.45;
 char z='A';
 char s[10]="tekst";
 wypisz (x);
 wypisz (y);
 wypisz (z);
 wypisz (s);
 return 0;
}
