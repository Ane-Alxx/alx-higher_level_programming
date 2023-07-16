#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_listint - function for rev
* @head:head pointer 
*
* Return: success
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
* is_palindrome - function for plinferome
* @head: well this one is obvious
*
* Return: something success
*/
int is_palindrome(listint_t **head)
{
	listint_t *p, *v, *d;
	size_t e = 0, l;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	p = *head;
	while (p)
	{
		e++;
		p = p->next;
	}

	p = *head;
	for (l = 0; l < (e / 2) - 1; l++)
		p = p->next;

	if ((e % 2) == 0 && p->n != p->next->n)
		return (0);

	p = p->next->next;
	r = reverse_listint(&p);
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
