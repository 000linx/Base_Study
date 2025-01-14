#include<bits/stdc++.h>
using namespace std;
int L, n;
int main()
{
	int n,sum=1;
	cin>>n;
	for(int i=1;i<=n;i++){
		sum=sum*i;
	}
	int a=log2(n);
	int b=(double)n*log2(n);
	int c=sqrt(n);
	cout<<a<<endl<<c<<endl<<n<<endl<<b<<endl<<pow(n,2)<<endl<<pow(n,3)<<endl<<pow(2,n)<<endl<<sum;
	return 0;
}