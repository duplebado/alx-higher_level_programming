  
#include "lists.h"

/**
 * check_cycle - Checks if a  singly linked list has a cycle in it
 * @list: The single linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *headCache = list;

	while (list && list->next)
	{
		if (list->next == headCache)
			return (1);

		list = list->next;
	}

	return (0);
}
