from typing import List, Dict
import json



class Edge:
    def __init__(self, start: 'Node', end: 'Node', cost: int | float):
        self.start = start
        self.end = end
        self.cost = cost
    def __str__(self) -> str:
        return f"{self.start} -> {self.end}"
    def json(self):
        return {
            "start": self.start.name,
            "end": self.end.name,
            "cost": self.cost
        }

class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges: List[Edge] = []
    def __str__(self) -> str:
        return f"{self.name}"
    def __repr__(self) -> str:
        retstr =  f" {self.name}\n"
        for edge in self.edges:
            retstr += f"\t{edge}\n"
        return retstr
    def json(self):
        return {
            "name": self.name,
            "edges": [edge.json() for edge in self.edges]
        }
        
class Graph:
    def __init__(self) -> None:
        self.nodes: List[Node] = []
        
    def __len__(self) -> int:
        return len(self.nodes)
    
    def addNode(self, name: str, Parent: str, weight: float) -> None:
        if(len(self) == 0):
            self.nodes.append(Node(name))
            return
        #Find the parent node
        parentNode = self.findNode(Parent)
        if parentNode is None:
            parentNode = Node(Parent)
            self.nodes.append(parentNode)
        
        #Create the new node
        newNode = Node(name)
        self.nodes.append(newNode)
        
        #Create the edge
        newEdge = Edge(parentNode, newNode, weight)
        parentNode.edges.append(newEdge)
        
        #Create the reverse edge
        reverseEdge = Edge(newNode, parentNode, 1 / weight)
        newNode.edges.append(reverseEdge)
        
    def findNode(self, name: str) -> Node | None:
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    #Use Depth First Search to find a path from start to end
    def findPath(self, start: str, end: str, path: List[Node] = []) -> List[Node] | None:
        startNode = self.findNode(start)
        endNode = self.findNode(end)
        if startNode is None or endNode is None:
            return None
        path = path + [startNode]
        if startNode == endNode:
            return path
        for edge in startNode.edges:
            if edge.end not in path:
                newpath = self.findPath(edge.end.name, end, path)
                if newpath: return newpath
        return None
    
    def json(self):
        return [node.json() for node in self.nodes]
    
    def convert(self, value: float, path: List[Node]):
        result = value
        for i in range(len(path) - 1):
            print(f"{path[i]} -> {path[i + 1]}")
            for edge in path[i].edges:
                
                if edge.end.name == path[i + 1].name:
                    result *= edge.cost
        return result
                    
    def printGraph(self) -> None:
        for node in self.nodes:
            print(f"{node.name} has {len(node.edges)} edges")
            for edge in node.edges:
                print(f"\t{edge.start.name} -> {edge.end.name} with cost {edge.cost}")

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.json(), f)
    @staticmethod
    def load(path: str) -> 'Graph':
        data: List[Dict[str, str | Dict[str, str | float]]] = []
        with open(path, 'r') as f:
            data = json.load(f)
        graph = Graph()
        for node in data:
            parentNode = node.get("name")
            for child in node.get("edges"): #type: ignore Since we know that the data is a list of dict.
                graph.addNode(child.get("end"), parentNode, child.get("cost")) #type: ignore
        return graph
                
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    a = Graph.load("units.json")
    a.printGraph()
    path = a.findPath("s", "hr")
    a.convert(1, path)
    

# List common units of measurement
# 4. Electric Current
# 5. Temperature
# 6. Amount of Substance
# 7. Luminous Intensity