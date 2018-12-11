from linkedlist import LinkedList

class Queue(LinkedList):

    def __init__(self, max_size, items=None):
        '''a class that will hold a fixed number of items (for performance).'''
        LinkedList.__init__(self, items=items)
        self.max_size = max_size

        if items != None:
            self.size = len(items)
        else:
            self.size = 0

    def enqueue(self, item):
        '''add item into queue.'''

        # first, check if queue is full
        if self.size == self.max_size:
            # remove item in 'FIFO' manner
            first_in = self.head.data
            self.delete(first_in)
            # keep track of list size
            self.size -= 1

        # now that there's space, add item into queue
        self.append(item)
        # keep track of list size
        self.size += 1


def test_queue():
    # credit to github.com/lvreynoso for the tests below:
    queue = Queue(max_size=5)
    print('queue: {}'.format(queue))

    print('\ntesting enqueue:')
    for item in range(20):
        print('enqueue({!r})'.format(item))
        queue.enqueue(item)
        print('queue: {}'.format(queue))
        print('size: {}'.format(queue.size))

    print('head: {}'.format(queue.head))
    print('tail: {}'.format(queue.tail))
    print('length: {}'.format(queue.length()))

    print('\ntesting queue with starting objects:')
    queue = Queue(max_size=5, items=['A','B','C'])
    print('queue: {}'.format(queue))
    print('size: {}'.format(queue.size))
    print('head: {}'.format(queue.head))
    print('tail: {}'.format(queue.tail))
    print('length: {}'.format(queue.length()))

if __name__ == '__main__':
    test_queue()
