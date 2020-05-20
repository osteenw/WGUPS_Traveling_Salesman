class HashTable:

    # Constructor
    # Assigns all buckets with an empty list.
    # Runtime is O(1)
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Hashing function
    # Runtime is O(1)
    def _hash(self, key):
        return hash(key) % len(self.table)

    # Runtime is O(n)
    def set(self, package):
        # Performs hash function to determine bucket place
        bucket = self._hash(package.id)
        bucket_list = self.table[bucket]

        bucket_list.append(package)

    # Runtime is O(n)
    def get(self, package_id):
        # Gets list for package ID hash location
        bucket = self._hash(package_id)
        bucket_list = self.table[bucket]

        # Returns package if found.
        for package in bucket_list:
            if package.id is package_id:
                return package
