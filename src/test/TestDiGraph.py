import time
from unittest import TestCase

from DiGraph import DiGraph



class TestDiGraph(TestCase):

    def build_graph24(self) -> DiGraph:
        graph = DiGraph()
        for i in range(24):
            graph.add_node(i)

        graph.add_edge(0, 6, 3.4)
        graph.add_edge(1, 2, 12.1)

        graph.add_edge(2, 18, 180)
        graph.add_edge(3, 5, 42)
        graph.add_edge(3, 4, 55)
        graph.add_edge(3, 14, 83)
        graph.add_edge(4, 17, 82)
        graph.add_edge(5, 8, 27)
        graph.add_edge(6, 7, 5.8)
        graph.add_edge(7, 0, 7.1)
        graph.add_edge(7, 9, 10)
        graph.add_edge(8, 9, 13.1)
        graph.add_edge(8, 10, 0.01)
        graph.add_edge(8, 3, 61)
        graph.add_edge(8, 14, 2.8)
        graph.add_edge(8, 0, 9.999)
        graph.add_edge(9, 10, 4.2)
        graph.add_edge(10, 1, 12.3)
        graph.add_edge(10, 5, 29)
        graph.add_edge(10, 8, 10.5)
        graph.add_edge(11, 1, 14.5)
        graph.add_edge(11, 12, 300)
        graph.add_edge(11, 10, 2.3)
        graph.add_edge(12, 13, 6.2)
        graph.add_edge(12, 16, 74)
        graph.add_edge(13, 11, 1.3)
        graph.add_edge(13, 18, 20)
        graph.add_edge(13, 19, 99)
        graph.add_edge(14, 8, 2.7)
        graph.add_edge(14, 15, 42.5)
        graph.add_edge(15, 20, 104.55)
        graph.add_edge(16, 10, 13.6)
        graph.add_edge(17, 2, 5 / 4)
        graph.add_edge(17, 4, 73.465)
        graph.add_edge(18, 1, 33)
        graph.add_edge(18, 21, 52)
        graph.add_edge(19, 12, 102)
        graph.add_edge(20, 16, 0.001)
        graph.add_edge(20, 23, 150)

        graph.add_edge(21, 13, 64.2)
        graph.add_edge(21, 19, 15)
        graph.add_edge(21, 22, 25)
        graph.add_edge(22, 2, 77)
        graph.add_edge(23, 21, 12.5)
        return graph



    def test_v_size(self):
        graph = self.build_graph24()
        size = 24
        self.assertEqual(graph.node_size, size)
        graph.add_node(4)
        self.assertEqual(graph.node_size, size)
        graph.remove_node(30)
        self.assertEqual(graph.node_size, size)
        graph.remove_node(11)
        self.assertEqual(graph.node_size, size - 1)
        graph.add_node(30)
        self.assertEqual(graph.node_size, size)

    def test_e_size(self):
        graph = self.build_graph24()
        size = 44
        self.assertEqual(graph.edge_size, size)
        graph.add_edge(5, 8, 30)
        self.assertEqual(graph.edge_size, size)
        graph.add_edge(5, 8, 27)
        self.assertEqual(graph.edge_size, size)
        graph.remove_edge(12, 8)
        self.assertEqual(graph.edge_size, size)
        graph.add_edge(5, 1, 11)
        self.assertEqual(graph.edge_size, size + 1)
        graph.remove_edge(3, 14)
        self.assertEqual(graph.edge_size, size)
        len8 = len(graph.neighbors[8])
        graph.remove_node(8)
        self.assertEqual(graph.edge_size, size - len8)

    def test_get_all_v(self):
        graph = self.build_graph24()
        dict1 = graph.get_all_v()
        for i in range(graph.node_size):
            self.assertEqual(dict1[i], (i, graph.get_node(i)))

    def test_all_in_edges_of_node(self):
        graph = self.build_graph24()
        graph.add_node(26)
        dict_26_in = {}
        dict_8_in = {5: (5, 27), 10: (10, 10.5), 14: (14, 2.7)}
        self.assertEqual(dict_8_in, graph.all_in_edges_of_node(8))
        self.assertEqual(dict_26_in, graph.all_in_edges_of_node(26))

    def test_all_out_edges_of_node(self):
        graph = self.build_graph24()
        graph.add_node(26)
        dict_26_out = {}
        dict_8_out = {9: (9, 13.1), 10: (10, 0.01), 3: (3, 61), 14: (14, 2.8), 0: (0, 9.999)}
        self.assertEqual(dict_8_out, graph.all_out_edges_of_node(8))
        self.assertEqual(dict_26_out, graph.all_out_edges_of_node(26))

    def test_get_mc(self):
        graph = self.build_graph24()
        size = graph.node_size + graph.edge_size
        self.assertEqual(graph.get_mc(), size)
        graph.add_edge(35, 0, 1.5)
        self.assertEqual(graph.get_mc(), size)
        graph.add_edge(0, 35, 1.5)
        self.assertEqual(graph.get_mc(), size)
        graph.add_edge(0, 6, 0.5)
        self.assertEqual(graph.get_mc(), size)
        graph.add_edge(1, 6, 0.5)
        self.assertEqual(graph.get_mc(), size + 1)
        graph.remove_edge(10, 7)
        self.assertEqual(graph.get_mc(), size + 1)
        graph.remove_edge(30, 7)
        self.assertEqual(graph.get_mc(), size + 1)
        graph.remove_edge(7, 30)
        self.assertEqual(graph.get_mc(), size + 1)
        graph.remove_edge(7, 9)
        self.assertEqual(graph.get_mc(), size + 2)
        graph.add_node(1)
        self.assertEqual(graph.get_mc(), size + 2)
        graph.add_node(27)
        self.assertEqual(graph.get_mc(), size + 3)
        graph.remove_node(53)
        self.assertEqual(graph.get_mc(), size + 3)
        len8 = len(graph.neighbors[8])
        graph.remove_node(8)
        self.assertEqual(graph.get_mc(), size + 3 + 1 + len8)

    def test_add_edge(self):
        graph = self.build_graph(10)
        bool1 = graph.add_edge(0, 12, 3.5)
        self.assertFalse(12 in graph.neighbors[0])
        self.assertFalse(bool1)
        bool2 = graph.add_edge(0, 4, 3.5)
        self.assertTrue(4 in graph.neighbors[0])
        self.assertTrue(bool2)
        bool3 = graph.add_edge(0, 0, 3.5)
        self.assertFalse(0 in graph.neighbors[0])
        self.assertFalse(bool3)
        bool4 = graph.add_edge(0, 4, 2.5)
        self.assertFalse(bool4)

    def test_add_node(self):
        graph = DiGraph()
        self.assertFalse(4 in graph.get_all_v())
        boo1 = graph.add_node(4)
        self.assertTrue(4 in graph.get_all_v())
        self.assertTrue(boo1)
        boo2 = graph.add_node(4)
        self.assertFalse(boo2)

    def test_remove_edge(self):
        graph = self.build_graph()
        graph.add_edge(0, 1, 0.5)
        graph.add_edge(0, 2, 0.5)
        boo1=graph.remove_edge(2,7)
        boo2 = graph.remove_edge(7, 2)
        self.assertFalse(boo1)
        self.assertFalse(boo2)
        self.assertTrue(1 in graph.neighbors[0])
        boo3 = graph.remove_edge(0, 1)
        self.assertFalse(1 in graph.neighbors[0])
        self.assertTrue(boo3)


    def test_remove_node(self):
        graph=self.build_graph(10)
        boo1 = graph.remove_node(45)
        self.assertFalse(boo1)
        graph.add_edge(0,4,0.5)
        self.assertTrue(0 in graph.get_all_v())
        self.assertTrue(0 in graph.upside_neighbors[4])
        self.assertTrue(0 in graph.neighbors)
        boo2 =graph.remove_node(0)
        self.assertTrue(boo2)
        self.assertFalse(0 in graph.get_all_v())
        self.assertFalse(0 in graph.upside_neighbors[4])
        self.assertFalse(0 in graph.neighbors)

    def test_run_time(self):

        start=time.time()
        graph=self.build_graph(10**5,10**6)
        length_time=time.time()-start
        self.assertTrue(length_time<=10)






    def build_graph(self, size_node: int = 6, size_edge: int =0) -> DiGraph:
        graph = DiGraph()
        for i in range(size_node):
            graph.add_node(i)

        for i in range(size_node):
            j=i+1
            while graph.edge_size<size_edge and j != i:
                graph.add_edge(i,j,0)
                j+=1
                if j >= size_node: j = 0
        return graph




