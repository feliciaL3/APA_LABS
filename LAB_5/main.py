import sys
from random import randint
from matplotlib import pyplot as plot
from time import time


# Dijkstra algorithm for the shortest path from the source
def Dijkstra_algorithm(vertices, edges, source):
    # Function to get the next vertex to be visited
    def to_be_visited():
        v = -10
        for index in range(num_of_vertices):         # Loop through all vertices
            # Check if the vertex has not been visited and its distance is less than or equal to the current minimum
            if (visited_and_distance[index][0] == 0) and (
                    v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
                v = index
        return v
    num_of_vertices = len(vertices[0])
    visited_and_distance = list()  # Create a list to keep track of visited vertices and their distances from the source
    for i in range(num_of_vertices):
        if i != source:  # Initialize all vertices with infinite distance except the source vertex
            visited_and_distance.append([0, sys.maxsize])
        else:
            visited_and_distance.append([0, 0])
    for vertex in range(num_of_vertices):    # Loop through all vertices
        to_visit = to_be_visited()         # Get the next vertex to be visited
        for neighbor_index in range(num_of_vertices):         # Loop through all neighbors of the current vertex
            # Check if the vertex is a neighbor and has not been visited
            if (vertices[to_visit][neighbor_index] == 1) and (visited_and_distance[neighbor_index][0] == 0):
                # Calculate the new distance from the source
                new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
                # Update the distance of the neighbor if the new distance is smaller
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance
            visited_and_distance[to_visit][0] = 1             # Mark the current vertex as visited
    return visited_and_distance


# Floyd-Warshall algorithm for the shortest path between all the vertices
def Floyd_Warshall_algorithm(vertices, edges):
    num_of_vertices = len(vertices[0])
    distance = edges
    # iterate over all vertices to find the shortest path between every pair of vertices
    for k in range(num_of_vertices):
        for i in range(num_of_vertices):
            for j in range(num_of_vertices):
                # check if there is a shorter path by going through the intermediate vertex k
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

# coefficients for defining the number of edges in a graph
# thus declaring it as dense or sparse
dense_coefficient = 80
sparse_coefficient = 30


# function for creating a dense/sparse graph of a given size
def generateGraph(size, coef):
    v = list()  # create an empty list to hold the vertices of the graph
    e = list()  # create an empty list to hold the edges of the graph
    for x in range(size):     # loop through the vertices and create a list of edges for each vertex
        v.append(list())         # create a list to hold the edges for the current vertex
        for y in range(size):  # loop through the other vertices to determine whether there is an edge between them
            if x == y:  # if the two vertices are the same, set the edge weight to 0
                v[x].append(0)
            else:
                choice = randint(0, 100)  # generate a random number between 0 and 100
                if choice <= coef:  # if the random number is less than or equal to the coef parameter, set the edge weight to 1
                    v[x].append(1)
                else:                 # otherwise, set the edge weight to 0
                    v[x].append(0)

    for x in range(size):  # loop through the vertices and create a list of edge weights for each vertex
        e.append(list())  # create a list to hold the edge weights for the current vertex
        for y in range(size):  # loop through the other vertices to determine the edge weights
            if v[x][y] != 0:  # if there is an edge between the two vertices, set the edge weight to a random number between 10 and 100
                e[x].append(randint(10, 100))
            else:  # otherwise, set the edge weight to 0
                e[x].append(0)
    return v, e


def current_time_millis():
    return time() * 1000


def normalizeVerticesSet(n_vertices, vertices, edges):
    for x in range(n_vertices - 1):
        for y in range(n_vertices - 1):
            if (vertices[x][y] == 0) and (x != y):
                edges[x][y] = sys.maxsize


# testing the algorithms
input_sizes = [10, 50, 100, 200, 300]
dijkstra_dense, dijkstra_sparse = list(), list()
floyd_dense, floyd_sparse = list(), list()
start_time, end_time = 0, 0

# testing on dense graphs
for index in range(len(input_sizes)):
    vertices, edges = generateGraph(input_sizes[index], dense_coefficient)     # generate dense graph
    # time Dijkstra's algorithm
    start_time = current_time_millis()
    for k in range(0, input_sizes[index]):
        Dijkstra_algorithm(vertices, edges, k)
    end_time = current_time_millis()
    # record time taken and normalize edges
    dijkstra_dense.append(round(end_time - start_time, 3))
    normalizeVerticesSet(len(vertices[0]), vertices, edges)

    # time Floyd-Warshall algorithm
    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    floyd_dense.append(round(end_time - start_time, 3))    # record time taken

# testing on sparse graphs
for index in range(len(input_sizes)):
    vertices, edges = generateGraph(input_sizes[index], sparse_coefficient)

    start_time = current_time_millis()
    for k in range(0, input_sizes[index]):
        Dijkstra_algorithm(vertices, edges, k)
    end_time = current_time_millis()
    dijkstra_sparse.append(round(end_time - start_time, 3))
    normalizeVerticesSet(len(vertices[0]), vertices, edges)
    # time Floyd-Warshall algorithm
    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    floyd_sparse.append(round(end_time - start_time, 3))

# Dijkstra and Floyd-Warshall separately
plot.figure()
plot.plot(input_sizes, dijkstra_dense, color="skyblue", label="Dense graph")
plot.plot(input_sizes, dijkstra_sparse, color="blue", label="Sparse graph")
plot.title("Dijkstra Algorithm", color="black", fontsize=16)
plot.legend(loc='upper left')
plot.xlabel(" Size ", color="black", fontsize=14)
plot.ylabel("Time (millis)", color="black", fontsize=14)
plot.grid()
plot.show()

plot.figure()
plot.plot(input_sizes, floyd_dense, color="skyblue", label="Dense graph")
plot.plot(input_sizes, floyd_sparse, color="blue", label="Sparse graph")
plot.title("Floyd-Warshall Algorithm", color="black", fontsize=16)
plot.legend(loc='upper left')
plot.xlabel(" Size ", color="black", fontsize=14)
plot.ylabel("Time (millis)", color="black", fontsize=14)
plot.grid()
plot.show()

# comparative analysis of Dijkstra and Floyd-Warshall algorithms
plot.figure()
plot.plot(input_sizes, dijkstra_dense, color="skyblue", label="Dijkstra")
plot.plot(input_sizes, floyd_dense, color="blue", label="Floyd-Warshall")
plot.title("Dense graphs", color="black", fontsize=16)
plot.legend(loc='upper left')
plot.xlabel(" Size ", color="black", fontsize=14)
plot.ylabel("Time (millis)", color="black", fontsize=14)
plot.grid()
plot.show()

plot.figure()
plot.plot(input_sizes, dijkstra_sparse, color="skyblue", label="Dijkstra")
plot.plot(input_sizes, floyd_sparse, color="blue", label="Floyd-Warshall")
plot.title("Sparse graphs", color="black", fontsize=16)
plot.legend(loc='upper left')
plot.xlabel(" Size ", color="black", fontsize=14)
plot.ylabel("Time (millis)", color="black", fontsize=14)
plot.grid()
plot.show()


# print time record for Dijkstra on dense graphs
print("Dijkstra's algorithm on dense graphs:")
for index in range(len(input_sizes)):
    print(f"Graph size: {input_sizes[index]}")
    print(f"Time taken: {dijkstra_dense[index]} ms")
    print()

# print time record for Dijkstra on sparse graphs
print("Dijkstra's algorithm on sparse graphs:")
for index in range(len(input_sizes)):
    print(f"Graph size: {input_sizes[index]}")
    print(f"Time taken: {dijkstra_sparse[index]} ms")
    print()

# print time record for Floyd-Warshall on dense graphs
print("Floyd-Warshall algorithm on dense graphs:")
for index in range(len(input_sizes)):
    print(f"Graph size: {input_sizes[index]}")
    print(f"Time taken: {floyd_dense[index]} ms")
    print()

# print time record for Floyd-Warshall on sparse graphs
print("Floyd-Warshall algorithm on sparse graphs:")
for index in range(len(input_sizes)):
    print(f"Graph size: {input_sizes[index]}")
    print(f"Time taken: {floyd_sparse[index]} ms")
    print()
