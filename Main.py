from graph import Vertex, Graph
from hash_table import HashTable
from package import Package
import csv
import operator

# Creates hash table
hash_table = HashTable()
package_list = []
address_list = []

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
    while i < (len(address_matrix[address_index]) - 3):  # 3 is subtracted because we are skipping the first 3 columns
        graph.add_undirected_edge(vertex,  # Current vertex / Same as vertex at address_matrix[address_index]
                                  address_matrix[i][0],  # Vertex for weighted edge
                                  address_matrix[address_index][i + 3])  # Weighted Edge
        i += 1

    address_index += 1


#######
#######
#######

def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = float(current_vertex.distance) + float(edge_weight)

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = str(start_vertex.label) + path
    return path


dijkstra_shortest_path(graph, graph.get_vertex(0))

# Sort the vertices by the label for convenience; display shortest path for each vertex
# from vertex_a.
for v in sorted(graph.adjacency_list, key=operator.attrgetter("label")):
    if v.pred_vertex is None and v is not graph.get_vertex(0):
        print("A to %s: no path exists" % v.label)
    else:
        print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(graph.get_vertex(0), v), v.distance))

