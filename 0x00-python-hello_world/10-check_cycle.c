#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle or not
 *
 * @list: a pointer to a linked list
 *
 * Return: 0 if there is ni cycle or 1 if a cycle is found
 */

int check_cycle(listint_t *list)
{
	listint_t *slug = NULL, *flash = NULL;
	int cycle = 0;

	if (!list)
		return (0);

	slug = list;
	flash = list;

	while (slug && flash && flash->next)
	{
		slug = slug->next;
		flash = flash->next->next;

		if (slug == flash)
		{
			cycle = 1;
			break;
		}
	}
	if (cycle == 1)
		return (1);

	return (0);
}
