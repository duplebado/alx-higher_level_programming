#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head of the list
 * @number: number to be inserted
 * Return: the address of the new node, OR
 * NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!(*head) || (*head)->n >= number)
	{
		new_node->next = *head;
		**head = *new_node;

		return (new_node);
	}

	prev_node = *head;
	current_node = (*head)->next;

	while (current_node)
	{
		if (current_node->n >= number)
		{
			prev_node->next = new_node;
			new_node->next = current_node;
			return (new_node);
		}
		
		prev_node = current_node;
		current_node = current_node->next;
	}

	current_node->next = new_node;
	new_node->next = NULL;

	return (new_node);
}
