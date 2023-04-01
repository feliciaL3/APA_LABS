import networkx as nx
import matplotlib.pyplot as plt
import time

# color for text output
WARNING = '\033[93m'
Blue = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'
graph = {'D': ['B', 'E'],
         'B': ['A', 'C'],
         'E': ['F'],
         'F': [],
         'A': [],
         'C': []}
graph2 = {'D': ['B', 'E'],
          'B': ['A', 'C'],
          'E': ['F'],
          'F': [],
          'A': ['S', 'T'],
          'S': ['N'],
          'T': [],
          'N': [],
          'C': []}


# depth-first search (recursive)
def dfs(visited, graph, node):
    # if the node has not been visited yet
    if node not in visited:
        # mark it as visited and print its value
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            # recursively call dfs on the neighbor
            dfs(visited, graph, neighbour)
queue = []


# breadth-first search
def bfs(graph, node):
    # create a list to keep track of visited nodes
    visited = [node]
    queue.append(node)
    # while the queue is not empty
    while queue:
        # remove the first element from the queue
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                # mark it as visited and add it to the queue
                visited.append(neighbour)
                queue.append(neighbour)


# define the starting node
root1 = 'D'
root2 = 'D'
visited1 = set()
visited2 = set()

if __name__ == '__main__':
    # define the trees to be tested
    trees = [
        ("balanced", graph, visited1, root1),
        ("unbalanced", graph2, visited2, root2)
    ]
    times = {}
    for tree in trees:
        name, g, visited, r = tree
        print(BOLD + Blue + f"For the {name} graph:" + END)
        for method in ["Depth-First Search", "Breadth-First Search"]:
            start = time.perf_counter()
            if method == "Breadth-First Search":
                bfs(g, str(r))
            else:
                dfs(visited, g, str(r))
            end = time.perf_counter()
            total = end - start
            times.setdefault(name, {})[method] = total
            print(f"\nExecution time for {method}: {WARNING}{total:.6f} sec{END}\n")

            # assign total value to corresponding variable
            if name == "balanced" and method == "Depth-First Search":
                total1 = total
            elif name == "balanced" and method == "Breadth-First Search":
                total2 = total
            elif name == "unbalanced" and method == "Depth-First Search":
                total3 = total
            else:
                total4 = total

    # print total execution times
    print(f"\nTotal execution time for balanced graph with DFS: {total1:.6f} sec")
    print(f"Total execution time for balanced graph with BFS: {total2:.6f} sec")
    print(f"Total execution time for unbalanced graph with DFS: {total3:.6f} sec")
    print(f"Total execution time for unbalanced graph with BFS: {total4:.6f} sec")


    def create_graph(graph, root, title):
        G = nx.Graph()
        for node in graph:
            G.add_edges_from([(node, child) for child in graph[node]])
        plt.title(title)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_nodes(G, pos,
                               nodelist=G.nodes(),
                               node_color=['pink' if node != str(root) else 'tab:orange' for node in G.nodes()],
                               node_size=550)
        plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='Root', markerfacecolor='tab:orange', markersize=10),
                            plt.Line2D([0], [0], marker='o', color='w', label='Node', markerfacecolor='pink', markersize=10)])
        plt.show()
    create_graph(graph, root1, 'Balanced Tree')
    create_graph(graph2, root2, 'Unbalanced Tree')

    # graph (3)
    x = ['BFS_B', 'DFS_B']
    x1 = ['BFS_U', 'DFS_U']
    b = [total1, total2]
    u = [total3, total4]

    plt.bar(x, b, color=['Blue', 'Blue'])
    plt.bar(x1, u, color=['Orange', 'Orange'])
    plt.xlabel('Method')
    plt.ylabel('Time (s)')
    plt.title('Time Comparator')
    plt.legend(['Balanced tree', 'Unbalanced tree'])
    plt.show()
