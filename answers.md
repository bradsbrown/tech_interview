# Question 1: Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = “udacity” and t = “ad”, then the function returns True. Your function definition should look like: “question1(s, t)”, and return a boolean True or False.

If I can assume as stated in the problem that both s and t are given as strings, the first thing it makes sense to test for is to verify that s is in fact at least as long as t, as otherwise you'll never encounter a full permutation of t within s. Then I can create a checksum hash by taking the sum of the ASCII values of the letters of t, with each letter multiplied by a large prime number (113) to prevent collisions, and roll along t-length segments of s looking for a set of letters with the same checksum. This is essentially a O(n) runtime solution, where n is the length of string s. We also get a O(1) space solution, as we only retain and only a single instance of a checksum for string t.

# Question 2: Given a string a, find the longest palindromic substring contained in a. Your function definition should look like "question2(a)", and return a string.

Assuming a is a string, I'll first check that it is at least 2 characters long, and if not simply return the string - a single character or a "" is inherently palindromic. Then, I will test each subset of the string, starting with its full length and working down to shorter slices. I compare each substring to itself run backwards, and if they match, I return the string. Worst-case efficiency is if no palindromic string is found, and would have you check every substring of every length, which simplifies to O(n^2) runtime, and O(n) space.

# 3: Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this: {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}. Vertices are represented as unique strings. The function definition should be "question3(G)"

I've taken a Prim's algorithm-style approach to the problem, starting with a random node (taking the first listed) and looking for the shorted connection to each node until all nodes have been connected to the MST. To assist in this, I wrote a helper (findSmallest) to find the shortest past to a previously unconnected node. My primary function then adds that vertex information to both nodes, and removes the node from the list of nodes to connect, working through each node until all have been added. Runtime is O(V^2), space complexity is O(V).

# Question 4: Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendants of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like "question4(T, r, n1, n2)", where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4), and the answer would be 3.

To work with this tree, my first step was to move the data from a matrix into some sort of system I could follow along more easily. I built a quick helper function to look over a row in the matrix, identify all child nodes, and return a list, then had my main function turn those lists into a dictionary of children, which made moving through the edges quite simple. Then, I built a function to return a path from the root node to each of the target nodes. With the dictionary list in play, I can walk up the list almost as easily as walking down it, so I didn't have to search the whole tree to find the ancestor from the parent. I then walked backwards up the path from n1 to find the first ancestor of n1 that was also an ancestor of n2, and return it. Runtime is O(log(V)), space is O(V).

# Question 5: Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like "question5(ll, m)", where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

For this question, as the chain only moves in one direction, the fastest solution is to use two cursors moving down the list - gapping them at a distance m-1. I can move the lead cursor forward until it is in the m-th spot on the list, then set the slow cursor at the root node and advance both at the same time until the lead cursor reaches the end of the list, then return the slow cursor's data, which will be m back from the end of the list. This gives a O(n) runtime in O(1) space.