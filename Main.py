from import_data import import_package_data, import_address_data
from delivery import delivery


# Imports data
graph, address_matrix = import_address_data()
package_list, hash_table = import_package_data(address_matrix)

# Package loading manually
# Load lists will be used to manually load trucks with packages
load_list1 = [1, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
load_list2 = [3, 4, 6, 18, 22, 25, 26, 28, 32, 36, 38]
load_list3 = [2, 5, 8, 9, 10, 11, 12, 17, 21, 23, 24, 27, 33, 35]

delivery(graph, hash_table, package_list, load_list1, load_list2, load_list3, 13, 0)

