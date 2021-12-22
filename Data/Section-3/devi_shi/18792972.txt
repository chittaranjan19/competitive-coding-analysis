#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int n,k,tr=1;
	scanf("%d",&n);
	scanf("%d",&k);
	int m=k,t=0,p=0,ans=0;
	while(k--)
	{
		int flag=0,t=0;
		char a[m+5];
		scanf("%s",a);

		while(flag!=1 && t<strlen(a))
		{
			if(a[t]=='0')
			{
				flag=1;
				ans++;

			}
			else if(a[t]=='1' && t==strlen(a)-1)
			{
				if(ans>p)
					p=ans;
				ans=0;
				flag=1;

			}
			else
				t++;
		}	
		if(ans>p)
			p=ans;
	}
	printf("%d\n",p);
	return 0;
}