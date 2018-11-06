def insertNodeAtPosition(head, data, position):
    count = 0
    newNode = SinglyLinkedListNode(data)
    if head is None:
        return newNode
    currentNode = head
    while count < position - 1 and currentNode:
        currentNode = currentNode.next
        count = count + 1
 

    nextNode = currentNode.next
    currentNode.next = newNode
    newNode.next = nextNode
    
    return head
