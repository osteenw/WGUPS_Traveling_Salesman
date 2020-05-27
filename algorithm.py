# Created by Will Osteen
# Student ID 001099825

# Algorithm to sort a list of packages by order of their nearest neighbor.
# Nearest neighbor is determined by the edge-weight between package addresses.
# Runtime is O(n^2)
def sort(list, graph, hash_table, veh_num="Unknown"):
    # Function to load package object into list from a list of index's
    # Runtime is O(n)
    package_list = hash_list(list, hash_table, veh_num)

    # Sorts first location against the hub
    # Runtime is O(n)
    edge_list = []
    new_order = []
    closest_neighbor = 0
    for package in package_list:
        edge_weight = float(graph.edge_weights[(graph.get_vertex(0), graph.get_vertex(package.address_id))])
        edge_list.append(edge_weight)
        edge_list.sort()
        if edge_weight == edge_list[0]:
            closest_neighbor = package.id
    new_order.append(closest_neighbor)

    # Sorts every other location against the previous item in the sorted list
    # Runtime is O(n^2)
    while len(new_order) < len(package_list):
        last_package = hash_table.get(closest_neighbor)
        edge_list = []
        closest_neighbor = new_order[len(new_order) - 1]

        # Runtime is O(n^2logn)
        # Adds the distance for each package address from the previous package address to a list.
        # The list is then sorted for closest distance first. If the current package has the closest address it is
        # now the closest neighbor and is next to be added to the new sort list.
        for package in package_list:
            # Looks up edge weight. Runtime is O(1)
            edge_weight = float(
                graph.edge_weights[
                    (graph.get_vertex(last_package.address_id), graph.get_vertex(package.address_id))])
            edge_list.append(edge_weight)
            # Runtime is O(nlogn)
            edge_list.sort()

            # Conditional to prevent duplicate package id's in the new order
            if edge_weight == edge_list[0] and (package.id in new_order):
                edge_list.pop(0)

            # Conditional in case the list is empty from the previous conditional, and to make sure only new
            # package ids are added
            if edge_list != [] and edge_weight == edge_list[0] and (package.id not in new_order):
                closest_neighbor = package.id

        new_order.append(closest_neighbor)

    return hash_list(new_order, hash_table, veh_num)


# Function to load package object into list from a list of index's
# Runtime is O(n)
def hash_list(list, hash_table, veh_num="Unknown"):
    package_list = []
    for package in list:
        hashed_package = hash_table.get(package)
        try:
            hashed_package.status = "On Truck {num}".format(num=veh_num)
        except AttributeError:
            print(f"Attribute error for package {package}")
        package_list.append(hashed_package)
    return package_list
