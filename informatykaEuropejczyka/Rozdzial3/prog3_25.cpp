#include <iostream>
using namespace std;

int a;                                          //zmienna globalna a

void oblicz1 (void)                             //zmienna lokalna a przeslania zmienna globalna a
{
 int a;
 a=5;
 cout<<"- w funkcji oblicz1: "<<a<<endl;
}

void oblicz2 (void)                             //operacje wykonywane na zmiennej globalnej a
{
 a=10;
 cout<<"- w funkcji oblicz2: "<<a<<endl;
}

void oblicz3 (int &z)
{
 z=-2;
 cout<<"- w funkcji oblicz3: "<<z<<endl;
}

void oblicz4 (int z)
{
 z=-15;
 cout<<"- w funkcji oblicz4: "<<z<<endl;
}

int main()
{
 a=0;
 cout<<"przebieg wartosci zmiennej a:"<<endl;
 cout<<"- poczatek programu: "<<a<<endl;                        //0
 oblicz1();                                                     //5
 cout<<"- po wykonaniu funkcji oblicz1: "<<a<<endl;             //0
 oblicz2();                                                     //10
 cout<<"- po wykonaniu funkcji oblicz2: "<<a<<endl;             //10
 oblicz3(a);                                                    //-2      zmienna globalna a jako parametr z przekazywany przez referencjê
 cout<<"- po wykonaniu funkcji oblicz3: "<<a<<endl;             //-2
 oblicz4(a);                                                    //-15     zmienna globalna a jako parametr z przekazywany przez wartosc
 cout<<"- po wykonaniu funkcji oblicz4: "<<a<<endl;             //-2
 return 0;
}
