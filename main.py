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
from src.similarity import similar_score


asyncio.run(similar_score.url_similarity_score())


if __name__ == "__main__":
    # read data
    df = dd.read_csv("../data/referer/www.cebookss.com.csv")
    # build the pipeline
    # pipelines = 
