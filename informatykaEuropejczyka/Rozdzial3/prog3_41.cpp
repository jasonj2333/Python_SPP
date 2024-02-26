#include <iostream>
#include <fstream>
using namespace std;
int main()
{
 ofstream plik;   //utworzenie obiektu plik klasy ofstream
 plik.open("dane.txt");   //otwarcie pliku dane.txt do zapisu
 for (int i=0;i<9;i++) plik<<i<<endl;   //zapis do pliku wartosci zmiennej i
 plik.close();   //zamkniecie pliku dane.txt
 plik.open("dane.txt");   //otwarcie pliku dane.txt do zapisu
 int a=5, b=4, c=3;
 plik<<a<<"\n"<<b<<endl<<c<<endl;   //zapis do pliku zmiennych a, b, c
 plik<<endl<<++a;   //zwiekszenie a o 1 i zapis a do pliku
 plik.close();   //zamkniecie pliku dane.txt
 return 0;
}
