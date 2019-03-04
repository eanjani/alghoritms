#graph presentation: each key is a vertex, values for particular key are his neighbour (edges)
graph = {}
graph["vertex1"] = ["vertex2","vertex3","vertex4"]
graph["vertex2"] = ["vertex3"]
graph["vertex3"] = ["vertex5"]
graph["vertex4"] = ["vertex5"]
graph["vertex5"] = []

vertexToVisit = ['vertex1'] #we're starting from entry point - vertex which has only outgoing edge 
visitedVertex = []
finalV = "vertex3"

def shortestWay(vertexToVisit, finalV):
    for v in vertexToVisit:
        print("checking", v)
        visitedVertex.append(v)
        if v  == finalV:
            return visitedVertex
        else:
            print("Adding neighbours: ",graph.get(v))
            vertexToVisit.extend(graph.get(v))
            if(finalV in graph.get(v)):
                visitedVertex.append(finalV)
                return visitedVertex



def shortestWayRecursion(vertexToVisit): #do poprawki
    steps = 0
    for v in vertexToVisit:
        if v not in visitedVertex:
            print("checking", v)
            visitedVertex.append(v)
            if v  == finalV:
                return visitedVertex
            else:
                if(graph.get(v) is not None):
                    print("Adding neighbours: ",graph.get(v))
                    shortestWayRecursion(graph.get(v))
                else:
                    return visitedVertex




v = shortestWayRecursion(vertexToVisit)
print(v)
