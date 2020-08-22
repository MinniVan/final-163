"""
Names: Van Tha Bik Lian
       Evelena Burunova

Date: 8/21
Mentor: Alex

This module implements all the necessary methods to create a class
that will represent the data that we want to analyze.
"""

import h5py
import pandas as pd


class Data:
    """
    Data is a class that represents a single file
    that will be analyzed in the program method
    """
    def __init__(self, file_name):
        """
        Intializes everything that is needed for the
        Data class, so that the Data class can be used
        and accessed by other programs. A LARGE file
        is processed using h5py, and the data is convered
        into a pandas DataFrame
        """
        _data = h5py.File(file_name, 'r+')
        _tree_array = _data['t_allpar_new'][()]
        _data_df = pd.DataFrame(_tree_array)
        self._filtered_data = _data_df.drop_duplicates(subset=[('j_index')
                                                       or ('index')])

        self._array_keys = _tree_array.dtype.names

    def get_data_df(self):
        """
        Returns the full data represented by the Data class
        as a Pandas DataFrame
        """
        return self._filtered_data

    def get_high_features(self):
        """
        Returns a list of all the high level feature names,
        as labeled on the data
        """
        feats_filter = [i for i in self._array_keys if (i[0:2] == 'j_')]
        hl_features = feats_filter[:-7]
        result = dict()
        for feat in hl_features:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())

    def get_low_features(self):
        """
        Returns a list of all the low level feature names,
        as labeled on the data represented by the Data
        class
        """
        ll_features = [i for i in self._array_keys if (i[0:3] == 'j1_')]
        result = dict()
        for feat in ll_features:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())

    def get_labels_truth_table(self):
        """
        Returns a list of all the labels respresented in
        the Data class
        """
        labels = ['j_g', 'j_q', 'j_w', 'j_z', 'j_t', 'j_undef']
        result = dict()
        for feat in labels:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())
