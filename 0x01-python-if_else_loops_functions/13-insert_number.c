#include "lists.h"
/**
 * insert_node - this function will insert node in a linked list
 * @head: this is the first part of the linked list
 * @number: this is the number to be inserted in the linked list
 * Return: the updated linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *r = malloc(sizeof(listint_t));
	/*checking if memory is allocated*/
	if (r == NULL)
	{
		return (NULL);
	}
	/*creating the node to be commpared with*/
	r->n = number;
	r->next = NULL;
	/*looking if head is null or the number is greatier than the number in the head*/
	if (*head == NULL || number < (*head)->n)
	{
		/*creating a node at the beginning of the node*/
		r->next = *head;
		*head = r;
		return (r);
	}

	temp = *head;/*Pointing temp at the head of the linked list*/
	while(temp->next != NULL && number > temp->next->n)
	{
		temp = temp->next;/*iterate through the linked list*/
	}
	r->next = temp->next;/*r->next will point where temp->next was pointing*/
	temp->next = r;/*temp->next points to r to complete the linkage*/

	return (r);
}
