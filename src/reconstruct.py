"""
@Description : 
@Author      : Newt Tan (Wapiti08)
@Time        : 2023/06/16 11:45
@File        : reconstruct.py
@Contact     : tzrzhuoran@gmail.com
"""
import dask
import asyncio
import BeautifulSoup as bs4
import networkx as nx
import re

class reconstructer:

    def __init__(self, graph: nx.DiGraph):
        self.graph = graph

    async def redirect_status_code(self, url:str, dd: dask.dataframe):
        ''' reconstruct redirected url for missing user initial request (single graph)

        '''
        # check the response code (301, 302, 303, 307)
        redirect_resp_code = [301, 302, 303, 307]

    

    async def redirect_html(self, order_list: list, dd: dask.dataframe):
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


    async def redirect_js(self, order_list: list, dd: dask.dataframe):
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
        