from GraphInterface import GraphInterface
from node_data import node_data


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}  # {key0: (key0, node0) , key1: (key1,node1)........}
        self.node_size = 0
        self.edge_size = 0
        self.mc = 0
        self.upside_neighbors = {}  # {key {(key , weight),,,,},,,,,,}   curret <-
        self.neighbors = {}  # {key {(key , weight),,,,},,,,,,}   curret ->

    def v_size(self) -> int:
        return self.node_size

    def e_size(self) -> int:
        return self.edge_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        # if not id1 in self.my_graph: return None
        return self.upside_neighbors[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.neighbors[id1]

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight < 0: return False
        if not (id1 in self.nodes) or not (id2 in self.nodes): return False
        if id1 == id2: return False
        if id2 in self.neighbors[id1]: return False
        self.edge_size += 1
        self.upside_neighbors[id2][id1] = (id1, weight)
        self.neighbors[id1][id2] = (id2, weight)
        self.mc += 1
        return True

    def get_node(self, node_id: int) -> node_data:
        return self.nodes[node_id][1]

    def add_node(self, node_id: int, pos: tuple = (0, 0, 0)) -> bool:
        if node_id in self.nodes: return False
        node = node_data(node_id, pos)
        self.nodes[node_id] = (node_id, node)
        self.neighbors[node_id] = {}
        self.upside_neighbors[node_id] = {}
        self.node_size += 1
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not node_id1 in self.neighbors: return False
        if not node_id2 in self.neighbors[node_id1]: return False
        del self.neighbors[node_id1][node_id2]
        del self.upside_neighbors[node_id2][node_id1]
        self.edge_size -= 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
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
        self.mc += num_nei + 1
        return True

    def __str__(self) -> str:
        return f"Edges: {self.neighbors} , Nodes:+{self.nodes}"

    def __repr__(self) -> str:
        return f"Edges: {self.neighbors} , Nodes:+{self.nodes}"

    def __eq__(self, other) -> bool:
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














