#include <iostream>
#include <fstream>
using namespace std;
int main ()
{
 ifstream fin("dane2.txt");
 ofstream fout("wyniki2.txt");
 int liczba1, liczba2, iloczyn;
 while (!fin.eof())
 {
  fin>>liczba1>>liczba2;
  iloczyn=liczba1*liczba2;
  if (iloczyn>=250&&iloczyn<=3000)
   fout<<iloczyn<<"\n";
 }
 fin.close();
 fout.close();
 return 0;
}
