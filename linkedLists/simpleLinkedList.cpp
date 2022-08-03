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

string printLinkedList(Node* temp) {
    string linkedList="";
    while (temp!=NULL) {
        linkedList += to_string(temp->data) + " ";
        temp = temp->next;
    }
    linkedList.pop_back();
    return linkedList;
}

//creating the linked list now
int main() {
    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;

    //allocating the Node object to all the above
    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 5;
    head->next = second;
    second->data = 10;
    second->next = third;
    third->data = 15;
    third->next = NULL;
    string result = printLinkedList(head);
    cout<<result;
    return 0;
}