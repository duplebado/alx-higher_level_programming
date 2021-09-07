#include "lists.h"

/**
 * check_cycle - Checks if a  singly linked list has a cycle in it
 * @list: The single linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *tmp = list;

	while (tmp && tmp->next)
	{
		current = current->next;
		tmp = tmp->next->next;

		if (current == tmp)
			return (1);
	}

	return (0);
}
