#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 int k=241;
 cout<<"k = "<<k<<endl;
 cout<<"konwersja systemow liczbowych:"<<endl;
 cout<<"szesnastkowy = "<<hex<<k<<endl;
 cout<<"dziesietny = "<<dec<<k<<endl;
 cout<<"szesnastkowy = "<<setfill('0')<<setw(6)<<hex<<k<<endl;
 cout<<"osemkowy = "<<setfill('*')<<setw(10)<<oct<<k<<endl;
 return 0;
}
