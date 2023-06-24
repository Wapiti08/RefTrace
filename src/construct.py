import networkx as nx
from tqdm import tqdm

class constructer:

    def __init__(self):
        pass

    def _web_req_graph(self, req_url_list: list, ref_url_list:list):
        ''' build the web request graph based on requested url and referer values
        referer value points at previous accessed url 
        :params req_url_list: the extracted list of requested urls
        :params ref_url_list: there is nan inside list --- ""
        '''
        # in order to do the refactoring for graph
        G = nx.DiGraph()
        # every loop corresponds to one complete http request (one line of dataset)
        for ref_url, req_url in tqdm(zip(ref_url_list, req_url_list), desc="traversing refer values in http requests"):
            if ref_url != "":
                G.add_edge(ref_url, req_url)
            else:
                G.add_node(req_url)

        return G