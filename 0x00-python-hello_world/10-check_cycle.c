#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the head of the linked list
 * Return: 0 if there is no cycle 1 if there is a cycle in it
 */
int check_cycle(listint_t *list)
{
	/*Using the hare tortoise algorithim*/
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		/*move one step at a time*/
		slow = slow->next;
		fast = fast->next->next;/*move 2 steps at a time*/
		/*if there is a cycle, the fast pointer will eventually catch up*/
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
