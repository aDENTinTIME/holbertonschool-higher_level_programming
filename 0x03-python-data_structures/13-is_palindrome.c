#include "head.h"

int is_palindrome(listint_t **head)
{
	listint_t *one, *two, *three;

	one = *head;
	two = *head;
	three = *head;

	while ()
	{
		while (two->next)
			two = two->next;

		while (three->next)
			three = three->next;

		if (one == two)
			return (0);
		else
			one = one->next;

		

	}

	return (1);
}
