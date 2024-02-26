#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
 int a;
 for (a=22; a>=6; a-=3) cout<<setw(5)<<a;
 cout<<endl;
 for (int a=22; a>=6; a-=3) cout<<setw(5)<<a;
 cout<<endl;
 return 0;
}
