#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *runner1, *runner2;

	if (list == NULL || list->next == NULL)
		return (0);

	runner1 = list;
	runner2 = list->next;

	for (; runner2 != NULL && runner2->next != NULL;
	runner1 = runner1->next, runner2 = runner2->next->next)
	{
		if (runner1 == runner2)
			return (1);
	}

	return (0);
}
