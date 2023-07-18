#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_listint - the subroutine
* @head: the beginning
* Return: something if successful and something else if fail
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
* is_palindrome - pzalimdrome time 
* @head: start here oo
*
* Return: something for success, something else for fail
*/
int is_palindrome(listint_t **head)
{
	listint_t *p, *v, *d;
	size_t e = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	p = *head;
	while (p)
	{
		e++;
		p = p->next;
	}

	p = *head;
	for (i = 0; i < (e / 2) - 1; i++)
		p = p->next;

	if ((e % 2) == 0 && p->n != p->next->n)
		return (0);

	p = p->next->next;
	v = reverse_listint(&p);
	d = v;

	p = *head;
	while (v)
	{
		if (p->n != v->n)
			return (0);
		p = p->next;
		v = v->next;
	}
	reverse_listint(&d);

	return (1);
}
