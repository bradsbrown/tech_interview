# --- Question 1 answer --- #
def question1(s, t):
    if len(t) > len(s):
        return False
    t_check = getChecksum(t)
    for i in range(0, len(s) - len(t) + 1):
        if getChecksum(s[i:i+len(t)]) == t_check:
            return True
    return False


def getChecksum(string):
    return sum([ord(a)*113 for a in string])


# --- Question 2 answer --- #
def question2(a):
    '''Takes in a single string, returns the longest palindromic
    slice of that string'''
    if len(a) == 1 or a == '':
        return a
    for test_length in range(len(a)+1, 1, -1):
        for start_point in range(0, len(a) - test_length + 1):
            test = a[start_point: start_point+test_length]
            if test == test[::-1]:
                return test
    return None


# --- Question 3 answer --- #
def question3(G):
    '''Inputs a graph G, returns the minimum spanning tree of the graph
    as an adjacency list'''
    nodes = G.keys()
    mst = {}
    cursor = nodes[0]
    while nodes:
        next_edge = findSmallest(G[cursor], nodes)
        nodes.pop(nodes.index(cursor))
        if next_edge:
            if cursor in mst:
                mst[cursor] += [(next_edge)]
            else:
                mst[cursor] = [(next_edge)]
            if next_edge[0] in mst:
                mst[next_edge[0]] += [(cursor, next_edge[1])]
            else:
                mst[next_edge[0]] = [(cursor, next_edge[1])]
            cursor = next_edge[0]
        else:
            if len(nodes) == 0:
                return mst
            else:
                return None


def findSmallest(list, nodes):
    smallest = float("inf")
    for key, value in list:
        if key in nodes:
            if value < smallest:
                smallest = value
                name = key
    return (name, smallest) if smallest < float("inf") else None


# --- Question 4 answer --- #
def question4(T, r, n1, n2):
    '''Inputs a binary search tree T, r as the root node, n1 and n2 as two
    nodes on the tree. Returns the least common ancestor of the two nodes.'''
    adjacencyList = {}
    nodes = [r]
    checked = []

    if r > len(T[0]) - 1 or n1 > len(T[0]) - 1 or n2 > len(T[0]) - 1:
        return None
    # build up list of nodes and connections until all found nodes are checked
    while len(nodes) > len(checked):
        for to_check in nodes:
            if to_check not in checked:
                connections = (q4_getEdges(T, to_check))
                if connections:
                    adjacencyList[to_check] = connections
                    nodes.extend(connections)
                checked.append(to_check)

    if not adjacencyList:
        return None

    # now, find the path to both numbers from the root
    try:
        n1_path = q4_getPathTo(adjacencyList, n1, r)
        n2_path = q4_getPathTo(adjacencyList, n2, r)
    except ValueError as err:
        print("Malformed tree: " + str(err))
        return

    # finally, iterate up through n1 parents until n2 shares ancestor
    for i in range(len(n1_path) - 1, -1, -1):
        if n1_path[i] in n2_path:
            return n1_path[i]


def q4_getEdges(T, nodeNum):
    '''Given a matrix representation of a tree and a node value, returns
    a list of all direct children of that node'''
    edgeList = []
    for i in range(0, len(T[nodeNum])):
        if T[nodeNum][i] == 1:
            edgeList.append(i)
    if edgeList == []:
        return None
    else:
        return edgeList


def q4_getPathTo_helper(adjacencyList, value, negpath):
    '''Helper function for q4_getPathTo, adds one move stepwise to the path'''
    for key in adjacencyList.keys():
        if value in adjacencyList[key]:
            negpath.append(key)
    return negpath


def q4_getPathTo(adjacencyList, value, root):
    '''given a completed adjacencyList, a node value, and the root value,
    returns a path from the root to the target node'''
    negpath = [value]
    while negpath[-1] != root:
        negpath = q4_getPathTo_helper(adjacencyList, value, negpath)
        value = negpath[-1]
        if len(negpath) > len(adjacencyList) + 1:
            raise ValueError("That path is not valid")
    return negpath[::-1]


# --- Question 5 class definition and answer --- #
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    '''Inputs a singly linked list with starting node ll, returns the
    data from the node that is m spaces from the end of the chain'''
    if m < 1:
        return None
    cursor = ll
    slow_cursor = None

    # advance the lead cursor to the necessary "gap"
    count = 1
    while count < m:
        if cursor.next:
            cursor = cursor.next
            count += 1
        else:
            return None

    # then set the slow cursor at the start and advance both together
    slow_cursor = ll
    while cursor.next:
        cursor = cursor.next
        slow_cursor = slow_cursor.next

    # when the lead cursor reaches the end, return slow cursor's data
    return slow_cursor.data


# Question 1 Tests
# basic test
assert question1("euripides", "side") is True
# test for t string too long
assert question1("der", "pizzaz") is False
# test for no match
assert question1("promotion", "x") is False

print question1('udddddddddda', 'uda')
print question1('udacity', 'tiy')
print question1('udacity', 'udy')


# Question 2 Tests
# basic test
assert question2("amalgamation") == "ama"
# test for full word
assert question2("racecar") == "racecar"
# test for blank string
assert question2("") == ""
# test for single letter
assert question2("a") == "a"


# Question 3 Tests
# basic test from question given
assert question3({'A': [('B', 2)],
                  'B': [('A', 2), ('C', 5)],
                  'C': [('B', 5)]}) == {'A': [('B', 2)],
                                        'C': [('B', 5)],
                                        'B': [('A', 2), ('C', 5)]}
# test for a unconnected graph
assert question3({'A': [('B', 2)],
                  'B': [('A', 2)],
                  'C': [('D', 3)],
                  'D': [('C', 3)]}) is None
# test for duplicate connection (should choose shortest path)
assert question3({'A': [('B', 1), ('C', 2), ('B', 5)],
                  'B': [('A', 1), ('C', 5)],
                  'C': [('A', 2), ('B', 5)]}) == {'A': [('B', 1)],
                                                  'B': [('A', 1), ('C', 5)],
                                                  'C': [('B', 5)]}


# Question 4 Tests
# test for given array from question
assert question4([[0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]], 3, 1, 4) == 3
# test a larger array
assert question4([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0]], 5, 2, 1) == 3
# test a malformed/misordered input
assert question4([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0]], 2, 5, 1) is None
# test a nonexistent root
assert question4([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0]], 7, 5, 1) is None


# Question 5 Tests
n5 = Node(1)
n4 = Node(2)
n4.next = n5
n3 = Node(3)
n3.next = n4
n2 = Node(4)
n2.next = n3
n1 = Node(5)
n1.next = n2

# basic test
assert question5(n1, 2) == 2
# test for m over length of chain (request before chain root)
assert question5(n1, 6) is None
# test for last entry in chain
assert question5(n1, 1) == 1
# test for m past end of chain
assert question5(n1, 0) is None
