#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - will initialize an infinite loop
 *
 * Return: 0 if interrupted by a signal.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_process - will create a new process and print the
 * PID of the new process
 */
void create_process(void)
{
	int rc = fork();

	if (rc == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - will create 5 zombie processes
 *
 * Return: 0 for a successful program run
 */
int main(void)
{
	create_process();
	create_process();
	create_process();
	create_process();
	create_process();
	return (infinite_while());
}
