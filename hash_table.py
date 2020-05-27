# Will Osteen
# Student ID 001099825
# From section 7.8 of the DSA 2 zyBook on creating a hash table data structure in python.

class HashTable:

    # Constructor
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Hashing function
    def _hash(self, key):
        return hash(key) % len(self.table)

    def set(self, package):
        # Performs hash function to determine bucket place
        bucket = self._hash(package.id)
        bucket_list = self.table[bucket]

        bucket_list.append(package)

    def get(self, package_id):
        # Gets list for package ID hash location
        bucket = self._hash(package_id)
        bucket_list = self.table[bucket]

        # Returns package if found.
        for package in bucket_list:
            if package.id is package_id:
                return package

        return None
