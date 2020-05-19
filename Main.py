from graph import Vertex, Graph
from hash_table import HashTable
from package import Package

package1 = Package(1, '195 W Oakland Ave', '10:30 AM', 'Salt Lake City', 'UT', '84115', '21 KILO', 'Not Delivered')
package2 = Package(1, '24 W Oakland Ave', '10:45 AM', 'Salt Lake City', 'UT', '84115', '21 KILO', '', 'Not Delivered')

hash_table = HashTable()
hash_table.set(package1)
hash_table.set(package2)

print(hash_table.get(1))


# Assign each location to a Vertex

# Assigns each vertex to a graph