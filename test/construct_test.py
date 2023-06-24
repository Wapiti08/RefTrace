import unittest
import sys
from pathlib import Path
sys.path.append(Path(sys.path[0]).parent.as_posix())
import networkx as nx
from src.construct import constructer
import asyncio

class TestClass(unittest.TestCase):

    def test_web_req_graph(self,):
        graph_build = constructer()
        ref_url_list = ["A", "", "C", "D", "A", ""]

        req_url_list = ["B", "B", "D", "E","F", "G"]

        G = graph_build._web_req_graph(req_url_list, ref_url_list)
        num_graph = len(list(nx.connected_components(G.to_undirected())))
        print(list(nx.connected_components(G.to_undirected())))
        expected_result = 3
        
        self.assertEqual(num_graph, expected_result)


if __name__ == "__main__":
    unittest.main()

