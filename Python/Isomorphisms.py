"""""""""""""""""""""""""""""""""""""""""""""
List permutation
"""""""""""""""""""""""""""""""""""""""""""""
def list_perm(user_list):
    if user_list: # if the list exists
        user_list = list(user_list) # make sure that the input is actually a list
        answer , h = [],[]
        for x in user_list: # iterate through list
            if x not in h: # if the inputted list item is not in the new list
                temp = user_list[:]
                temp.remove(x) # remove item from temp list
                for p in list_perm(temp):
                    answer.append([x]+p) # append item to answer list
            h.append(x)
        return answer 
    else:
        return [[]]

"""""""""""""""""""""""""""""""""""""""""""""
Is same
"""""""""""""""""""""""""""""""""""""""""""""
def is_same(list1, list2):
    if list1 in list_perm(list2):
        return True
    return False


"""""""""""""""""""""""""""""""""""""""""""""
Switch vertices
"""""""""""""""""""""""""""""""""""""""""""""
def switch(graph, vert1, vert2):
    
    temp_dict = {} # Temporary dictionary to hold data   
    final_dict = {} # Final dictionary that will be returned
    
    # Loop through the keys in the inputted graph
    for key in graph.copy():
        
        # Checks if either vertex is in the values 
        if vert1 in graph[key] or vert2 in graph[key]:
            
            loops = len(graph[key]) # How many items to iterate through
            counter = 0 # Counter used for the while loop
            
            while counter < loops: # Loop through every item in the keys value
                if graph[key][counter] == vert1: # If the value is equal to the first vertex
                    graph[key][counter] = vert2 # Change the value to the second vertex
                elif graph[key][counter] == vert2: # If the value is equal to the second vertex
                    graph[key][counter] = vert1 # Change the value to the first vertex     
                counter += 1 # Increment counter by one
    
    # Loop through all of the keys in the dictionary
    for key in graph.copy():
        
        if key == vert1: # If the key is equal to the first vertex input
            new_key = vert2 # Make a new key that is to replace the original key    
            temp_dict[key] = graph[key] # Put the entire key and value into the temporary dictionary       
            final_dict[new_key] = temp_dict.pop(key) # Take the values from the temporary dictionary and place them under the new key
        
        elif key == vert2: # Uses the same logic as above
            new_key = vert1
            temp_dict[key] = graph[key]        
            final_dict[new_key] = temp_dict.pop(key)
        else:
            final_dict[key] = graph[key] # Transfer the remainder of the orginal graph to the new dictionary
        
    return final_dict
        

"""""""""""""""""""""""""""""""""""""""""""""
Is isomorphic
"""""""""""""""""""""""""""""""""""""""""""""
def is_iso(graph1, graph2):
    
    # Compare number of vertices
    if len(graph1)!= len(graph2): 
        return False
    
    # Check the degree sequences and if one is not
    # in the other then return false
    g1_degree_sequence = []
    g2_degree_sequence = []
    
    for key in graph1:
        g1_degree_sequence.append(len(graph1[key]))
    for key in graph2:
        g2_degree_sequence.append(len(graph2[key]))

        
    temp = [] # Temp list to hold permutations
    
    # Iterate through all the permutations
    for permutation in list_perm(g1_degree_sequence): 
        temp.append(permutation) # Add them to a temp array
    g1_degree_sequence[:] = [] 
    g1_degree_sequence = temp[:] # Assign entire temp list to initial list
    temp[:] = [] 
    
    # Iterate through all the permutations
    for permutation in list_perm(g2_degree_sequence): 
        temp.append(permutation) # Add them to a temp array
    g2_degree_sequence[:] = [] 
    g2_degree_sequence = temp[:] # Assign entire temp list to initial list
    temp[:] = [] 
    
    # Iterate through all permuted degree sequences
    for d_sequence in g1_degree_sequence: 
        if d_sequence in g2_degree_sequence:
            return True
        
    return False
