#ifndef Lists_H
#define Lists_H

#include <stdlib.h>

/**
 * struct listint_s - A singly linked list
 * @n: An integer perameter
 * @next: A pointer to the next node
 *
 * Description: An ALX singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif /* Lists_H */
