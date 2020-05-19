from graph import Vertex, Graph
from hash_table import HashTable
from package import Package
import csv


# Creates hash table
hash_table = HashTable()

package_list = []

# Initializes package data into the hash table
with open('package_list.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Create package
        package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], 'At Hub', row[7])
        # Add the package to the hash table
        hash_table.set(package)
        package_list.append(package)

# Test to find all packages
for i in range(1, len(package_list) + 1):
    print(hash_table.get(i).id)

# Assign each location to a Vertex

# Assigns each vertex to a graph