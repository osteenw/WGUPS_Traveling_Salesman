from graph import Vertex, Graph
from hash_table import HashTable
from package import Package
import csv

# Creates hash table
hash_table = HashTable()
package_list = []
address_list = []

# Initializes package data into the hash table
# Runtime is O(n)
with open('package_list.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Create package
        column = row  # To look at columns within row
        package = Package(int(column[0]), column[1], column[2], column[3], column[4], column[5], column[6], 'At Hub',
                          column[7])
        # Add the package to the hash table
        hash_table.set(package)
        package_list.append(package)


with open('address_matrix.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 1
    for row in csv_reader:
        # Create package
        column = row  # To look at columns within row
        name = column[0]
        address = column[1]
        for j in range(1, len(package_list) + 1):
            if hash_table.get(j).address == address:
                print(f"Address ID: {i} | Package ID {hash_table.get(j).id} | {name}, {address}")
        i += 1



# Assigns each vertex to a graph
