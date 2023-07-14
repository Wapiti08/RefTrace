"""
@Description : 
@Author      : Newt Tan (Wapiti08)
@Time        : 2023/06/24 16:12
@File        : preprocess.py
@Contact     : tzrzhuoran@gmail.com
"""

import dask.dataframe as dd
from zat.log_to_dataframe import LogToDataFrame
from zat import dataframe_to_matrix

class propocesser:
    def __init__(self):
        pass

    def _extract_url(self):
        ''' divide according to users' IP address: 
        extract the referer field, host field, request url field
        
        '''
        pass


    def log_to_dataframe(log_file):
        # create a pandas dataframe from a zeek log
        log_to_df = LogToDataFrame()
        log_df = log_to_df.create_dataframe(log_file, ts_index=False)

        return log_df

    def log_to_matrix(log_dataframe):
        '''
        :param log_dataframe: the log pandas dataframe object
        :return: the matrix converted from log dataframe
        '''
        # DataFrameToMatrix here is used to handle the categorical data
        to_matrix = dataframe_to_matrix.DataFrameToMatrix()
        log_matrix = to_matrix.fit_transform(log_dataframe)

        return log_matrix