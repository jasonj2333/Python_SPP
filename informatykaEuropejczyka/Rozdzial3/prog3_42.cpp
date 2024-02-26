#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int main ()
{
 ifstream fin("dane1.txt");
 ofstream fout("wyniki1.txt");
 string s;
 while (!fin.eof())
 {
  fin>>s;
  if (s.size()%2==0) fout<<s<<"\n";
 }
 fin.close();
 fout.close();
 return 0;
}
