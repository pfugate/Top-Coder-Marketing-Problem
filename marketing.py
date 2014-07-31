##Top Coder Marketing Problem - http://community.topcoder.com/stat?c=problem_statement&pm=1524&rd=4472

#Load examples as array of strings
exone = ["1 4","2","3","0",""]
extwo = ["1","2","0"]
exthree = ["1","2","3","0","0 5","1"]
exfour = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
exfive = ["1","2","3","0","5","6","4"]

class Marketing:
  
  #A method that takes the array of strings and builds an adjacency list.
  #The list is stored in a class varaible.
  #  Paramaters : Array of Strings
  #  Returns :    Nothing
  #  Complexity : Worse Case - O(n + m)
  def preprocess(self,example):
    # Setup the class varaibles needed in each method
    self.n = len(example)
    self.color = [-1]*self.n
    self.visited = [-1]*self.n
    self.adj = [-1]*self.n
    
    # Loop through each node to create the adjacency list
    i = 0;
    while(i < self.n):
      # Initilize the adj array with arrays at each position
      if self.adj[i] == -1:
        self.adj[i] = []
      # Create a temp array to hold the edges belonging to a node
      temp = []
      edges = example[i].split(" ")
      for edge in edges:
        if edge != "":
          temp.append(int(edge))
          # Since the graph is undirected we must also add the edge to the oposite node
          if self.adj[int(edge)] == -1:
            self.adj[int(edge)] = [i]
          elif i not in self.adj[int(edge)]:
            self.adj[int(edge)].append(i)
      self.adj[i].extend(temp)
      i+=1
      
  #The method required by the problem, it loops through each node and if that node is not visited it calls the Depth First Search
  #  Paramaters : Array of Strings
  #  Returns :    int
  #  Complexity : Worst Case - O(n^2*m) - Due to the call of DFS
  def howMany(self, example):
    # Call preprosses to set up the adjacency list
    self.preprocess(example)
    i = 0
    # graph_componet_count is the count of how many components are in the graph
    graph_componet_count = 0
    while(i < self.n):
      if self.visited[i] == -1:
        graph_componet_count += 1
        # Call the Depth First Search, if the search returns false a graph could not be colored
        if not self.dfs(i, 0):
          return -1
      i += 1
    # We must take 2 to the graph componet count to get the possible solutions. If one solution is
    # possiable, so is it's inverse
    return 2**graph_componet_count
  
  #The depth first search recursive method - Note recurison has a high memory overhead for large datasets
  #iterative implamentation would work better for large sets. The DFS colors each node if it has not been visited.
  #If the node has been visted then it checks to see if the node is colored corretly
  #  Paramaters : int: position in the adjacency list, int: current color
  #  Returns :    bool
  #  Complexity : Worst Case - O(n*m)
  def dfs(self, i, c):
    self.color[i] = c
    self.visited[i] = 1
    j = 0
    while j < self.n:
      if j in self.adj[i]:
        # If vertex j has already been visted and is the wrong color the graph can't be completed so we return false
        if self.visited[j] != -1 and self.color[j] == c: 
          return False
        # If the recursive call returns false at anytime, the parent recursive function must also return false
        if self.visited[j] == -1 and not self.dfs(j, 1-c):
          return False
      j+=1
    return True

mark = Marketing()
print "Example One: %i" % mark.howMany(exone)
print "Example Two: %i" % mark.howMany(extwo)
print "Example Three: %i" % mark.howMany(exthree)
print "Example Four: %i" % mark.howMany(exfour)
print "Example Five: %i" % mark.howMany(exfive)