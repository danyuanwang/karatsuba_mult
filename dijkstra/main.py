from dmatrix import DMatrix
import sys
#integrates one node from the unexzplored into the explored
def integrate_node(graph, explored, distances):
    #loop all edges that cross from x to unexplored
    shortest_dist = sys.maxsize
    new_node = None
    for head in explored:
        for tail in graph.gettails(head).keys():
            if tail not in explored:
                length = graph.edge(head, tail)
                print('head', head)
                distance_h = distances[head - 1]
                distance = distance_h + length
                print(distance)
                if distance < shortest_dist:
                    shortest_dist = distance
                    new_node = tail
                    print('new', new_node)
    return shortest_dist, new_node

        #evaulate according to djikstra greedy score
#main loop loop on all the nodes
def dijkstra(graph, source):
    #initialize
    # the X containing every vertex we have computed shortest path distance from source to 
    explored = [source]
    # the A in which entry contains the correct shortest path from source to the vertex(index of the entry)
    distances = [sys.maxsize] * graph.size()
    print(len(distances))
    distances[source - 1] = 0
    while len(explored) != graph.size():
        new_dist, new_node = integrate_node(graph, explored, distances)
        distances[new_node - 1] = new_dist
        print(new_node)
        explored.append(new_node)
    return distances

selected = [7,37,59,82,99,115,133,165,188,197]
graph = DMatrix()
#graph.printout()
shortestPath = dijkstra(graph, 1)
for v in selected:
    print(shortestPath[v- 1])
