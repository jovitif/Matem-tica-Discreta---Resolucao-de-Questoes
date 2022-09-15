#include <iostream>

using namespace std;


int fi(int n)
{
	int m=1;
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
		if(primo==true && n % i == 0)
		{
			// valor de m
			m = m*i;
			// (p1-1)(p2-1)…(pk-1)
			rec=rec*(i-1);
		}
	}
	// fi(n)=n/m(p1-1)(p2-1)...(pk-1)
	int x = n/m * (rec);
	return x;
} 

int main()
{
	int n;
	
	cout << "insira o valor de n :" << endl;
	cin >> n;
	int x = fi(n);
	
	cout << "Resultado :"<< x << endl;
}
