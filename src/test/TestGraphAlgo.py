import time
from unittest import TestCase
from TestDiGraph import TestDiGraph
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo





class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        graph = TestDiGraph.build_graph(10, 20)
        algo = GraphAlgo(graph)
        graph2 = algo.get_graph()
        self.assertEqual(graph, graph2)

    def test_load_and_save_from_json(self):
        file_name = "file"
        graph24 = TestDiGraph.build_graph24(self)
        algo = GraphAlgo(graph24)
        self.assertEqual(graph24, algo.graph_algo)
        boo1 = algo.save_to_json(file_name)
        self.assertTrue(boo1)
        self.assertEqual(graph24, algo.graph_algo)
        algo.graph_algo = DiGraph()
        self.assertEqual(DiGraph(), algo.graph_algo)
        boo2 = algo.load_from_json(file_name)
        self.assertTrue(boo2)
        self.assertEqual(algo.graph_algo, graph24)

    def test_shortest_path(self):
        graph = TestDiGraph.build_graph24(self)
        algo = GraphAlgo(graph)
        ans1 = (227.8, [0, 6, 7, 9, 10, 1, 2, 18])
        self.assertEqual(ans1, algo.shortest_path(0, 18))
        ans2 = (333.75, [0, 6, 7, 9, 10, 8, 14, 15, 20, 23])
        self.assertEqual(ans2, algo.shortest_path(0, 23))
        graph.remove_edge(20, 23)
        ans3 = (float('inf'), [])
        self.assertEqual(ans3, algo.shortest_path(0, 23))
        ans4 = (0, [6])
        self.assertEqual(ans4, algo.shortest_path(6, 6))

    def test_connected_component(self):
        graph = TestDiGraph.build_graph24(self)
        algo = GraphAlgo()
        self.assertEqual([], algo.connected_component(0))
        algo.__init__(graph)
        self.assertEqual([], algo.connected_component(30))
        graph.remove_edge(20, 23)
        graph.remove_edge(20, 16)
        graph.add_edge(20, 15, 0.4)
        self.assertEqual([15, 20], algo.connected_component(15))
        self.assertEqual([15, 20], algo.connected_component(20))
        self.assertEqual([23], algo.connected_component(23))
        ans0=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22]
        self.assertEqual(ans0,algo.connected_component(0))

    def test_connected_components(self):
        graph=DiGraph()
        algo=GraphAlgo()
        self.assertEqual([],algo.connected_components())
        algo.__init__(graph)
        self.assertEqual([], algo.connected_components())
        graph=TestDiGraph.build_graph24(self)
        algo.__init__(graph)
        ans1=[]
        for i in range(24):
            ans1.append(i)
        ans=[ans1]
        self.assertEqual(ans, algo.connected_components())
        graph.remove_edge(20, 23)
        graph.remove_edge(20, 16)
        graph.add_edge(20, 15, 0.4)
        ans1.remove(15)
        ans1.remove(20)
        ans1.remove(23)
        ans=[ans1]
        ans.append([15,20])
        ans.append([23])
        self.assertEqual(ans, algo.connected_components())



    def test_plot_graph(self):
        graph=TestDiGraph.build_graph24(self)
        algo=GraphAlgo(graph)
        algo.plot_graph()
        self.assertEqual(graph,TestDiGraph.build_graph24(self))
        graph2=TestDiGraph.build_graph(self,100,300)
        algo.__init__(graph2)
        algo.plot_graph()
        self.assertEqual(graph2, TestDiGraph.build_graph(self,100,300))








    def test_run_time(self):
        start = time.time()
        graph = TestDiGraph.build_graph(10 ** 4, 10 ** 5)
        file="run_test"
        algo=GraphAlgo(graph)
        algo.save_to_json(file)
        algo.load_from_json(file)
        algo.connected_component(0)
        length_time = time.time() - start
        self.assertTrue(length_time <= 10)


















