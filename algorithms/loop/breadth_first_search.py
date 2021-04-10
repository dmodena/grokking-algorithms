from collections import deque

def search(graph, initial_node, searched_item):
    '''
    Performs Breadth-First Search.

    Returns the searched item if found.
    '''
    search_queue = deque()
    search_queue += graph[initial_node]
    verified = []

    while search_queue:
        curr_node = search_queue.popleft()
        if not curr_node in verified:
            if searched_item(curr_node):
                return curr_node
            else:
                search_queue += graph[curr_node]
                verified.append(curr_node)
    return None
