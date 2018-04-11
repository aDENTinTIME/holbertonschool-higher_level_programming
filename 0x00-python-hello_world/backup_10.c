#include "lists.h"

/**
 * check_cycle - Checks if a list cycles.
 *
 * @list: Head of list to check.
 * Return: 0 if it does not cycle, 1 if it does.
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list->next;

	while (current != NULL)
	{
		if (current == list)
			return (1);

		current = current->next;
	}

	return (0);
}
