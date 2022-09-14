#include <iostream>

using namespace std;


long double fi(int n)
{
	long double m=1;
	int rec =1;
	bool primo;
	for(int i = n;i > 1;i--)
	{
		primo = true;
		for(int j=i-1;j>1;j--)
		{
			if(i %j ==0)
			{
				primo = false;
			}
		}
		// valor de m
		if(primo==true)
		{
			m = m*i;
		}
		// (p1-1)(p2-1)…(pk-1)
		if(primo==true && n % i == 0)
		{
			rec=rec*(i-1);
		}
	}
	// fi(n)=n/m(p1-1)(p2-1)...(pk-1)
	long double x = n/m * (rec);
	return x;
} 

int main()
{
	int n;
	
	cout << "insira o valor de n :" << endl;
	cin >> n;
	long double x = fi(n);
	
	cout << "Resultado :"<< x << endl;
}

