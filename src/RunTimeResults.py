import time

from GraphAlgo import GraphAlgo


def run_time_shortest_path(algo: GraphAlgo, list_i: list) -> None:
    print("shortest_path:")
    start = time.time()
    short1 = algo.shortest_path(list_i[0], list_i[1])
    length_time1 = time.time() - start
    print(f"time_short1 ={length_time1}")
    short2 = algo.shortest_path(list_i[2], list_i[3])
    length_time2 = time.time() - length_time1-start
    print(f"time_short2 ={length_time2}")
    short3 = algo.shortest_path(list_i[4], list_i[5])
    length_time3 = time.time() - length_time2 - start -length_time1
    print(f"time_short3 ={length_time3}")
    print(f"time_all_short={time.time() - start}")


def run_time_connected_component(algo: GraphAlgo,list_i) -> None:
    print("component:")
    start = time.time()
    short1 = algo.connected_component(list_i[0])
    length_time1 = time.time() - start
    print(f"time_component1 ={length_time1}")
    short2 = algo.connected_component(list_i[1])
    length_time2 = time.time() - length_time1 - start
    print(f"time_component2 ={length_time2}")
    short3 = algo.connected_component(list_i[3])
    length_time3 = time.time() - length_time2 - start - length_time1
    print(f"time_component3 ={length_time3}")
    print(f"time_all_component={time.time() - start}")


def run_time_connected_components(algo: GraphAlgo) -> None:
    print("components:")
    start = time.time()
    short1 = algo.connected_components()
    length_time = time.time() - start
    print(f"time_components ={length_time}")



def run_time_results(file_name: str, i: int, list_i: list):
    algo = GraphAlgo()
    algo.load_from_json(file_name)
    print(f"************time for graph{i}*****************")
    run_time_shortest_path(algo, list_i)
    run_time_connected_component(algo,list_i)
    run_time_connected_components(algo)


def run_time_graph_from_json():
    file0 = "../B1/G_10_80_0.json"
    file1 = "../B1/G_100_800_0.json"
    file2 = "../B1/G_1000_8000_0.json"
    file3 = "../B1/G_10000_80000_0.json"
    file4 = "../B1/G_20000_160000_0.json"
    file5 = "../B1/G_30000_240000_0.json"
    list0 = [0, 9, 2, 5, 1, 8]
    list1 = list(map(lambda x: 10 * x, list0))
    list2 = list(map(lambda x: 100 * x, list0))
    list3 = list(map(lambda x: 1000 * x, list0))
    list4 = list(map(lambda x: 2000 * x, list0))
    list5 = list(map(lambda x: 3000 * x, list0))
    run_time_results(file0, 0, list0)
    run_time_results(file1, 1, list1)
    run_time_results(file2, 2, list2)
    run_time_results(file3, 3, list3)
    run_time_results(file4, 4, list4)
    run_time_results(file5, 5, list5)









if __name__ == '__main__':
    start_all=time.time()
    run_time_graph_from_json()
    print(f"Total time of all the algorithms on all the graphs: {time.time()-start_all}")
