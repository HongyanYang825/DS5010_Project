'''
    DS 5010
    Spring 2022
    Project_Drivers_Applications_of_Graph_Theory_Topics

    Define a bunch of drivers to support the Graph class in
    graph.py

    Hongyan Yang
'''


from itertools import permutations

def check_input(eg_list, lens_list):
    '''
    Function -- check_input
    Check user inputs of edges and edge_lens for a Graph instance,
    transform inputs to correct format and raise errors when needed
    Parameters: eg_list (list)  -- a list of all edges in a graph
                lens_list (list) -- a list of ordered edge lengths      
    Return user inputs in correct format. Raise error and return None
    when inputs contains ValueError
    '''
    if len(eg_list) != len(lens_list):
        # Raise error when not every input edge has been assigned
        # one and only one edge length
        raise ValueError("Please input all edges' lengths.")
    else:
        ckd_egs, ckd_lens = [], []
        for i in range(len(eg_list)):
            # Transform input edges to uppercases
            temp_list = [each.upper() for each in eg_list[i]]
            # Transform input edges to sorted order
            sorted_eg = "".join(sorted(temp_list))
            if sorted_eg not in ckd_egs:
                ckd_egs.append(sorted_eg)
                ckd_lens.append(lens_list[i])
            elif ckd_lens[ckd_egs.index(sorted_eg)] == lens_list[i]:
                # Remove duplicated input edge length of the same edge
                continue
            else:
                # Raise error when the same edge has been assigned
                # different edge lengths
                raise ValueError(f"Conflict lens input for edge {sorted_eg}.")
    return ckd_egs, ckd_lens

def generate_subsets(vertices_set):
    '''
    Function -- generate_subsets
    Grnerate all subsets, or the power set of a given set
    Parameters: vertices_set (set) -- a set contains all vertices of a given
                                      Graph instance        
    Returns a dictionary with keys as the sizes of the subsets and with value
    as a list of all subsets of the same size
    '''
    sets_dict, order = {}, len(vertices_set)
    vert_list = list(vertices_set)  # Convert set to list for ordered elements
    # Traverse all subsets in the power set
    for i in range(2 ** order):
        # Convert the index to a binary number and format it
        to_bin = bin(i).replace("0b", "")
        bin_adj = (order - len(to_bin)) * "0" + to_bin
        # Find the corresponding subset to the binary index number
        subset = [vert_list[i] for i in range(order) if bin_adj[i] == "1"]
        key = sum([int(each) for each in bin_adj])  # Key as the size of subset
        if key in sets_dict:
            sets_dict[key].append(subset)
        else:
            sets_dict[key] = [subset]
    return sets_dict

def sort_edge(cycle_set):
    '''
    Function -- sort_edge
    Sort edges' names in the cycle_set to ascending order
    Parameters: cycle_set (set) -- a set of edges in a cycle, edges' names are
                                   unformatted
    Return a formatted set of edges in a cycle
    '''
    sorted_set, eg_list = set(), list(cycle_set)
    # Format all edges' names in the cycle_set to ascending order
    for i in range(len(cycle_set)):
        temp_list = [each.upper() for each in eg_list[i]]
        sorted_eg = "".join(sorted(temp_list))
        # Add the edge with its name sorted to output set
        sorted_set.add(sorted_eg)
    return sorted_set

def generate_cycle(vertices_list):
    '''
    Function -- generate_cycle
    Generate a set of edges with formatted names given the input vertices
    Parameters: vertices_list (list)  -- A list of vertices from a subset of
                                         vertices of the vertices_set
    Return a set of edges in a cycle, edges are formatted
    '''
    cycle_set = set()
    # Generate a list of edges in arranged order
    for i in range(len(vertices_list)):
        if i != len(vertices_list) - 1:
            cycle_set.add(vertices_list[i] + vertices_list[i + 1])
        else:
            cycle_set.add(vertices_list[0] + vertices_list[i])
    # Format edges' names in the output set of edges
    cycle_set = sort_edge(cycle_set)
    return cycle_set

def reduce_duplicate_cycle(vertices_set):
    '''
    Function -- reduce_duplicate_cycle
    Remove duplicated cycles by the nature of cycle given a set of vertices 
    Parameters: vertices_set (set) -- a set contains all vertices of a given
                                      subset of the graph's vertices_set     
    Return a list of nonduplicated cycles given its vertices
    '''
    unique_cycles = []
    # Traverse all possible cycles given its vertices
    for each in list(permutations(vertices_set)):
        # Generate a set of edges with formatted names
        cycle_set = generate_cycle(each)
        if cycle_set not in unique_cycles:
            unique_cycles.append(cycle_set) # Append only unique set of edges
    return unique_cycles

