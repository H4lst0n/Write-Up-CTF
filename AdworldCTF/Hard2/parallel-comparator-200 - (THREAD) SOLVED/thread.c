#include <conio.h>
#include "pthread.h"
#include <stdio.h>

void * printx(void * data)
{
	while(1)
	{
		printf("x\n");
	}
}

int main(int argc, char * argv[])
{
	pthread_t idthread;
	pthread_create(&idthread,NULL,&printx,NULL);
	while(1)
	{
		printf("o");
	}
	return 0;
}

// Nó sẽ tạo ra 1 thread mới chạy song song với thread cũ 
