#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
 int liczba;
 srand(time(NULL));
 liczba=rand()%11;
 cout<<liczba<<endl;
 return 0;
}
