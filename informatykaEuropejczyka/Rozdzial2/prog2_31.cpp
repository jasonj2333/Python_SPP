//ogolny problem plecakowy - programowanie dynamiczne
#include <iostream>
using namespace std;
const int MAX = 50;

void wczytaj (int W[], int C[], int n)
{
 cout<<"podaj wartosci i wagi przedmiotow:"<<endl;
 for (int i=1;i<=n;i++)
 {
  cout<<i<<".   wartosc=";
  cin>>W[i];
  cout<<"     waga=";
  cin>>C[i];
 }
}

void wyswietl (int T[][MAX], int m, int n, char* komunikat)
{
 cout<<komunikat<<":"<<endl;
 for (int i=1;i<=m;i++)
 {
  for (int j=1;j<=n;j++) cout<<"\t"<<T[i][j];
  cout<<endl;
 }
}

void pakujPlecak (int W[], int C[], int n, int waga, int Wartosci[][MAX], int Numery[][MAX])
{
 for (int i=1;i<=waga;i++)
 {
  Wartosci[0][i]=0;
  Numery[0][i]=0;
 }
 for (int i=1;i<=n;i++)
 {
  Wartosci[i][0]=0;
  Numery[i][0]=0;
 }
 for (int i=1;i<=n;i++)
  for (int j=1;j<=waga;j++)
   if (j>=C[i]&&Wartosci[i-1][j]<Wartosci[i][j-C[i]]+W[i])
   {
    Wartosci[i][j]=Wartosci[i][j-C[i]]+W[i];
    Numery[i][j]=i;
   }
   else
   {
    Wartosci[i][j]=Wartosci[i-1][j];
    Numery[i][j]=Numery[i-1][j];
   }
}

int odczytajPlecak (int W[], int C[], int n, int waga, int Wartosci[][MAX], int Numery[][MAX], int K[])
{
 int wynik=Wartosci[n][waga];
 for (int i=1;i<=n;i++) K[i]=0;
 while (Numery[n][waga]>0)
 {
  K[Numery[n][waga]]+=1;
  waga-=C[Numery[n][waga]];
 }
 return wynik;
}

int main()
{
 int W[MAX], C[MAX], K[MAX], Wartosci[MAX][MAX], Numery[MAX][MAX], waga, n;
 cout<<"podaj maksymalna wage plecaka: ";
 cin>>waga;
 cout<<"podaj liczbe przedmiotow: ";
 cin>>n;
 wczytaj(W,C,n);
 pakujPlecak(W,C,n,waga,Wartosci,Numery);
 wyswietl(Wartosci,n,waga,"tablica wartosci");
 wyswietl(Numery,n,waga,"tablica numerow");
 cout<<"wartosc plecaka = "<<odczytajPlecak(W,C,n,waga,Wartosci,Numery,K)<<endl;
 cout<<"zapakowane przedmioty:"<<endl;
 for (int i=1;i<=n;i++) cout<<i<<":  ilosc="<<K[i]<<"  wartosc="<<W[i]<<"  waga="<<C[i]<<endl;
 return 0;
}
