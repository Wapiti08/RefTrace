"""
@Description : 
@Author      : Newt Tan (Wapiti08)
@Time        : 2023/06/16 11:46
@File        : similarity.py
@Contact     : tzrzhuoran@gmail.com
"""

import asyncio

class similar_score:
    def __init__(self):
        pass

    async def url_similarity_score(self, url1, url2):
        ''' calculat the similarity score of two urls

        a = y(A, B) / max(b(A),b(B))
        y(A,B) is the number if elements in common
        max(b(A), b(B)) is the maxmium of elements

        '''
        tasks = [
            self.split_url(url1),
            self.split_url(url2),
        ]
        results = await asyncio.gather(*tasks)

        com_eles = list(set(results[0]).intersection(results[1]))
        
        return round(len(com_eles)/max(len(results[0]), len(results[1])),2)


    async def split_url(self, url):
        '''
            split single url with . and /
        '''
    
        coms = []
        # split url by . and /
        url_coms = url.split(".")
        for com in url_coms:
            coms.extend(com.split("/"))
        # filter out blank string
        coms = [x for x in coms if x != '']
        return coms

