#include "lists.h"

/**
* check_cycle - function to check cycle
* @list: list with links for checking
*
* Return: 1 success, 0 fail
*/
int check_cycle(listint_t *list)
{
	listint_t *w = list;
	listint_t *t = list;

	if (!list)
		return (0);

	while (w && t && t->next)
	{
		w = w->next;
		t = t->next->next;
		if (w == t)
			return (1);
	}

	return (0);
}
