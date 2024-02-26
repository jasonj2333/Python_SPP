#include <iostream>
using namespace std;

int main()
{
 int n;
 cout<<"podaj liczbe elementow w tablicy: ";
 cin>>n;
 double *T=NULL;
 T=new double [n];
 for (int i=0;i<n;i++)
 {
  cout<<"T["<<i<<"] = ";
  cin>>T[i];
 }
 for (int i=0;i<n;i++) cout<<T[i]<<"\t";
 cout<<endl;
 delete [] T;
 return 0;
}
