import os
class Graph(object):
    '''This class is for the graph'''
    def __init__(self):
        '''This function initialises the instance of the object self and sets up an empty list for verticies'''   
        self.verticies = []

    def insert(self, n):
        '''This function takes a vertex and adds the value of the vertex to the end of verticies list'''
        self.verticies.append(n.value)
    
    def addEdge(self, V1, V2):
        '''This function takes two verticies and adds them to one-anothers list of other connected verticies or neighbours'''
        if V2.value not in V1.neighbours:
            V1.neighbours.append(V2.value)
            V2.neighbours.append(V1.value)
        else:
            print("These verticiess are connected by an edge already")

    def displayNodes(self):
        '''This function simply displays all of the nodes in the graph as a list'''
        print("The graph has the following nodes: ", self.verticies)

    def displayConnections(self, V1):
        '''This function takes any given vertex and calls the list of connected verticies'''
        V1.connected()

    def DFS(self, v):
        '''This function performs a depth first search starting at a given vertex'''
        stack = []
        visited = []
        vertex = v.value
        stack.append(vertex)

        while stack != []:
            placeholder = stack.pop()                                      #removes the last item from the stack because its LIFO

            if placeholder not in visited:                                 #makes sure the node hasnt already been visited
                visited.append(placeholder)                                #appends the node to list of visited

                for edges in vertice[placeholder].neighbours:             #iterates through the connected nodes
                    stack.append(edges)
                                                                            #appends all the connected nodes to the stack
        return visited

    def BFS(self, v):
        '''This function performs a depth first search starting at a given vertex'''
        Queue = []
        visited = []
        vertex = v.value
        Queue.append(vertex)
        while Queue != []:
            placeholder = Queue.pop(0)                                     #removes the first item from the Queue because its FIFO
            if placeholder not in visited:                                 #makes sure the node hasnt already been visited
                visited.append(placeholder)                                #appends the node to list of visited
                for edges in vertice[placeholder].neighbours:             #iterates through the connected nodes
                    Queue.append(edges)                             #appends all the connected nodes to the Queue
        return visited

class Vertex(object):
    '''This class is for the Vertex'''
    def __init__(self, value):
        '''This function creates an instance of the class and saves the value for the vertex.
        It also sets up an empty list to store vertices and and their connections'''
        self.value = value
        self.neighbours = []

    def connected(self):
        '''This function prints the vertex and which nodes it's connected to'''
        print(self.value, "is connected to",self.neighbours)


g = Graph()                                                         # Creates an instance of class graph called 'g'
vertice = {}                                                        #Creates a dictionary to store all vertice variable names and values
for i in range(1,11):                                               #For all 10 verticies, populate the dictionary with class instances
    vertice[i] = Vertex(i)

for i in range(1,11):                                               #For all 10 verticies, insert the nodes into the graph
    g.insert(vertice[i])

                                                                    #These are all the edge creations between two given verticies
g.addEdge(vertice[1],vertice[2])
g.addEdge(vertice[1],vertice[6])
g.addEdge(vertice[1],vertice[7])
g.addEdge(vertice[2],vertice[7])
g.addEdge(vertice[2],vertice[4])
g.addEdge(vertice[2],vertice[3])
g.addEdge(vertice[3],vertice[5])
g.addEdge(vertice[3],vertice[8])
g.addEdge(vertice[3],vertice[9])
g.addEdge(vertice[4],vertice[5])
g.addEdge(vertice[4],vertice[6])
g.addEdge(vertice[4],vertice[10])
g.addEdge(vertice[5],vertice[8])
g.addEdge(vertice[5],vertice[10])
g.addEdge(vertice[6],vertice[10])
g.addEdge(vertice[6],vertice[7])

g.displayNodes()                                                    #Display nodes

for i in range(1,11):                                               #For all 10 vertices, display connected vertices
    g.displayConnections(vertice[i])

''' Question 14 [WEEK 7] BFS and DFS Implementation  '''

searches = input("Would you like to run a Breadth First Search and a Depth First Search on your graph? y/n ")
if searches == "y":
    
    dfs = str(g.DFS(vertice[5]))                                    #Starts a DFS and BFS search starting with vertex 5
    bfs = str(g.BFS(vertice[5]))                                    
    File = open('BFS and DFS Results.txt','w+')                     #creates, names, opens, writes results then closes a file 
    File.write("The results of your Depth First Search are:"+ dfs + "\n")
    File.write("The results of your Breadth First Search are:"+ bfs + "\n")
    os.startfile('BFS and DFS Results.txt')
    File.close()

else:
    input("Press any key to end the program")
