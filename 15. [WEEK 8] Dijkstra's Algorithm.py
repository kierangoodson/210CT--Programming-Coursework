 def dijkstrasAlg(self, start, end):
     '''A function based on Dijkstra's 1956 algorithm for finding the
    shortest route between nodes in a graph'''
     
        node = start                        #Begin by setting starting value at 0 for the current node
        visited = []                        #Empty set for visited nodes

        for n in self.verticies:             
            vertice[n].tWeight = float('inf') #Sets n.tWeight for all other nodes to infinty

        node.tWeight = 0                      #n.tWeight becomes 0
        while node != end:                    #while node isn't the terminal (end) node
            for V in node.connectedTo:        #For the count in connected notes
                v = vertice[V]               

                if node.tWeight + self.edges[node.value,v.value] < v.tWeight:      #if node tentative weight + edges[set of vertices, node] is less than vertice tentative weight then..  
                    v.tWeight = node.tWeight + int(self.edges[v.value,node.value]) #Tentative weight of vertex V = node tWeight + edges[set of vertices and node]
                    v.pre = node

            visited.append(node)                #append the node to visited set
            minimum = float('inf')              #mimimum is infinity
            
            for n in self.verticies:            
                if vertice[n] not in visited and vertice[n].tWeight < minimum: 
                    node = vertice[n]
                    minimum = vertice[n].tWeight

        n = end
        while n != start:
            print(n.value)
            n = n.pre

        print(start.value)
