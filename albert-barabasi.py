import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math,os

class ABGraph:
    '''This class represents the Barabasi-Albert model for emulating the real networks(scale-free networks)'''

    def __init__(self, num_node):
        #initialize 5 node connected graph
        li = {}

        for i in range(num_node):
            li[i] = range(num_node)
            li[i].remove(i)

        self.nodes =  range(num_node)
        self.adj_list = li
        self.degree_nodes = [num_node-1]*5 #may be we don't need this information
        self.total_links = num_node * (num_node-1)
        self.prob = [float(num_node-1)/sum(self.degree_nodes)]*num_node
        self.tot_nodes = num_node

    def add_node(self, m):
        self.m = m
        used_node = []
        i=0
        while(i < self.m):
            target_node = np.random.choice(self.nodes , p=self.prob)
            if target_node not in used_node:
                self.adj_list[target_node].append(self.tot_nodes)
                self.degree_nodes[target_node] += 1
                used_node.append(target_node)
                self.total_links += 1
                i += 1
            else:
                i =  i

        self.adj_list[self.tot_nodes] = used_node
        #update degree probabilities
        for node in self.nodes:
            self.prob[node] = float(self.degree_nodes[node])/(sum(self.degree_nodes)+self.m)

        self.nodes.append(self.tot_nodes)                       #adding new node into the list of nodes
        self.tot_nodes += 1                                     #updating the number of nodes
        self.degree_nodes.append(self.m)                        #updating the degree for the newly added node which will be the value 'm'
        self.prob.append(float(self.m)/sum(self.degree_nodes))  #update the probability of new added node

    def showDegrees(self):
        print(self.degree_nodes)

    def showDegProb(self):
        print(self.prob)

    def showInfo(self):
        print("Num of nodes = %d"%self.tot_nodes)
        print("Num of links = %d"%self.total_links)
        # print(len(self.nodes))
        # print(len(self.degree_nodes))

    def plotDegDist(self):
    #plots degree distribution in linear and log-log scale
    	
        counter = Counter(self.degree_nodes)
        counter.most_common()
        sorted_counter = sorted(counter.items())
        k = [y[0] for y in sorted_counter]
        p_k = [float(y[1])/self.tot_nodes for y in sorted_counter]

        log_k = [math.log10(y) for y in k]
        log_p_k =[math.log10(pk) for pk in p_k]
        plt.title("Degree Distribution Plot")
        plt.scatter(k], p_k)
        plt.xlabel("Degress(k)")
        plt.ylabel("Probability(p(k))")
        plt.savefig(os.getcwd()+'/linear_plot.png')

        plt.title("Degree Distribution Plot")
        plt.scatter(log_k[:150], log_p_k[:150])
        plt.xlabel("Degress(k)")
        plt.ylabel("Probability(p(k))")
        plt.savefig(os.getcwd() +'/log-log_plot.png')
        # plt.show()


if __name__ == '__main__':
    #Part1 - with constant m = 2
    graph1 = ABGraph(5)
    graph1.showDegProb()
    graph1.showInfo()
    for i in range(2000):
        graph1.add_node(2)
    graph1.showInfo()

    #Part 2 - with m = 2 or 3
    # graph2 = ABGraph(5)
    # graph2.showDegProb()
    # graph2.showInfo()
    # m = [2, 3]
    # prob_m = [0.5, 0.5]
    # for i in range(5000):
    #     graph2.add_node(np.random.choice(m, p= prob_m))
    # graph2.showInfo()
    # graph2.plotDegDist()
