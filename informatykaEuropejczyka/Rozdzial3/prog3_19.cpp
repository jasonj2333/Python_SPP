#include <iostream>
using namespace std;

int funkcja1 (void)
{
 int a=2, b=5;
 return a+b;
}

void funkcja2 (void)
{
 int a=2, b=5;
 cout<<a+b<<endl;
}

int main()
{
 cout<<funkcja1()<<endl;
 funkcja2();
 return 0;
}
