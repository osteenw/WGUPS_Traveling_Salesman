from graph import Vertex, Graph
from hash_table import HashTable
from package import Package
from import_data import import_package_data, import_address_data
import csv
import operator

# Imports data
package_list, hash_table = import_package_data()
graph, address_matrix = import_address_data()

# Package loading manually
# Truck 1 - Package [13, 15, 19, 20] Do 15 first - Delivered together [1, 14, 16, 25, 29, 30, 31, 34, 37, 40] | 14 total
#            Package 15 must be delivered by 9:00
# Truck 2 - Package [3, 6, 18, 36, 38] - Special constraints... truck leaves at 9:05 need package 6 delivered by 10:30
#                    [26, 27, 28, 32, 33, 35, 39] | 12 total
# Truck 1 Reload - Load [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24] | 14 total
#                   At 1020 am Package 9 address gets an update... Truck reload must leave after 1020

# Load lists will be used to manually load trucks with packages
load_list1 = [1, 13, 14, 15, 16, 19, 20, 25, 29, 30, 31, 34, 37, 40]
load_list2 = [3, 6, 18, 26, 27, 28, 32, 33, 35, 36, 38, 39]
load_list3 = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24]

truck_1_packages = []
truck_2_packages = []

# Function to load package object into list from a list of index's
# Runtime is O(n)
for package in load_list1:
    hashed_package = hash_table.get(package)
    truck_1_packages.append(hashed_package)  # 1 is subtracted because package_list starts at index 0

print(address_matrix[0])
# for address in address_matrix:
#     print(address_matrix[address])

for package in truck_1_packages:
    i = 0
    while i < len(address_matrix):
        if package.address == address_matrix[i][2]:
            print(f"Package ID: {package.id} = {address_matrix[i][2]}")
        i += 1

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

# # Sort the vertices by the label for convenience; display shortest path for each vertex
# # from vertex_a.
# for v in sorted(graph.adjacency_list, key=operator.attrgetter("label")):
#     if v.pred_vertex is None and v is not graph.get_vertex(0):
#         print("A to %s: no path exists" % v.label)
#     else:
#         print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(graph.get_vertex(0), v), v.distance))
