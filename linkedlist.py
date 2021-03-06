#!python
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list_length = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) because we're simply fetching a variable's value"""
        return self.list_length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        # Append node after tail, if it exists
        new_node = Node(item)
        if self.is_empty(): # linkedlist is empty
            self.head = new_node
            self.tail = new_node # since linkedlist has 1 item, it is also tail
        else: # linkedlist is not empty
            assert self.tail is not None
            self.tail.next = new_node # point previous tail's 'next' to new_node
            self.tail = new_node # set tail to new_node
        self.list_length += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we're always inserting at head"""
        # Create new node to hold given item
        # Prepend node before head, if it exists
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None: # linkedlist was empty before prepend
            self.tail = new_node # since linkedlist only has 1 item, it is the tail
        self.list_length += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Running time: BEST O(1) if first object
                      WORST O(n) if last obj / doesn't exist"""
        # Loop through all nodes to find item where quality(item) is TruCheck if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data) is True:
                return node.data
            else:
                node = node.next # reassign variable to iterate through the list
        return None # item satisfying quality never found


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Running time: BEST O(1) if first object
                      WORST O(n) if last obj / doesn't exist"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # raise ValueError('Item not found: {}'.format(item))
        prev_node = None
        curr_node = self.head

        while curr_node is not None: # ll isn't empty & curr_node not out of range
            if curr_node.data == item: # curr_node is same as item
                if self.head == curr_node:
                    self.head = curr_node.next # re-assign head
                else: # 2nd node (or later) is a match
                    prev_node.next = curr_node.next
                if self.tail == curr_node:
                    self.tail = prev_node # re-assign tail
                curr_node = None # delete data inside curr_node in all situations
                self.list_length -= 1
                return
            else: # curr_node is NOT same as item
                prev_node = curr_node # keep track of previous node before moving on
                curr_node = curr_node.next # to iterate through the list

        raise ValueError('Item not found: {}'.format(item)) # never found item

    def replace(self, orig_value, new_value):
        """Replace the given item from this linked list if it exists, or raise ValueError.
        Running time: BEST O(1) if first object
                      WORST O(n) if last obj / doesn't exist"""
        # walk through ll until finding orig_value. If found, replace with new_value
        node = self.head
        while node is not None: # ll isn't empty & node not out of range
            if node.data == orig_value:
                node.data = new_value
            else: # keep looking
                node = node.next
        raise ValueError('Replacement target not found: {}'.format(orig_value))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
