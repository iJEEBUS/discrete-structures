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
################ Use below for testing ################
# This should return ["A", "B", "D", "C"]
test_tree = {
				"A" : ["B","C"], 
				"B" : ["D"], 
				"C" : ["E","F"], 
				"D" : [],
				"E" : ["G"],
				"F" : ["H"],
				"G" : [],
				"H" : ["I"],
				"I" : []
			}

print DFS(test_tree)



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
    ################ Use for testing ################

# This should return ["A", "B", "D", "C"]
test_one = {
				"A" : ["B","C"], 
				"B" : ["D"], 
				"C" : ["E","F"], 
				"D" : [],
				"E" : ["G"],
				"F" : ["H"],
				"G" : [],
				"H" : ["I"],
				"I" : []
			}

test_two = {
				"A" : ["B","C"], 
				"B" : ["D"], 
				"C" : [], 
				"D" : []
			}

test_three = {
				"A" : ["B","C", "D"], 
				"B" : [], 
				"C" : [], 
				"D" : []
			}

print '\ntest_one: %s\n' % (BFS(test_one))
print 'test_two: %s\n' % (BFS(test_two))
print 'test_three: %s\n' % (BFS(test_three))