def check_cycle(eg_list, vertices_set):
    '''
    Function -- check_cycle
    Check and return all existing cycles in the given graph
    Parameters: eg_list (list)  -- a list of all edges in a graph
                vertices_set (set) -- a set contains all vertices
                                      of a given Graph instance                             
    Returns a dictionary with keys as the sizes of the cycles and
    values as a list of all existing cycles with given size
    '''
    eg_set, cycle_dict = set(eg_list), {}
    # Generate a dictionary with keys as the sizes of the subsets and
    # values as a list of all subsets of the same size
    vertices_subsets = generate_subsets(vertices_set)
    # Return an empty dictionary if there's no potential cycles 
    if len(vertices_subsets) < 4:
        return {}
    # Only check subsets with more than 3 vertices inside
    potential_subsets = {key: vertices_subsets[key]
                         for key in range(3, len(vertices_subsets))}
    # Traverse all potential cycles in the given graph
    for key in potential_subsets.keys():
        for value in potential_subsets[key]:
            # Remove duplicated cycles by the nature of cycle
            unique_cycles = reduce_duplicate_cycle(value)
            for each in unique_cycles:
                # Check if the unique set of edges exists in the graph
                if each.issubset(eg_set):
                    if key in cycle_dict:
                        cycle_dict[key].append(each)
                    else:
                        cycle_dict[key] = [each]
    return cycle_dict

def generate_path(path_tuple, sequence_tuple):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    path_of_egs, sequence_list = [], list(sequence_tuple)
    path_tuple = tuple(sorted(list(path_tuple)))
    sequence_list.insert(0, path_tuple[0])
    sequence_list.append(path_tuple[-1])
    for i in range(len(sequence_list) - 1):
        temp_list = sorted([sequence_list[i], sequence_list[i + 1]])
        path_of_egs.append("".join(temp_list))
    return path_of_egs, set(path_of_egs)

def print_path(path_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    path_route = ""
    for i in range(len(path_list) - 1):
        path_route += f"{path_list[i]} --> "
    path_route += path_list[-1]
    return path_route

def path_len(path_list, eg_list, lens_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    total_len = 0
    for each in path_list:
        total_len += lens_list[eg_list.index(each)]
    return total_len

def min_index(path_len_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    min_len = min(path_len_list)
    min_indices = [index for index in range(len(path_len_list))
                   if path_len_list[index] == min_len]
    return min_indices, min_len

def shortest_path(path_tuple, eg_list, lens_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    potential_paths, path_lens, shortest_paths = [], [], []
    path_tuple = tuple([each.upper() for each in path_tuple])
    vertices_set = to_vertices_set(eg_list)
    if not set(path_tuple).issubset(vertices_set):
        raise ValueError("Please input existing vertices.")
        return None
    else:
        seq_set = vertices_set - set(path_tuple)
        sub_seq_set = generate_subsets(seq_set)
        for key in sub_seq_set.keys():
            for value in sub_seq_set[key]:
                for each in list(permutations(value)):
                    path = generate_path(path_tuple, each)
                    if path[1].issubset(set(eg_list)):
                        potential_paths.append(path[0])
                        path_lens.append(path_len(path[0],eg_list, lens_list))
        min_indices, min_len = min_index(path_lens)
        for each in min_indices:
            shortest_paths.append(print_path(potential_paths[each]))
        return shortest_paths, min_len

def to_vertices_set(edges_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    vertices = []
    for i in range(len(edges_list)):
        vertices.extend(list(edges_list[i]))
    vertices_set = set(vertices)
    return vertices_set

def connect_indices(edge, edges_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    indices = []
    for i in range(len(edges_list)):
        if not set(edge).isdisjoint(set(edges_list[i])):
           indices.append(i)
    return indices

def append_by_index(indices_list, from_list, to_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    for index in sorted(indices_list, reverse = True):
        to_append = from_list.pop(index)
        if to_append not in to_list:
            to_list.append(to_append)
    return to_list
 
def append_by_values(value_list, from_list, to_list):
    '''
    Function -- load_window
    Draw a window at preset position with adjustable side_length
    Parameters: window (str)  -- current window to load
                start_point (tuple) -- start position
                horizontal (float) -- window's horizontal length
                vertical (float) -- window's vertical length
                width, color, speed -- default pen information        
    Draw a window at pre-determined position with specific size
    '''
    output_list = []
    for value in value_list:
        index = from_list.index(value)
        output_list.append(to_list[index])
    return output_list
