import os
import unittest
import time
from GraphAlgo import GraphAlgo
import networkx as nx
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTestCase(unittest.TestCase):



    def net_load_from_json(self, file_name: str) -> nx.DiGraph:
        try:
            with open(file_name, 'r') as file:
                dict_graph = json.load(file)
            file.closed
        except IOError as e:
            print(e)
        graph = nx.DiGraph()
        Edges = dict_graph["Edges"]
        Nodes = dict_graph["Nodes"]
        for node in Nodes:
            graph.add_node(node["id"])
        for edge in Edges:
            src = edge["src"]
            dest = edge["dest"]
            graph.add_edge(src, dest)
            graph.edges[src, dest]["weight"] = edge["w"]
        return graph

    def run_time_shortest_path(self, algo: GraphAlgo, list_i: list) -> None:
        print("shortest_path:")
        start = time.time()
        short1 = algo.shortest_path(list_i[0], list_i[1])
        length_time1 = time.time() - start
        print(f"time_short1 ={length_time1}")
        short2 = algo.shortest_path(list_i[2], list_i[3])
        length_time2 = time.time() - length_time1 - start
        print(f"time_short2 ={length_time2}")
        short3 = algo.shortest_path(list_i[4], list_i[5])
        length_time3 = time.time() - length_time2 - start - length_time1
        print(f"time_short3 ={length_time3}")
        print(f"time_all_short={time.time() - start}")

    def run_time_connected_component(self, algo: GraphAlgo, list_i) -> None:
        print("component:")
        start = time.time()
        algo.connected_component(list_i[0])
        length_time1 = time.time() - start
        print(f"time_component1 ={length_time1}")
        algo.connected_component(list_i[1])
        length_time2 = time.time() - length_time1 - start
        print(f"time_component2 ={length_time2}")
        algo.connected_component(list_i[3])
        length_time3 = time.time() - length_time2 - start - length_time1
        print(f"time_component3 ={length_time3}")
        print(f"time_all_component={time.time() - start}")

    def run_time_connected_components(self, algo: GraphAlgo) -> None:
        print("components:")
        start = time.time()
        components = algo.connected_components()
        length_time = time.time() - start
        print(f"time_components ={length_time}")

    def run_time_results(self, file_name: str, i: int, list_i: list):
        algo = GraphAlgo()
        algo.load_from_json(ROOT_DIR + file_name)
        print(f"************time for graph{i}*****************")
        self.run_time_shortest_path(algo, list_i)
        self.run_time_connected_component(algo, list_i)
        self.run_time_connected_components(algo)

    def loading_data(self):
        file0 = "/B1/G_10_80_0.json"
        file1 = "/B1/G_100_800_0.json"
        file2 = "/B1/G_1000_8000_0.json"
        file3 = "/B1/G_10000_80000_0.json"
        file4 = "/B1/G_20000_160000_0.json"
        file5 = "/B1/G_30000_240000_0.json"
        list0 = [0, 9, 2, 5, 1, 8]
        list1 = list(map(lambda x: 10 * x, list0))
        list2 = list(map(lambda x: 100 * x, list0))
        list3 = list(map(lambda x: 1000 * x, list0))
        list4 = list(map(lambda x: 2000 * x, list0))
        list5 = list(map(lambda x: 3000 * x, list0))

        ans = {0: (file0, list0), 1: (file1, list1), 2: (file2, list2), 3: (file3, list3), 4: (file4, list4),
               5: (file5, list5)}

        return ans

    def run_time_graph_from_json(self):
        for i, tup in self.loading_data().items():
            self.run_time_results(tup[0], i, tup[1])

    def net_run_time_shortest_path(self, graph: nx.DiGraph, list_i: list) -> None:
        print("shortest_path:")
        start = time.time()
        short1 = nx.shortest_path(graph, source=list_i[0], target=list_i[1], weight='weight')
        length_time1 = time.time() - start
        print(f"time_short1 ={length_time1}")
        short2 = nx.shortest_path(graph, source=list_i[2], target=list_i[3], weight='weight')
        length_time2 = time.time() - length_time1 - start
        print(f"time_short2 ={length_time2}")
        short3 = nx.shortest_path(graph, source=list_i[4], target=list_i[5], weight='weight')
        length_time3 = time.time() - length_time2 - start - length_time1
        print(f"time_short3 ={length_time3}")
        print(f"time_all_short={time.time() - start}")

    def net_run_time_connected_components(self, graph: nx.DiGraph):
        print("components:")
        start = time.time()
        components = nx.strongly_connected_components(graph)
        length_time = time.time() - start
        print(f"time_components ={length_time}")

    def run_time_results_net(self, file_name: str, i: int, list_i: list):
        graph = self.net_load_from_json(ROOT_DIR + file_name)
        print(f"************time for graph{i}*****************")
        self.net_run_time_shortest_path(graph, list_i)
        self.net_run_time_connected_components(graph)

    def run_time_graph_from_json_net(self):
        for i, tup in self.loading_data().items():
            self.run_time_results_net(tup[0], i, tup[1])

    def test_run_time_my_algoritem(self):
        print("*********************************************************my**********************************")
        start_all = time.time()
        self.run_time_graph_from_json()
        print(f"Total time of all the algorithms on all the graphs: {time.time() - start_all}")

    def test_run_time_NetworkX(self):
        print("*********************************************************forNetWorkx**********************************")
        start_all_net = time.time()
        self.run_time_graph_from_json_net()
        print(f"NETWORKX - Total time of all the algorithms on all the graphs: {time.time() - start_all_net}")
        # print("cc")
        # x=json.load(ROOT_DIR+"/B1/G_10_80_0.json")
        # print(x)

    def test_checking_correctness(self):

        for tup in self.loading_data().values():
            graph = self.net_load_from_json(ROOT_DIR + tup[0])
            list_i=tup[1]
            nx_short1 = nx.shortest_path(graph, source=list_i[0], target=list_i[1], weight='weight')
            nx_short2 = nx.shortest_path(graph, source=list_i[2], target=list_i[3], weight='weight')
            nx_short3 = nx.shortest_path(graph, source=list_i[4], target=list_i[5], weight='weight')
            nx_components=[]
            for obj in nx.strongly_connected_components(graph):
                nx_list=[]
                for j in obj:
                    nx_list.append(j)
                nx_components.append(nx_list)
                         # ******my******

            algo = GraphAlgo()
            algo.load_from_json(ROOT_DIR + tup[0])
            my_short1 = algo.shortest_path(list_i[0], list_i[1])[1]
            my_short2 = algo.shortest_path(list_i[2], list_i[3])[1]
            my_short3 = algo.shortest_path(list_i[4], list_i[5])[1]
            my_components = algo.connected_components()

                            # *****eq*****
            self.assertEqual(my_short1,nx_short1)
            self.assertEqual(my_short2, nx_short2)
            self.assertEqual(my_short3, nx_short3)
            self.assertEqual(sorted(my_components), sorted(nx_components))



















    # if __name__ == '__main__':
    #     # test_plt_load()
    #     test_run_time_my_algoritem()
    #     test_run_time_NetworkX()
