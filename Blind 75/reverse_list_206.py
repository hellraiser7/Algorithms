from calendar import c


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseList(self):
        #base case: empty list or only one element
        temp = self.head
        if (not temp or temp.next == None):
            return temp

        previousNode = None
        nextNode = None
        current = temp

        while (current):
            # just some manipulation, need to revise this more times in order to get the process ingrained
            nextNode = current.next
            current.next = previousNode
            previousNode = current
            current = nextNode
        temp = previousNode # relocate to prev, since current will be at null
        return temp
    
    def printList(self, head):
        temp = head
        llist = ""
        while (temp):
            llist += str(temp.val) + "->"
            temp = temp.next
        return llist[:-2]            

if __name__ == "__main__":
    # appending/making the list
    list = LinkedList()
    list.head = ListNode(1)
    list.head.next = ListNode(2)
    list.head.next.next = ListNode(3)
    list.head.next.next.next = ListNode(4)

    reversedHead = list.reverseList()
    print(list.printList(reversedHead))


