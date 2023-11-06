#include "lists.h"
/**
 * reverse_list - function to reverse a singly linked list
 * @head: the start of the linked list
 * Return: The previous list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - function that checks if a singly linked lis is a palindrome
 * @head: the start of the linked list
 * Return: 0 if not a palindrome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_half;
	listint_t *prev_slow = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/*Finding the middle of the list*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/*if list is an odd number off elements, skip the middle element*/
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;/*Split the list into two halves*/
	/*reverse the second half of the list*/
	second_half = reverse_list(second_half);

	listint_t *list1 = *head;
	listint_t *list2 = second_half;

	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	/*Restore the original list by reversing the second half again*/
	second_half = reverse_list(second_half);
	prev_slow->next = second_half;
	return (1);
}
