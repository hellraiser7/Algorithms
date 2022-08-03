#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>
using namespace std;

// Define the Node
class Node {
    public:
        int data;
        Node* next;
};

string printList(Node* temp) {
    string linkedList = "";
    while(temp!=NULL) {
        linkedList += to_string(temp->data) + " ";
        temp = temp->next;        
    }
    linkedList.pop_back();
    return linkedList;
}

// Logic for inserting a node at beginning
/* 
Steps taken are as follows:
1. Create the Node element with data and next pointer (perhaps in int main?)
   || 10 |   | -->
2. Point the next pointer of new element towards the previous beginning.
3. Remove head from previous beginning, and point it towards the new element
  
*/

Node* insertAtFront(Node* temp, int data) {
    Node* newElement = new Node(); //created new element node: step 1
    newElement->data = data; //assign the given key
    newElement->next = temp; //step 2
    temp = newElement; //step 3
    return temp; //return the new head
}

/* Inserting at the end steps:
1. Create the node element with data and next pointer
2. Traverse the linked list till you reach the end.
3. Point the next pointer of the last node (previously NULL) to the inserted node in 1.
4. Point the next pointer of inserted node to NULL.
*/

Node* insertAtEnd(Node* temp, int data) { 
    Node* tempNew = temp;
    Node* newElement = new Node(); 
    newElement->data = data; //assign the key
    while((tempNew->next)!=NULL) {
        //traverse
        tempNew = tempNew->next;
    }
    //temp contains the last node
    tempNew->next = newElement; //step 3
    newElement->next = NULL; //step 4
    return temp;   
}

/* Inserting after a specified node - steps:
1. Create the Node with given data
2. Traverse to the node in question (after which to insert new node)
3. Point the next pointer of new node to the next node pointed to by the node in question
4. Point the next pointer of node in question to new node
*/

Node* insertAfterNode(Node* temp, int data, int position) { 

    Node* tempNew = temp;
    int k=0;
    Node* newElement = new Node();
    newElement->data = data; //step 1
    while(k<position-1) {
        tempNew = tempNew->next;
        k += 1;
    } //step 2
    newElement->next = tempNew->next; //step 3
    tempNew->next = newElement; //step 4
    return temp;
}

int main() {
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();
    
    //assign data and links
    head->data = 5;
    head->next = second;
    
    second->data = 10;
    second->next = third;

    third->data = 15;
    third->next = NULL;

    //Insertion at the beginning
    
    Node* node1 = insertAtFront(head,1000);
    string result = printList(node1);
    cout<<result<<endl;
    
    //Insertion at the end
    Node* node2 = insertAtEnd(head,2000);
    result = printList(node2);
    cout<<result<<endl;
    
    //Insertion after a node
    Node* node3 = insertAfterNode(head,3000,2);
    result = printList(node3);
    cout<<result;
    return 0;
}