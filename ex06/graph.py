import matplotlib.pyplot as plt

def show(vertices, edges):
    for (inicio, fim) in edges:
        edge = filter(lambda x: (x[0] == inicio or x[0] == fim), vertices)
        edge = tuple(edge)

        x = tuple(map(lambda x: x[1], edge))
        y = tuple(map(lambda x: x[2], edge))

        # print(edge, x, y)

        plt.scatter(0, 0, color="white")
        plt.scatter(10, 10, color="white")
        plt.plot(x, y, 'b', marker='o')

    for (name, x, y) in vertices:
        plt.text(x, y, name, fontsize=12, ha='right', va='bottom', color='red')

    plt.show()

def delete_node(node_name, vertices, edges):
    vertices = tuple(
        filter(lambda x: x[0] != node_name, vertices)
    )

    edges = tuple(
        filter(lambda x: x[0] != node_name and x[1] != node_name, edges)
    )

    return vertices, edges

def delete_edge(target_edge, vertices, edges):
    edges = tuple(
        filter(lambda x: x != target_edge, edges)
    )

    if len(tuple(filter(lambda x: target_edge[0] in x, edges))) == 0:
        vertices, edges = delete_node(target_edge[0], vertices, edges)

    if len(tuple(filter(lambda x: target_edge[1] in x, edges))) == 0:
        vertices, edges = delete_node(target_edge[1], vertices, edges)

    return vertices, edges

def add_edge(new_edge, vertices, edges):
    if len(tuple(filter(lambda x: new_edge[0] == x[0], vertices))) == 0:
        raise ValueError("Unknown vertex: {}".format(new_edge[0]))

    if len(tuple(filter(lambda x: new_edge[1] == x[0], vertices))) == 0:
        raise ValueError("Unknown vertex: {}".format(new_edge[1]))

    edges = edges + (new_edge,)

    return vertices, edges
