import operator
from import_data import import_package_data, import_address_data
from algorithm import sort, print_status

# Imports data
graph, address_matrix = import_address_data()
package_list, hash_table = import_package_data(address_matrix)

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

truck_1_packages = sort(load_list1, graph, hash_table, 1)
truck_2_packages = sort(load_list2, graph, hash_table, 2)
truck_3_packages = sort(load_list3, graph, hash_table, 3)


# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0
for package in truck_1_packages:

    i = 0
    while i < len(address_matrix):
        if package.address == address_matrix[i][2]:
            current_location = i
            edge_weight = float(
                graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])

            distance_traveled += edge_weight
            # print(f"Distance Traveled = {distance_traveled} Package ID: {package.id} = {address_matrix[i][2]} = {i}")
            previous_location = i
        i += 1

print(f"Distance traveled: {distance_traveled}")

# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0
for package in truck_2_packages:

    i = 0
    while i < len(address_matrix):
        if package.address == address_matrix[i][2]:
            current_location = i
            edge_weight = float(
                graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])

            distance_traveled += edge_weight
            # print(f"Distance Traveled = {distance_traveled} Package ID: {package.id} = {address_matrix[i][2]} = {i}")
            previous_location = i
        i += 1

print(f"Distance traveled: {distance_traveled}")

# Determines distance traveled along route
# Runtime is O(n^2)
current_location = 0
previous_location = 0
distance_traveled = 0.0
for package in truck_3_packages:

    i = 0
    while i < len(address_matrix):
        if package.address == address_matrix[i][2]:
            current_location = i
            edge_weight = float(
                graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])

            distance_traveled += edge_weight
            # print(f"Distance Traveled = {distance_traveled} Package ID: {package.id} = {address_matrix[i][2]} = {i}")
            previous_location = i
        i += 1

print(f"Distance traveled: {distance_traveled}")

print_status(package_list)

