from import_data import import_package_data, import_address_data
from algorithm import sort, hash_list, print_status


# Converts time from hours and minutes to minutes
# This is used for determining package location. Time must be after 0800
class Clock:
    def __init__(self, hour, min, end_hour, end_min):
        self.hour = hour
        self.min = min
        self.end_hour = end_hour
        self.end_min = end_min
        self.delivery1_finished = False

    def add_min(self, min):
        assert isinstance(self.min, int)
        assert isinstance(self.hour, int)
        self.min += min
        while self.min > 59:
            self.hour += 1
            self.min -= 60

    def get_time(self):
        return f"{self.hour:02d}:{self.min:02d}"

    def get_end_time(self):
        return f"{self.end_hour:02d}:{self.end_min:02d}"


def delivery(graph, hash_table, package_list, list1, list2, list3, hour, min):
    time = Clock(8, 0, hour, min)
    total_distance = 0

    if time.end_hour > 7:
        list1 = sort(list1, graph, hash_table, 1)
        total_distance += delivery_algo(graph, time, list1)

    if (time.hour > 8 and time.min > 5) \
            and (time.hour < time.end_hour or ((time.hour == time.end_hour) and (time.min < time.end_min))):
        list2 = sort(list2, graph, hash_table, 2)
        total_distance += delivery_algo(graph, time, list2)

    # When truck driver 1 finishes, he takes truck 3
    # Delivery time must be after 10:20 to get package change
    if time.delivery1_finished == True:
        if time.hour > 11 or (time.hour > 10 and time.min > 20) \
                and (time.hour < time.end_hour or ((time.hour == time.end_hour) and (time.min < time.end_min))):
            list3 = sort(list3, graph, hash_table, 3)
            total_distance += delivery_algo(graph, time, list3)

    print(f"Total distance traveled: {int(total_distance)} miles")
    print_status(package_list, time.get_end_time())


def delivery_algo(graph, time, list1):
    current_location = 0
    previous_location = 0
    distance_traveled = 0.0

    # Determines distance traveled along route
    # Runtime is O(n)
    for package in list1:
        # If time passed since 0800 is less than requested time, package delivery continues
        if time.hour < time.end_hour or ((time.hour == time.end_hour) and (time.min < time.end_min)):
            previous_location = current_location
            current_location = package.address_id

            # Determines distance driven from previous location
            edge_weight = float(
                graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(current_location))])

            # Updates total time and distance traveled
            time.add_min(int((edge_weight / 18) * 60))

            # If time is less than requested time then the package status is updated
            if time.hour < time.end_hour or ((time.hour == time.end_hour) and (time.min < time.end_min)):
                delivery_time = time.get_time()
                package.status = f"Delivered at {delivery_time}"
                distance_traveled += edge_weight

    # Calculates distance from last package location and the hub
    # Runtime is O(1)
    edge_weight = float(
        graph.edge_weights[(graph.get_vertex(previous_location), graph.get_vertex(0))])

    # Updates total time and distance traveled
    time.add_min(int((edge_weight / 18) * 60))

    # If time is less than requested time then the package status is updated
    if time.hour < time.end_hour or ((time.hour == time.end_hour) and (time.min < time.end_min)):
        delivery_time = time.get_time()
        package.status = f"Delivered at {delivery_time}"
        distance_traveled += edge_weight

    time.delivery1_finished = True
    return distance_traveled