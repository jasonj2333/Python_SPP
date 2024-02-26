#include <iostream>
#include <fstream>
using namespace std;

void wczytajBezSpacji (char *nazwapliku)
{
 char s[256];
 ofstream fout (nazwapliku);
 if (!fout) cout<<"plik nie zostal otwarty"<<endl;
 else
  {
   for (int i=1;i<=3;i++)
   {
    cout<<"\npodaj tekst bez spacji nr "<<i<<": ";
    cin>>s;
    fout<<endl<<s;
   }
   fout.close();
   cout<<endl;
  }
}

void wczytajZeSpacjami (char *nazwapliku)
{
 char s[256];
 ofstream fout (nazwapliku);
 if (!fout) cout<<"plik nie zostal otwarty"<<endl;
 else
 {
  for (int i=1;i<=3;i++)
  {
   cout<<"\npodaj tekst ze spacjami nr "<<i<<": ";
   cin.getline(s,sizeof(s));
   fout<<endl<<s;
  }
  fout.close();
  cout<<endl;
 }
}

void wypiszSlowa (char *nazwapliku)
{
 char s[256];
 ifstream fin(nazwapliku);
 if (!fin) cout<<"plik nie zostal otwarty"<<endl;
 else
 {
  cout<<"\nwczytane wyrazy:"<<endl;
  while (!fin.eof())	//sprawdza, czy uzyskaliœmy koniec pliku
  {
   fin>>s;
   cout<<s<<endl;
  }
  fin.close();
 }
 cin.ignore();
}

void wypiszZnaki (char *nazwapliku)
{
 char znak;
 ifstream fin(nazwapliku);
 if (!fin) cout<<"plik nie zostal otwarty"<<endl;
 else
 {
  cout<<"\nwczytane znaki:"<<endl;
//    while (!fin.eof())
//    {
//      fin.get(znak);                  //fin>>znak;
//      cout<<znak;
//    }
  while (fin.get(znak)) cout<<znak;
  cout<<endl;
  fin.close();
 }
 cin.ignore();
}

void wypiszWiersze (char *nazwapliku)
{
 char s[256];
 ifstream fin(nazwapliku);
 if (!fin) cout<<"plik nie zostal otwarty"<<endl;
 else
 {
  cout<<"\nwczytany tekst ze spacjami:"<<endl;
//    while (!fin.eof())
//    {
//      fin.getline(s,sizeof(s));
//      cout<<s<<endl;
//    }
  while (fin.getline(s,sizeof(s))) cout<<s<<endl;
  cout<<endl;
  fin.close();
 }
 cin.ignore();
}

int main()
{
 char *plik="plik.txt";
 wczytajBezSpacji(plik);
 wypiszSlowa(plik);
 wczytajZeSpacjami(plik);
 wypiszSlowa(plik);
 wypiszZnaki(plik);
 wypiszWiersze(plik);
 return 0;
}
