def sort(list, graph, hash_table, veh_num="Unknown"):
    # Function to load package object into list from a list of index's
    # Runtime is O(n)
    package_list = hash_list(list, hash_table, veh_num)

    # Sorts first location against the hub
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
    while len(new_order) < len(package_list):
        last_package = hash_table.get(closest_neighbor)
        edge_list = []
        closest_neighbor = new_order[len(new_order) - 1]
        for package in package_list:
            if last_package.address_id != package.address_id:
                edge_weight = float(
                    graph.edge_weights[
                        (graph.get_vertex(last_package.address_id), graph.get_vertex(package.address_id))])
                edge_list.append(edge_weight)
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
        hashed_package.status = "On Truck {num}".format(num=veh_num)
        package_list.append(hashed_package)
    return package_list


def print_status(package_list):
    print("========================================================================================================")
    print("=                                      ALL PACKAGES AS OF NOW                                          =")
    print("========================================================================================================")
    for package in package_list:
        print(package.package_string())
