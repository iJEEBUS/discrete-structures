"""""""""""""""""""""""""""""""""""""""""""""
Depth-First Search
"""""""""""""""""""""""""""""""""""""""""""""
def DFS(tree):

    root = "A"
    visited, stack = [] , [root]

    while stack: # While the stack contains items do this
    	vertex = stack.pop()
    	if vertex not in visited:
    		visited.append(vertex)
    		stack.extend(tree[vertex][::-1])
    return visited

"""""""""""""""""""""""""""""""""""""""""""""
Breadth-First Search
"""""""""""""""""""""""""""""""""""""""""""""
def BFS(tree):

    root = "A"
    visited, stack, neighbors = [] , [root], []

    while stack: # While the stack exists
    	vertex = stack.pop() # Take the vertex out of the stack
    	if vertex not in visited: # Check if the vertex has been visited
    		visited.append(vertex) # Add vertex to visited list
    		neighbors.extend(tree[vertex][:])
    		if len(stack) == 0:
    			stack.extend(neighbors[::-1])
    return visited

"""""""""""""""""""""""""""""""""""""""""""""
List permutation
"""""""""""""""""""""""""""""""""""""""""""""
def list_perm(user_list):
    if user_list: 
        user_list = list(user_list) # Make sure that the input is actually a list
        answer , h = [],[]
        for x in user_list: # iterate through list
            if x not in h: # if the inputted list item is not in the new list
                temp = user_list[:]
                temp.remove(x) # remove item from temp list
                for p in list_perm(temp):
                    answer.append([x]+p) # append item to answer list
            h.append(x)
        return answer # return answer list
    else:
        return [[]]

"""""""""""""""""""""""""""""""""""""""""""""
Edge get
"""""""""""""""""""""""""""""""""""""""""""""
def edge_get(graph):
    
    weights = [] # all of the weights in the graph
    smallest_weight = 0 
    
    edges = [] # Holds edges that have minimum edge weight
    final_edges = [] 
    
    # Iterate through the graph and create a list of the weights
    for vertex in graph:
        for weight in graph[vertex]:
            if weight[1] not in weights:
                weights.append(weight[1])
    
    weights = sorted(weights)  # Sort the weights
    
    # Execute until all weights are accounted for
    while weights:
        edges = []
        for vertex in graph:
            smallest_weight = weights[0]
            
            # Checks the weight to make sure it is the current  
            # minimum and checks that any permutation of that 
            # edge is in the list already.
            for weight in graph[vertex]:
                if weight[1] == smallest_weight:
                    if [vertex, weight[0]] not in edges:
                        if [weight[0], vertex] not in edges:
                            edges.append([vertex, weight[0]])
                            
        # Remove the first weight from the list after use
        weights = weights[1:]
        
        # Add edges to final output list
        for edge in edges:
            final_edges.append(edge)
                        
    return final_edges

"""""""""""""""""""""""""""""""""""""""""""""
Kruskal's Algorithm - MST
"""""""""""""""""""""""""""""""""""""""""""""
def min_kruskal(graph):    
    sorted_edges = edge_get(graph) # Get all edges in non-decreasing order
    kruskals = sorted_edges[:len(graph)-1] # Add edges to list, stop when there is only less edge than vertex
    return kruskals

"""""""""""""""""""""""""""""""""""""""""""""
Helper method for Prim's MST
Finds the smallest neighboring edge
"""""""""""""""""""""""""""""""""""""""""""""
def smallest_neighbor(graph, vertex, e):
    smallest = ["", -1]
    for node in graph[vertex]:
        if smallest[1] == -1 or smallest[1] > node[1]:
            if [vertex, node[0]] not in e and [node[0], vertex] not in e:
                smallest = node
    return smallest

"""""""""""""""""""""""""""""""""""""""""""""
Prim's Algorithm - MST
"""""""""""""""""""""""""""""""""""""""""""""
def min_prim(graph):

    # Initializing our output variables, and our
    # vertex set to start at 'A'
    e = []
    v = ["A"]

    # Iterate through all of the vertices in the graph
    while len(v) != len(graph):
        smallest_edges = []

        # Find smallest neighboring edge of each vertex
        for vertex in v:
            edge = smallest_neighbor(graph, vertex, e)
            smallest_edges.append([vertex, edge[0], edge[1]])

        # Compare smallest possible edges
        smallest = ["", "", -1]
        for edge in smallest_edges:
            if smallest[2] == -1 or smallest[2] > edge[2]:
                if [edge[0], edge[1]] not in e and [edge[1], edge[0]] not in e:
                    smallest = edge

        # Append to our edge set the next smallest
        # available option.
        e.append([smallest[0], smallest[1]])
        if smallest[0] not in v:
            v.append(smallest[0])
        else:
            v.append(smallest[1])

    return e
