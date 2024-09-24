from graph import show
from graph import delete_node
from graph import delete_edge
from graph import add_edge

vertices = [
    ('1', 0, 0),
    ('2', 2, 3),
    ('3', 4, 5),
    ('4', 2, 8),
    ('5', 7, 6),
]

arestas = [
    ('1', '2'),
    ('1', '3'),
    ('2', '4'),
    ('4', '3'),
    ('3', '5'),
]

# vertices, arestas = delete_node('1', vertices, arestas)
# vertices, arestas = delete_edge(('2', '4'), vertices, arestas)
# vertices, arestas = delete_edge(('4', '3'), vertices, arestas)
# vertices, arestas = add_edge(('2', '3'), vertices, arestas)
show(vertices, arestas)

