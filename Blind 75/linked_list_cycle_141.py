class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        temp = head
        llist = ""
        while (temp):
            llist += str(temp.val) + "->"
            temp = temp.next
        return llist[:-2]

    def hasCycle(self, head):
        # if we encounter the node again, it has a cycle (end not reached)
        # If we reach the end of the llist, we return false
        nodeAddresses = set()
        temp = head
        while (temp):
            nodeAddresses.add(temp)
            if (temp.next in nodeAddresses):
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    # appending/making the list
    llist = LinkedList()
  
    llist.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)

    llist.head.next = second
    second.next = third
    third.next = llist.head
    #print("The linked list is: ", llist.printList(llist.head))
    print("Has Cycle: ", llist.hasCycle(llist.head))


