

from networkx import DiGraph, draw
from matplotlib.pyplot import show

digraph = DiGraph(directed=True)

# digraph.add_node('Moscow')
# digraph.add_node('Piter')
# digraph.add_node('Khanty-Mansyisk')
# digraph.add_node('Mathgrad')

# digraph.add_edge('Moscow', 'Piter')
# digraph.add_edge('Khanty-Mansyisk', 'Mathgrad')

# draw(digraph, with_labels=True)
#Список вершин для пользователя
print('ВВОД ВЕРШИН')
nodes = []
edges = []
while 1:
    node = input('Введите вершины (для остановки напишите "."):')
    if node == '.':
        break
    nodes.append(node)
    digraph.add_node(node)
while 1:
    edge_start = input('Введите вершину, из которой будет построен путь (для остановки введите "."):')
    if edge_start == '.':
        break
    if edge_start in nodes:
        edge_finish = input('Введите вершину, в которую будет построен путь (для остановки введите "."):')
        if edge_finish == '.':
            break
    digraph.add_edge(edge_start, edge_finish)
#Отрисовка
draw(digraph, with_labels=True)
#Вывод для пользователя
result = ", ".join(nodes)
print(f"Вы ввели:{result}")

show()

