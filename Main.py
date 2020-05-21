from import_data import import_package_data, import_address_data
from algorithm import sort, hash_list, print_status

# Imports data
graph, address_matrix = import_address_data()
package_list, hash_table = import_package_data(address_matrix)

# Package loading manually
# Load lists will be used to manually load trucks with packages
load_list1 = [1, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 32, 34, 37, 39, 40]
load_list2 = [3, 4, 6, 18, 22, 25, 26, 28, 36, 38]
load_list3 = [2, 5, 8, 9, 10, 11, 12, 17, 21, 23, 24, 27, 33, 35]

truck_1_packages = sort(load_list1, graph, hash_table, 1)
truck_2_packages = sort(load_list2, graph, hash_table, 2)
truck_3_packages = sort(load_list3, graph, hash_table, 3)


total_distance = 0
# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0

for package in truck_1_packages:
    previous_location = current_location
    current_location = package.address_id
    edge_weight = float(
        graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])
    print(f"ID: {package.address_id} | Edge {edge_weight} | {address_matrix[package.address_id][1]} | {distance_traveled}")
    distance_traveled += edge_weight

# Calculates distance from last package location and the hub
edge_weight = float(
    graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(0))])
print(edge_weight)
distance_traveled += edge_weight

print(f"Distance traveled: {distance_traveled}")
total_distance += distance_traveled

# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0
for package in truck_2_packages:
    previous_location = current_location
    current_location = package.address_id
    edge_weight = float(
        graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])
    distance_traveled += edge_weight
edge_weight = float(
    graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(0))])
distance_traveled += edge_weight
print(edge_weight)
print(f"Distance traveled: {distance_traveled}")
total_distance += distance_traveled

# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0
for package in truck_3_packages:
    previous_location = current_location
    current_location = package.address_id
    edge_weight = float(
        graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])
    distance_traveled += edge_weight

print(edge_weight)
edge_weight = float(
    graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(0))])
distance_traveled += edge_weight

print(f"Distance traveled: {distance_traveled}")
total_distance += distance_traveled

print(f"Total distance traveled: {total_distance}")

# print_status(package_list)
