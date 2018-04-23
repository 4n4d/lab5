from graf import adjGraf

def dotReader(filehandle):
    g = adjGraf()
    mydict = dict()
    id = 0
    
    # opens file and removes first and last line in file (we dont care about name etc.)
    f = filehandle.readlines()[1:-1]

    for i in range(len(f)):
        # strip away all unncessary zeroes and the ending ;
        f[i] = f[i].strip()[:-1]
        f[i] = f[i].split(" -- ")
        
        # if was not able to split
        if len(f[i]) == 1:
            raise KeyError
        
        if not (f[i][0] in mydict):
            mydict[f[i][0]] = id
            id = id + 1
        if not (f[i][1] in mydict):
            mydict[f[i][1]] = id
            id = id + 1

    # we have a dictionary for the names in the list, now we can create edges and nodes
    for i in range(id):
        g.addNode()

    # add the edges
    for i in range(len(f)):
        # add edge does not allow "a -- a", but we want to allow for
        # nodes without any neighbors, hence we just ignore "a -- a"
        if f[i][0] != f[i][1]:
            g.addEdge(mydict[f[i][0]],mydict[f[i][1]])
    
    #print f
    #print mydict
    return g
    
def main():
    print "circular: "
    g = dotReader(open("circular.dot"))
    print g
    print g.distance(0)
    print "----"

    print "line: "
    g = dotReader(open("line.dot"))
    print g
    print g.distance(0)
    print "----"

    print "lonely: "
    # lonely is a "forest" where the first node is all alone (added by a -- a)
    g = dotReader(open("lonely.dot"))
    print g
    print g.distance(0)
    print "----"

    print "complete: "
    # complete is a complete graph
    g = dotReader(open("complete.dot"))
    print g
    print g.distance(0)
    print "----"

    print "binary tree: "
    # bintree is a binary tree
    g = dotReader(open("bintree.dot"))
    print g
    print g.distance(0)
    print "----"
if __name__ == '__main__':
    main()


