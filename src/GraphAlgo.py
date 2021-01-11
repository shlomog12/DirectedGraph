import json
import queue
from math import inf
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from node_data import node_data
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, my_graph: DiGraph =None):
        self.graph_algo = my_graph

    def get_graph(self) -> GraphInterface:
        return self.graph_algo

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                self.graph_algo = self.dict_to_graph(json.load(file))
                return True

        except IOError as e:
            print(e)

        return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.as_dict(), indent=4, fp=file)
                return True
        except IOError as e:
            print(e)

        return False


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        null = (float(inf), [])
        graph = self.get_graph()
        if graph == None: return null
        if  not id1  in graph.nodes or  not id2  in graph.nodes: return null
        fathers = self.init_tag(id1)
        dis=graph.nodes[id2][1].get_tag()
        if dis == -1: return null
        path = self.get_path(id1, id2, fathers,[])
        graph.nodes[id2][1].reset_tag()
        path.reverse()
        ans =(dis , path)
        return ans

    def connected_component(self, id1: int) -> list:
        ans=[]
        graph=self.get_graph()
        if graph==None: return ans
        if not id1 in graph.nodes: return ans
        self.init_tag(id1)
        for i in graph.nodes.values():
            node=i[1]
            if node.get_tag()!= -1:
                ans.append(node.get_key())
        revers_my_graph=self.revers_graph(graph)
        self.__init__(revers_my_graph)
        self.init_tag(id1)
        del_from_ans=[]
        for i in ans:
            node=revers_my_graph.nodes[i][1]
            if  node.get_tag()==-1:
                del_from_ans.append(i)
        for i in del_from_ans:
            ans.remove(i)
        node_data(0).reset_tag()
        self.__init__(graph)
        return ans

    def connected_components(self) -> List[list]:
        ans=[]
        if self.graph_algo == None: return ans
        for node_id in self.get_graph().nodes:
            flag=False
            for group in ans:
                if node_id in group:
                    flag=True
                    break
            if not flag:
                ans.append(self.connected_component(node_id))

        return ans

    def plot_graph(self) -> None:
        rnd=random
        graph=self.get_graph()
        list_x=[]
        list_y=[]
        for i in graph.nodes:
            node=graph.get_node(i)
            key=node.get_key()
            pos=node.get_location()
            if pos==(0,0,0):
                rnd.seed(key)
                # x = rnd.random() * 1000
                # y = rnd.random() * 1000
                b=key
                x=np.sin(b)* 400
                y=np.cos(b)* 400
                d=key*3
                if x<0:
                    x+=d
                else:
                    x-=d
                if y<0:
                    y+=d
                else:
                    y-=d


                x+=500
                y+=500


                pos= (x,y,0)
                node.set_location(pos)
            else:
                x=pos[0]
                y=pos[1]
            plt.text(x, y+25, f"{key}",color="r")
            list_x.append(x)
            list_y.append(y)



        for key_current,edges in self.get_graph().neighbors.items():
            node_current=graph.get_node(key_current)
            pos_current=node_current.get_location()
            for i in edges:
                nei=graph.get_node(i)
                pos_nei=nei.get_location()
                dis_x=pos_nei[0]-pos_current[0]
                dis_y=pos_nei[1]-pos_current[1]

                plt.arrow(pos_current[0], pos_current[1], dis_x, dis_y,color="gray",length_includes_head=True, head_width=10, head_length=15,width=0.05,fc='k',ec='k' )

        #
        #
        #
        #
        #
        #
        #     # for edge in self.get_graph().neighbors[key_current
        #         print(edge)
        #
        # print(list_x)
        # print(list_y)

        # plt.arrow(200,200,350,350 ,length_includes_head=True , head_width=20, head_length=80)
        plt.plot(list_x, list_y, 'yo')
        plt.axis([0, 1000, 0, 1000])
        plt.show()
        plt.show()
        pass










    def get_path(self, src: int, dest: int, fathers: {}, path: []):
        path.append(dest)
        if (dest == src):
            return path
        else:
            return self.get_path(src, fathers[dest], fathers, path)

    def init_tag(self,  src: int = -1):
        my_priority_queue= queue.PriorityQueue()
        fathers = {src: -1}
        node_src = self.get_graph().nodes[src][1]
        node_src.set_tag(0)
        my_priority_queue.put(node_src)
        while len(my_priority_queue.queue) !=0:
            node_current = my_priority_queue.get()
            key_current = node_current.get_key()
            tag_current = node_current.get_tag()
            for edge in self.get_graph().neighbors[key_current].values():
                distance = tag_current + edge[1]
                key_dest = edge[0]
                node_dest = self.get_graph().nodes[key_dest][1]
                tag_dest = node_dest.get_tag()
                if tag_dest > distance or tag_dest == -1:
                    node_dest.set_tag(distance)
                    fathers[key_dest] = key_current
                    my_priority_queue.put(node_dest)

        return fathers

    def as_dict(self):
        Edges = []
        nei = self.graph_algo.neighbors
        for node_id in nei:
            for edge_tup in nei[node_id]:
                src = node_id
                w = nei[node_id][edge_tup][1]
                dest = nei[node_id][edge_tup][0]

                edge_dic = {"src": src, "w": w, "dest": dest}
                Edges.append(edge_dic)
        Nodes = []
        nodes2 = self.graph_algo.nodes
        for i in nodes2:
            n_tup = nodes2[i]
            node = n_tup[1]
            node_id = node.key
            pos = f"{node.pos[0]},{node.pos[1]},{node.pos[2]}"
            n_dict = {"pos": pos, "id": node_id}
            Nodes.append(n_dict)
        return {"Edges": Edges, "Nodes": Nodes}

    def dict_to_graph(self, dict_graph) -> DiGraph:

        graph = DiGraph()
        Edges = dict_graph["Edges"]
        Nodes = dict_graph["Nodes"]

        for node in Nodes:
            str_pos = node["pos"]
            pos_tup = tuple(map(int, str_pos.split(',')))
            graph.add_node(node["id"], pos_tup)

        for edge in Edges:
            graph.add_edge(edge["src"], edge["dest"], edge["w"])

        return graph

    def revers_graph(self, graph:DiGraph)-> DiGraph:
        ans=DiGraph()
        for i in graph.nodes:
            ans.add_node(i)



        edges=graph.upside_neighbors
        for node_current,neighbors in edges.items():
            for edge in neighbors.values():
                ans.add_edge(node_current,edge[0],edge[1])



        return ans









