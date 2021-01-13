import json
import queue
from math import inf
import random
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from NodeData import node_data
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    """
    This class represents set of algorithms on a directed weighted graph, and some important actions on graph,including:
    0. shortestPath(int src, int dest);
    1. save_to_json(file); // save graph as JSON file
    2. load_from_json(file); // load graph from aJSON file
    3. connected_component(node_id) //Returns the connected component of a node
    4.connected_components //Returns all connected components of the graph
    @author Shlomo GLick
    """

    def __init__(self, my_graph: DiGraph = None):
        if (my_graph == None):
            self.graph_algo = DiGraph()
        else:
            self.graph_algo = my_graph

    def get_graph(self) -> GraphInterface:
        """
        This method return the underlying graph of which this class works
        :return:GraphInterface
        """
        return self.graph_algo

    def load_from_json(self, file_name: str) -> bool:
        """
        This method load a graph to this graph algorithm.
        if the file was successfully loaded - the underlying graph
        of this class will be changed (to the loaded one), in case the
        graph was not loaded the original graph should remain "as is".
        :param file_name:  - file name of JSON file
        :return: True - iff the graph was successfully loaded.
        """
        try:
            with open(file_name, "r") as file:
                self.graph_algo = self.dict_to_graph(json.load(file))
                file.closed
                return True

        except IOError as e:
            print(e)

        return False

    def save_to_json(self, file_name: str) -> bool:
        """
        This method saves the graph to a given file name in Json format
        :param file_name: - the file name (may include a relative path).
        :return: True if and only if the file was successfuly saved
        """
        if self.get_graph() == None: return False
        try:
            with open(file_name, "w") as file:
                json.dump(self.as_dict(), indent=4, fp=file)
                return True
        except IOError as e:
            print(e)

        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        This method calculates and returns a list of node_data representing the shortest path Between two nodes
         and the weight of the path

        :param id1: - start node of the traversal
        :param id2: - end (target) node
        :return:tuple(weight: float ,path: list)
        """
        null = (float(inf), [])
        graph = self.get_graph()
        if graph == None: return null
        if not id1 in graph.get_all_v() or not id2 in graph.get_all_v(): return null
        fathers = self.init_tag(id1)
        dis = graph.get_all_v()[id2][1].get_tag()
        if dis == -1: return null
        path = self.get_path(id1, id2, fathers, [])
        graph.get_all_v()[id2][1].reset_tag()
        path.reverse()
        ans = (dis, path)
        return ans

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        :param id1:  : The node id
        :return: The list of nodes in the SCC
        If the graph is None or id1 is not in the graph, return an empty list []
        """
        ans = []
        graph = self.get_graph()
        if graph == None: return ans
        if not id1 in graph.get_all_v(): return ans
        self.init_tag(id1)
        for i in graph.get_all_v().values():
            node = i[1]
            if node.get_tag() != -1:
                ans.append(node.get_key())
        revers_my_graph = self.revers_graph(graph)
        self.__init__(revers_my_graph)
        self.init_tag(id1)
        del_from_ans = []
        for i in ans:
            node = revers_my_graph.get_all_v()[i][1]
            if node.get_tag() == -1:
                del_from_ans.append(i)
        for i in del_from_ans:
            ans.remove(i)
        node_data(0).reset_tag()
        self.__init__(graph)
        return ans

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        :return:The list all SCC
        If the graph is None return an empty list []
        """
        ans = []
        if self.get_graph() == None: return ans
        for node_id in self.get_graph().get_all_v():
            flag = False
            for group in ans:
                if node_id in group:
                    flag = True
                    break
            if not flag:
                ans.append(self.connected_component(node_id))

        return ans

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        Note: The display size is adjusted to the graph it displays
        :return:None
        """
        rnd = random
        graph = self.get_graph()
        if graph == None or graph.node_size == 0: return
        pos_all = {}
        list_x, list_y = [], []
        for i in graph.get_all_v():
            node = graph.get_node(i)
            key = node.get_key()
            pos = node.get_location()
            pos_all[key] = pos
            if pos == (0, 0, 0):
                rnd.seed(key)
                x = rnd.random() + np.sin(key)
                y = rnd.random() + np.cos(key)
            else:
                x = pos[0]
                y = pos[1]
            pos_all[key] = (x, y, 0)
            list_x.append(x)
            list_y.append(y)
        min_x = min(list_x)
        max_x = max(list_x)
        min_y = min(list_y)
        max_y = max(list_y)
        dx = (max_x - min_x)
        dy = (max_y - min_y)
        for i in pos_all:
            x = list_x[i]
            y = list_y[i]
            plt.text(x, y + (dy / 40), f"{i}", color="b")
        plt.plot(list_x, list_y, 'ro')
        for key in graph.get_all_v():
            pos_current = pos_all[key]
            edges = graph.all_out_edges_of_node(key)
            for i in edges:
                pos_nei = pos_all[i]
                dis_x = pos_nei[0] - pos_current[0]
                dis_y = pos_nei[1] - pos_current[1]
                plt.arrow(pos_current[0], pos_current[1], dis_x, dis_y, color="gray", length_includes_head=True,
                          head_width=dx / 80, head_length=dx / 66.666, width=dx / 10000, fc='k', ec='k')

        extension_x = dx / 20
        extension_y = dy / 20
        plt.axis([min_x - extension_x, max_x + extension_x, min_y - extension_y, max_y + extension_y])
        plt.title("my graph:")
        plt.show()

    def get_path(self, src: int, dest: int, fathers: {}, path: []) -> list:
        """
        Runs from the dest and passes each time from a vertex to his father with the help of a fathers dictionary
        and adds them to the "path" list until he reaches src
        where he stops
        :param src:
        :param dest:
        :param fathers:
        :param path:
        :return:a ptah list from dest to src
        """
        path.append(dest)
        if (dest == src):
            return path
        else:
            return self.get_path(src, fathers[dest], fathers, path)

    def init_tag(self, src: int = -1) -> dict:
        """
        Updates the tag to all vertices
        so that for each vertex the tag is equal to the lowest weight of a trajectory to the current vertex
        The algorithm:
        Let's start with the first vertex whose distance from itself is 0
        We will run on all its neighbors
        and update them the tag that will be equal to the tag of node  the  current + the weight of the side that connects them.
        We will then put all of his neighbors in the priority queue (lowest weight).
        And run until the line is over
        So in each iteration we will perform the same action on the vertex at the top of the priority queue
        when we go over its neighbors and for that only in case the tag value has not yet been updated or the new value is lower than the old one
        we will perform the tag update and re-insert queue
        In addition to the function there is also a dictionary of fathers
        where every time we update the tag
        we also add to it the vertex from which it came to the ancestral list
        :param src:
        :return: fathers: dict
        """

        my_priority_queue = queue.PriorityQueue()
        fathers = {src: -1}
        node_src = self.get_graph().get_all_v()[src][1]
        node_src.set_tag(0)
        my_priority_queue.put(node_src)
        while len(my_priority_queue.queue) != 0:
            node_current = my_priority_queue.get()
            key_current = node_current.get_key()
            tag_current = node_current.get_tag()
            for edge in self.get_graph().neighbors[key_current].values():
                distance = tag_current + edge[1]
                key_dest = edge[0]
                node_dest = self.get_graph().get_all_v()[key_dest][1]
                tag_dest = node_dest.get_tag()
                if tag_dest > distance or tag_dest == -1:
                    node_dest.set_tag(distance)
                    fathers[key_dest] = key_current
                    my_priority_queue.put(node_dest)

        return fathers

    def as_dict(self) -> dict:
        """
        :return: the dictionary that represents the graph
        """
        if self.get_graph() == None: return None
        Edges = []
        nei = self.get_graph().neighbors
        for node_id in nei:
            for edge_tup in nei[node_id]:
                src = node_id
                w = nei[node_id][edge_tup][1]
                dest = nei[node_id][edge_tup][0]
                edge_dic = {"src": src, "w": w, "dest": dest}
                Edges.append(edge_dic)
        Nodes = []
        nodes2 = self.graph_algo.get_all_v()
        for i in nodes2:
            n_tup = nodes2[i]
            node = n_tup[1]
            node_id = node.key
            pos = f"{node.pos[0]},{node.pos[1]},{node.pos[2]}"
            n_dict = {"pos": pos, "id": node_id}
            Nodes.append(n_dict)
        return {"Edges": Edges, "Nodes": Nodes}

    def dict_to_graph(self, dict_graph) -> DiGraph:
        """
        Gets a dictionary that represents the graph and converts it to a graph
        :param dict_graph:
        :return: graph DiGraph
        """
        graph = DiGraph()
        Edges = dict_graph["Edges"]
        Nodes = dict_graph["Nodes"]
        for node in Nodes:
            if "pos" in node:
                str_pos = node["pos"]
                pos_tup = tuple(map(float, str_pos.split(',')))
                graph.add_node(node["id"], pos_tup)
            else:
                graph.add_node(node["id"])
        for edge in Edges:
            graph.add_edge(edge["src"], edge["dest"], edge["w"])
        return graph

    def revers_graph(self, graph: DiGraph) -> DiGraph:
        """
        Get a graph and return the same graph only with inverted ribs
        :param graph:
        :return: Inverted graph
        """
        ans = DiGraph()
        for i in graph.get_all_v():
            ans.add_node(i)
        edges = graph.upside_neighbors
        for node_current, neighbors in edges.items():
            for edge in neighbors.values():
                ans.add_edge(node_current, edge[0], edge[1])
        return ans
