#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.num_of_values = 0
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) where n is number of items"""
        # Collect all keys in each bucket
        list_of_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                list_of_keys.append(key)
        return list_of_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) where n is number of items"""
        list_of_values = []
        # Loop through all buckets
        for bucket in self.buckets:
        # Collect all values in each bucket
            for key, value in bucket.items():
                list_of_values.append(value)
        return list_of_values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) where n is number of items
        because we always need to loop through all n nodes to get each item."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(1) because it is simply fetching a variable"""
        # total_key_values = 0
        # # Loop through all buckets
        # for bucket in self.buckets:
        # # Count number of key-value entries in each bucket
        #     for key_value in bucket.items():
        #         total_key_values += 1
        # return total_key_values
        return self.num_of_values

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: BEST O(1) if first object / WORST O(n) if last obj / doesn't exist"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        # Check if key-value entry exists in bucket
        key_value_node = bucket.find(lambda item: item[0] == key)
        if key_value_node is None:
            return False
        else:
            return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        RUNTIME: BEST O(1) if first object / WORST O(n) if last obj / doesn't exist"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_node = bucket.find(lambda item: item[0] == key)
        # Check if key-value entry exists in bucket
        if key_value_node is None:
            # If not found, raise error to tell user get failed
            raise KeyError('Key not found: {}'.format(key))
        else:
            # return value associated with given key
            return key_value_node[1]


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) if first node, O(n) if last node or doesn't exist"""

        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_node = bucket.find(lambda item: item[0] == key)
        # Check if key-value entry exists in bucket
        # If found, delete old value
        if key_value_node is not None:
            bucket.delete(key_value_node)
            bucket.append((key, value))
        else:
            # doesn't exist yet, insert given key-value entry into bucket
            bucket.append((key, value))
            self.num_of_values += 1



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) if first node, O(n) if last node or doesn't exist"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_node = bucket.find(lambda item: item[0] == key)
        # Check if key-value entry exists in bucket
        if key_value_node is None:
        # If not found, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))
        else:
            # Otherwise, delete entry associated with given key
            bucket.delete(key_value_node)
            self.num_of_values -= 1


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
