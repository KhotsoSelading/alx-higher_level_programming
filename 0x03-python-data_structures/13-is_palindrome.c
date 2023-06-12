#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the first node in the list.
 *
 * Return: Pointer to the first node in the new list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head;

	while (current)
	{
		listint_t *next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	/* Empty list or single node list is considered a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Finding the middle node of the list */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reversing the second half of the list */
	reverse_listint(&slow);
	dup = slow;

	/* Comparing the first half and reversed second half of the list */
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	return (1);
}
