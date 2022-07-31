from traceback import print_list


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

    def mergeTwoLists(self, list1, list2):
        #base case when one of them is empty
        A,B = list1, list2
        if not A:
            return B
        elif not B:
            return A
        A,B,current = self.getNewHead(A,B) # new vals after new head is in place
        return self.mergeLinkedLists(A,B,current)

    def mergeLinkedLists(self, A, B, current):
        # compare A and B pointers, and move current ptr accordingly
        temp = current # store new head for returning
        while (A and B):
            if (A.val <= B.val):
                current.next = A
                current = A
                A = A.next
            elif (B.val < A.val):
                current.next = B
                current = B
                B = B.next
        # if B is empty
        if (not B):
            current.next = A
        # if A is empty
        elif (not A):
            current.next = B
        return temp

    def getNewHead(self, A, B):
        if A.val <= B.val:
            current = A
            A = A.next
        elif B.val < A.val:
            current = B
            B = B.next
        return A,B,current

if __name__ == "__main__":
    # appending/making the list
    list1 = LinkedList()
    list1.head = ListNode(1)
    list1.head.next = ListNode(3)
    list1.head.next.next = ListNode(5)
    list1.head.next.next.next = ListNode(7)
    list1.head.next.next.next.next = ListNode(8)

    list2 = LinkedList()
    list2.head = ListNode(2)
    list2.head.next = ListNode(4)
    list2.head.next.next = ListNode(6)
    print("List 1 is: ", list1.printList(list1.head))
    print("List 2 is: ", list2.printList(list2.head))
    newHead = list2.mergeTwoLists(list1.head, list2.head)
    print("The merged and sorted super list is: ", list2.printList(newHead))