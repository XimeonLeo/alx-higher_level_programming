#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: the begining of the linked list
 * @number: the number to be added
 *
 * Return: the address of the new node added
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *my_node = NULL;
	listint_t *tmp_node = *head, *old = NULL;

	my_node = malloc(sizeof(listint_t));
	if (!my_node)
		return (NULL);
	my_node->n = number;

	if (!(*head))
	{
		*head = my_node;
		my_node->next = NULL;
		return (my_node);
	}
	if ((*head)->n >= number)
	{
		my_node->next = *head;
		*head = my_node;
	}
	else
	{
		while ((tmp_node) && (tmp_node->n < number))
		{
			old = tmp_node;
			tmp_node = tmp_node->next;
		}
		if (!tmp_node)
		{
			old->next = my_node;
			my_node->next = NULL;
		}
		else
		{
			old->next = my_node;
			my_node->next = tmp_node;
		}
	}
	return (my_node);

}
