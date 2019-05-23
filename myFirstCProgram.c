#include<stdio.h>

main(void)
{
	double f,c;
	double low, up, step;

	low = 0;
	up = 3000;
	step = 1;
	f = low;
	while(f <= up)
	{
		c = 5* (f-32) / 9;
		printf("%f\t%f\n", f, c);
		f = f + step;
	}
	
}
