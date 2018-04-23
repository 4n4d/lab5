from graf import adjGraf
import matplotlib.pyplot as plt

def main():
    #g = adjGraf.random(100,0.1)
    #print g
    #mydict =  g.distance(0)
    #totaldist =0
    
    #for key in mydict:
    #    totaldist = totaldist + mydict[key]

    #mydict = g.distance(1)

    #for key in mydict:
    #    totaldist = totaldist - mydict[key]

    #print totaldist
    mean_dist = [0 for x in range(1,10)]
    for prob in [x*0.1 for x in range(1,10)]:
        i = 0
        # for each probability (0.1-0.9)
        # we create n=100 random graphs (possibly more if not complete)
        # creating a random graph of n=100 nodes is O(n)~O(n^2), hence the operation
        # of creating 100 random graphs is between O(n^2) and O(n^3)
        # on each random graph we do distance O(n+e) n times, O(n(n+e))~O(n^2)
        # doing this n times is O(n^2(n+e)) <- more than O(n^3), thus
        # the complexity should be O(n^2(n+e))
        
        # for each random graph, we call distance for each node
        
        #print prob
        #print mean_dist
        
        while i < 100:
            # all graphs need to be connected
            # if it is not connected (one key is "None"), let i = i - 1
            # if it is connected, add mean distance
            g = adjGraf.random(100,prob)
            g_dist = g.distance(0)
            
            connected = True
            longest_dist = 0

            # check connectedness
            for key in g_dist:
                if g_dist[key]== None:
                    connected = False # redo, graph not complete
                    break
                else:
                    if longest_dist < g_dist[key]:
                        longest_dist = g_dist[key]

            if connected:
                i = i + 1
                # if we have found a complete graph we need to find the
                # diameter of the graph. I interpret this as
                # the longest shortest distnace. but for this we need to
                # look at all the nodes (?) hence we loop through the remaining
                # 99 nodes to see if we need to update the distance
                for x in range(1,100):
                    g_dist = g.distance(x)
                    for key in g_dist:
                        if longest_dist < g_dist[key]:
                            longest_dist = g_dist[key]
                
                # add the longest dist to the list, will be divided by 100 later to find mean
                mean_dist[int(prob*10)-1] = mean_dist[int(prob*10)-1]+longest_dist
                
    #print table to std out
    print " prob. | mean dist "
    print "-------------------"
    for i in range(9):
        print "   {:03.1f} |   {:04.2f}".format((i+1)/10.0,mean_dist[i]/10.0 )
        mean_dist[i] = mean_dist[i]/100.0
        
    #print mean_dist
    plt.plot([(i+1)/10.0 for i in range(9)],mean_dist, 'bo')
    plt.xlabel("P(edge)")
    plt.ylabel("Distance(graph)")
    plt.title("Mean dist. in random graph (n=100) of varying edge prob.")
    plt.ylim(ymin = 0)
    plt.xlim(xmin = 0)
    plt.savefig("output.pdf")
    #plt.show()
    
if __name__ == '__main__':
    main()


