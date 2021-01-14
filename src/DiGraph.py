from GraphInterface import GraphInterface
from NodeData import node_data





class DiGraph(GraphInterface):
    """
      This Class represents a directional weighted graph , and implements the GraphAlgoInterface interface
      Every graph includes nodes and edges between nodes.
      Every edge is directed - which means that there is only way from the source to the destnation of the edge

      @Author Shlomo Glick
    """


    def __init__(self):
        """** ** ** ** *Constructor ** ** ** ** ** *"""

        self.nodes = {}  # #{key0:  node0 , key1: node1........}
        self.node_size = 0
        self.edge_size = 0
        self.mc = 0
        self.upside_neighbors = {}  # {key {key : weight,,,,},,,,,,}   curret <-
        self.neighbors = {}  # {key {key : weight,,,,},,,,,,}   curret ->

    def v_size(self) -> int:
        """
        This method returns the number of vertices (nodes) in the graph.
        return: the number of nodes in the graph
        """
        return self.node_size

    def e_size(self) -> int:
        """
        This method returns the number of edges (assume directional graph).
        :return: the number of the edges in the graph
        """
        return self.edge_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
            (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        :param id1:
        :return:  a dictionary of all the nodes connected to (into) node_id ,
                each node is represented using a pair (other_node_id, weight)
        """
        if not id1 in self.nodes: return {}
        return self.upside_neighbors[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        :param id1:
        :return: a dictionary of all the nodes connected from node_id ,
                each node is represented using a pair
                (other_node_id, weight)
        """
        if not id1 in self.nodes: return {}
        return self.neighbors[id1]

    def get_mc(self) -> int:
        """
        This method returns the Mode Count - for testing changes in the graph.
        :return:  the mode count of the graph
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        :param id1: -  the source of the edge.
        :param id2: - the destination of the edge.
        :param weight:  - positive weight representing the cost (aka time, price, etc) between src-->dest.
        :return: True, if the operation was successful and False if the operation failed
        """
        if weight < 0: return False
        if not (id1 in self.nodes) or not (id2 in self.nodes): return False
        if id1 == id2: return False
        if id2 in self.neighbors[id1]: return False
        self.edge_size += 1
        self.upside_neighbors[id2][id1] = weight
        self.neighbors[id1][id2] = weight
        self.mc += 1
        return True

    def get_node(self, node_id: int) -> node_data:
        """
         This method returns the node_data by the node_id,
        :param node_id:
        :return: the node_data by the node_id, None if none.
        """

        return self.nodes[node_id]

    def add_node(self, node_id: int, pos: tuple = (0, 0, 0)) -> bool:
        """
        :param node_id: - is the new node for the graph
        :param pos:
        :return:True, if the operation was successful and False if the operation failed
        """
        if node_id in self.nodes: return False
        node = node_data(node_id, pos)
        self.nodes[node_id] = node
        self.neighbors[node_id] = {}
        self.upside_neighbors[node_id] = {}
        self.node_size += 1
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        This method deletes the edge from the graph,
        :param node_id1:
        :param node_id2:
        :return:True, if the operation was successful and False if the operation failed
        """
        if not node_id1 in self.neighbors: return False
        if not node_id2 in self.neighbors[node_id1]: return False
        del self.neighbors[node_id1][node_id2]
        del self.upside_neighbors[node_id2][node_id1]
        self.edge_size -= 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
         Deletes the node (with the given ID) from the graph -
        and removes all edges which starts or ends at this node.
        :param node_id:
        :return:True, if the operation was successful and False if the operation failed
        """
        if not node_id in self.nodes: return False
        del self.nodes[node_id]
        for i in self.neighbors[node_id]:
            del self.upside_neighbors[i][node_id]
        for i in self.upside_neighbors[node_id]:
            del self.neighbors[i][node_id]
        num_nei = len(self.neighbors[node_id])
        self.edge_size -= num_nei
        del self.neighbors[node_id]
        self.node_size -= 1
        self.mc += 1
        return True

    def __str__(self) -> str:
        return f"Edges: {self.neighbors} , Nodes:+{self.nodes}"

    def __repr__(self) -> str:
        return f"Edges: {self.neighbors} , Nodes:+{self.nodes}"

    def __eq__(self, other) -> bool:


        """
        Equals method for testing the graph
        :param other:  - another graph for comparing
        :return: true if and only if two of the graphs have the same vertices and edges
        """

        if type(other) !=DiGraph: return False
        if self.edge_size != other.edge_size: return False
        if self.node_size != other.node_size: return False
        nodes1 = self.nodes
        nodes2 = other.nodes
        for i in nodes1:
            if nodes1[i] != nodes2[i]: return False
        if self.neighbors != other.neighbors:
            return False
        return True




















