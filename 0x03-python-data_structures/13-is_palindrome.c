#include "lists.h"

int match(listint_t *place)
{
	if (place == NULL)
		return (1);
	if (place->n != match(place->next))
		return (0);
	return (place->n);
}

int is_palindrome(listint_t **head)
{
	return (match(*head));
}
