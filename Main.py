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

graph = Graph()
address_matrix = []

# Initializes a matrix for each address
# Each address is set to a Vertex on the graph
with open('address_matrix.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Create a list for each row in the file
    # Runtime is O(n^2)
    i = 0  # Iterable used for indexing the Vertex
    for row in csv_reader:
        row_data = []

        # add each column of data to the list
        row_data.append(Vertex(i))
        for column in row:
            if column != '':
                row_data.append(column)
            else:
                i += 1
                break

        # Adds the current row data to the list
        address_matrix.append(row_data)

        # Adds the current rows vertex to the graph
        graph.add_vertex(row_data[0])

# Adds edges between addresses on the graph
# Runtime is O(n^2)
address_index = 0
for vertex in graph.adjacency_list:
    i = 0

    # Iterates through each edge column for each row of the address_matrix
    while i < len(address_matrix[address_index]) - 3:  # 3 is subtracted because we are skipping the first 3 columns
        graph.add_undirected_edge(vertex,  # Current vertex / Same as vertex at address_matrix[address_index]
                                  address_matrix[i][0],  # Vertex for weighted edge
                                  address_matrix[address_index][i + 3])  # Weighted Edge
        i += 1

    address_index += 1
