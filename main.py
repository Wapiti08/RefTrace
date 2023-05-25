"""
@Description : 
@Author      : Newt Tan (Wapiti08)
@Time        : 2023/05/25 19:35
@File        : main.py
@Contact     : tzrzhuoran@gmail.com
"""

import asyncio
import dask.dataframe as dd
import dask
import ray
import networkx as nx
import tqdm
import re
import BeautifulSoup as bs4

def web_req_graph(req_url_list: list, ref_url_list:list, undir=False):
    ''' build the web request graph based on requested url and referer values
    referer value points at previous accessed url 
    '''
    edge_list = []
    # in order to do the refactoring for graph
    ord_list = []
    i = 0
    for ref_url, req_url in tqdm(zip(ref_url_list, req_url_list), desc="traversing refer values in http requests"):
        if ref_url is not None:
            edge_list.append((ref_url, req_url))
            ord_list.append(i)
        i += 1

    G = nx.MultiDiGraph()
    G.add_edges_from(edge_list)

    return G, ord_list

def redirect_reconstruct_status_code(order_list: list, dd: dask.dataframe):
    ''' reconstruct redirected url for missing user initial request (single graph)

    '''
    # check the response code (301, 302, 303, 307)
    redirect_resp_code = [301, 302, 303, 307]

def redirect_reconstruct_html(order_list: list, dd: dask.dataframe):
    ''' apply on single graph based on html element for redirection check

    the main methodology for redirection:
        <meta http-equiv="refresh" content="5; URL=https://example.com">

    '''
    # get the html code

    # parse the html
    soup = bs4(html_code, 'html.parser')

    meta_refresh = soup.find("meta", attrs = {'http-equiv': 'refresh'})
    if meta_refresh:
        content 


def redirect_reconstruct_js(order_list: list, dd: dask.dataframe):
    ''' apply on single graph based on js element for redirection check
    
    all the potential methods for redirection in js code:
        1. window.location.href = "https://example.com";
        2. window.location.replace("https://example.com");
        3. window.location.assign("https://example.com");
        4. window.location = "https://example.com";
        5. window.location.pathname = "/new-path";
        6. window.location.hash = "#section2";
        7. window.location.search = "?param=value";

    '''
    # get the js code from response
    js_code = 

    # define multiple regexes to match redirection signal --- can extract to setting file
    redirect_regexes = [
        r'windows\.location\.href\s*=\s*"([^"]+)"'
    ]
    for redirect_regex in redirect_regexes: 
        # assume there is only one directed link for one response
        matches = re.findall(redirect_regex,  js_code)
        # extract the matched redirected url
        if matches:
            redirect_url = matches[0]
            break
        else:
            print("there is no directed link found")
    

def url_similarity_score():
    ''' calculat the similarity score of two urls

    a = y(A, B) / max(b(A),b(B))
    y(A,B) is the number if elements in common
    max(b(A), b(B)) is the maxmium of elements

    '''
    pass


def outlier_filter():
    ''' implement Local Oultier Filter(LOF) to filter out normal traffic
    
    '''
    pass

if __name__ == "__main__":
    # read data
    df = dd.read_csv("../data/referer/www.cebookss.com.csv")
    # build the pipeline
    # pipelines = 
