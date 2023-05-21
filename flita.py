import graphviz

# a = r"adjacency_matrix_13.txt"
a = r"matrix.txt"
dot = graphviz.Graph('graph', comment='A Round Graph')
with open(a, 'r') as file:
    nodes = len(file.readline().split())
for i in range(nodes):
    dot.node(str(i), str(i), fontsize='20')
with open(a, 'r') as file:
    adj = [line.split() for line in file]
for i in range(nodes):
    for j in range(nodes):
        if adj[i][j] == 'a':
            continue
        weight = int(adj[i][j])
        if weight != 0:
            dot.edge(str(i), str(j), xlabel=str(weight))
        adj[i][j] = 'a'
        adj[j][i] = 'a'
dot.render('doctest-output/round-table.gv', view=True)
