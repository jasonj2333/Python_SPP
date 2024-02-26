#include <iostream>
using namespace std;

class pierwsza
{
 protected:
  int a;
  int b;
 public:
  pierwsza(int a, int b);
  ~pierwsza();
  virtual void oblicz1();
  virtual void oblicz2();
  int oblicz();
  int wypiszA();
  int wypiszB();
};

class druga: public pierwsza
{
  int c;
 public:
  druga(int a, int b, int c);
  ~druga();
  void oblicz1();
  void oblicz2();
  int wypiszC();
};

pierwsza::pierwsza(int aa, int bb): a(aa), b(bb)
{}
pierwsza::~pierwsza()
{}

void pierwsza::oblicz1()
{
 a*=2;
}

void pierwsza::oblicz2()
{
 b*=2;
}

int pierwsza::oblicz()
{
 oblicz1();
 oblicz2();
 return a+b;
}

druga::druga(int aa, int bb, int cc=3): pierwsza(aa, bb), c(cc)
{}
druga::~druga()
{}

void druga::oblicz1()
{
 a*=c;
}

void druga::oblicz2()
{
 b*=c;
}

int pierwsza::wypiszA()
{
 return a;
}

int pierwsza::wypiszB()
{
 return b;
}

int druga::wypiszC()
{
 return c;
}

int main()
{
 pierwsza *P = new pierwsza(2,3);
 druga *D;
 D = new druga(3,4);
 cout<<"klasa PIERWSZA"<<endl;
 cout<<"a="<<P->wypiszA()<<"\nb="<<P->wypiszB()<<endl;
 cout<<"wynik="<<P->oblicz()<<endl;
 cout<<"\nklasa DRUGA"<<endl;
 cout<<"a="<<D->wypiszA()<<"\nb="<<D->wypiszB()<<"\nc="<<D->wypiszC()<<endl;
 cout<<"wynik="<<D->oblicz()<<endl;
 delete P;
 delete D;
 return 0;
}
