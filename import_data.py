from graph import Vertex, Graph
from hash_table import HashTable
from package import Package
import csv

def import_package_data():
    # Creates package list and hash table
    package_list = []
    hash_table = HashTable()

    # Initializes package data into the hash table
    with open('package_list.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Runtime is O(n)
        for row in csv_reader:
            # Create package
            column = row  # To look at columns within row
            package = Package(int(column[0]), column[1], column[2], column[3], column[4], column[5], column[6], 'At Hub',
                              column[7])
            # Add the package to the hash table
            hash_table.set(package)
            package_list.append(package)

    return package_list, hash_table

def import_address_data():
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

        return graph, address_matrix