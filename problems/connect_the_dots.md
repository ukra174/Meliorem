
<metadata>

{   
    "created":"26/12/2024",
    "categories":["Optimization","2D"]
}

</metadata>
<setup>
import random, math
random.seed(127001)
class Dots:
    def __init__(self,n=100):
        self.dots = [(random.random(),random.random()) for i in range(n)]
        self.connections=[]
    def get_dots(self):
        return(self.dots)
    def connect(self,id1,id2):
        self.connections.append([id1,id2])
    def length(self):
        return(sum([((self.dots[id1][0]-self.dots[id2][0])**2+(self.dots[id1][1]-self.dots[id2][1])**2)**0.5 for id1,id2 in self.connections]))   
    def recursion(self,id,connections,visited):
        if(visited[id]):
            return(0)
        visited[id]=True
        return(1+sum([self.recursion(connection,connections,visited) for connection in connections[id]]))
    def isComplete(self):
        connections = self.getGraph()
        visited = [False]*len(self.dots)
        dots_connected = self.recursion(0,connections,visited)
        print(f"{dots_connected} dots connected!")
        return(dots_connected==len(self.dots))
    def getGraph(self):
        connections={}
        for dot in range(len(self.dots)):
            connections[dot]=[]
        for ids in self.connections:
            connections[ids[0]].append(ids[1])
            connections[ids[1]].append(ids[0])
        return(connections)
    def reset(self):
        self.connections=[]

quest = Dots()
print=display
</setup>

# Connect the dots
Let's say you have a bunch of dots in 2d space. And you need to connect them, so that total length of connaction is as short as possible.

# 

#### Here's how you interact with the quest:


```python
dots = quest.dots
print(dots)
quest.connect(0,1) # connects 1'st and 2'nd dot

total = quest.length()
print(total) # prints sum of lengths of all connections

connections = quest.getGraph()
print(connections) # prints the connections graph

quest.reset() # removes all connections

```

For this test dots are placed randomly across (0,0) (1,1) square, but there is a 'follow up' quest with [Connect the dots II]()! Check it out if you like this one!

# 


#### Let the quest begin!

# 




<check>
if(quest.isComplete()):
    display(f"Score: {1000/quest.length():.2f}")
else:
    display("You didn't collect all the dots!")
</check>