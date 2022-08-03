#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>
using namespace std;

class Node {
    public:
    Node* next;
    int data;
};

string printList(Node* temp) {
    string result = "";
    while(temp!=NULL) {
        result += to_string(temp->data) + " ";
        temp = temp->next;
    }
    result.pop_back();
    return result;
}

/* Delete front front of the linked list, here are the steps:
1. Create another Node object temp in order to store the original head pointer
2. Reassign the head to it's next node.
3. Reassign the next pointer of temp (which is the deleted front node) to NULL, which 
effectively deletes the node.
4. Return the head of the newly formed list.
*/
Node* deleteFromFront(Node* head) {
    Node* temp = head; //step1
    head = head->next; //step2
    temp->next = NULL; //step3
    return head; //step4
}

Node* insertAtFront(Node* head, int data) {
    Node* newElement = new Node(); //created new element node: step 1
    newElement->data = data; //assign the given key
    newElement->next = head; //step 2
    head = newElement; //step 3
    return head; //return the new head
}

int main() {

    Node* head = new Node();
    

}