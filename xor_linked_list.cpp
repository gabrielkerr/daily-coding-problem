/*
 * An XOR linked list is a more memory efficient doubly linked list. Instead of
 * each node holding next and prev fields, it holds a field named both, which
 * is an XOR of the next node and the previous node.
 *
 * Implement an XOR linked list; it has an add(element) which adds the element
 * to the end, and a get(index) which returns the node at index.
 */

#include <iostream>
#include <string>

using namespace std;

class node
{

    int data;
    node* both;

    public:
    node(int data)
    {
        this->data = data;
        this->both = NULL;
    }

    int get_data()
    {
        return this->data;
    }

    void add(int element)
    {
        // Get current node and previous node
        node *curr = this;
        node *prev = NULL;

        node *next = (node*)((uintptr_t)prev ^ (uintptr_t)curr->both);
        cout << "Next is " << next << endl;

        // If next != null, move to next
        while (next != NULL)
        {
            prev = curr;
            curr = next;

            // XOR current with current->both to get next
            next = (node*)((uintptr_t)prev ^ (uintptr_t)curr->both);

            cout << "Next is " << next << endl;
        }

        // If next = null then add node to the end
        cout << "next is null!" << endl;

        node n(element);
        node *np = &n;

        // current->both = prev^&new_n
        curr->both = (node*)((uintptr_t)prev ^ (uintptr_t)np);

        // new_n->both = curr^null
        np->both = (node*)((uintptr_t)curr ^ (uintptr_t)NULL);


        cout << "prev is " << prev << endl;
        cout << "curr is " << curr << endl;
    }

    node *get(int index);
};

int main()
{
    node n(1);
    cout << "Hey there! " << n.get_data() << endl;
    n.add(2);
    cout << endl;
    n.add(3);
    return 0;
}


