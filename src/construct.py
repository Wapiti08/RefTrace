import networkx as nx
from tqdm import tqdm

class constructer:

    def __init__(self):
        pass

    def web_req_graph(self, req_url_list: list, ref_url_list:list):
        ''' build the web request graph based on requested url and referer values
        referer value points at previous accessed url 
        '''
        edge_list = []
        # in order to do the refactoring for graph
        ord_list = []
        i = 0
        # every loop corresponds to one complete http request (one line of dataset)
        for ref_url, req_url in tqdm(zip(ref_url_list, req_url_list), desc="traversing refer values in http requests"):
            if ref_url is not None:
                edge_list.append((ref_url, req_url))
                ord_list.append(i)
            i += 1

        G = nx.DiGraph()
        G.add_edges_from(edge_list)

        return G, ord_list