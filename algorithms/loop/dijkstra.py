def build_initial_costs(graph, initial_node):
    '''
    Builds dictionary of initial costs.
    '''
    costs = {}
    for node in graph:
        if node == initial_node:
            costs[node] = 0
        else:
            costs[node] = float('inf')
    return costs

def get_unprocessed_lowest_cost_node(graph, costs, processed):
    '''
    Returns node based on costs and processed list.
    '''
    node = None
    lowest_cost = float('inf')
    for cost in costs:
        if costs[cost] <= lowest_cost and cost not in processed:
            node = cost
            lowest_cost = costs[cost]
    return node

def build_path(parents, end_node):
    '''
    Returns possible path from initial to end node.
    '''
    path = []
    parent = parents[end_node]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    if len(path) > 0:
        path.reverse()
        path.append(end_node)

    return path


def search(graph, initial_node, end_node):
    '''
    Returns shortest path from initial to end node based on Dijkstra's algorithm.
    '''
    costs = {}
    parents = {}
    processed = []
    path = []

    parents[initial_node] = None

    costs = build_initial_costs(graph, initial_node)

    while len(processed) < len(costs):
        node = get_unprocessed_lowest_cost_node(graph, costs, processed)
        processed.append(node)
        for neighbor in graph[node]:
            new_cost = costs[node] + graph[node][neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node

    path = build_path(parents, end_node)
    return path
