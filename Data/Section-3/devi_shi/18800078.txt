#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char b[1000006];
	int i;
	scanf("%s",b);
		printf("%s",b );
	for(i=strlen(b)-1;i>=0;i--)
		printf("%c",b[i] );
	printf("\n");
}