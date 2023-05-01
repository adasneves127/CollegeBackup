import typing
import math

def getNode(nodeCount: int, currentNode: int) -> typing.Tuple[int, int]:
    x = math.sin(2*math.pi * (currentNode/nodeCount))
    y = math.cos(2*math.pi * (currentNode/nodeCount))
    print(x, y)


getNode(10, 10)
