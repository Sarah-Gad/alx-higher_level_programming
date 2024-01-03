#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head
 * @number: the number to be added
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw = malloc(sizeof(listint_t));

	if (nw == NULL)
		return (NULL);
	nw->n = number;
	nw->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		nw->next = *head;
		*head = nw;
	}
	else
	{
		listint_t *od = *head;

		while (od->next != NULL && number > od->next->n)
			od = od->next;
		nw->next = od->next;
		od->next = nw;
	}
	return (nw);
}
