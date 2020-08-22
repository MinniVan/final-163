
import h5py
import pandas as pd

class Data:



    def __init__(self, file_name):
        _data = h5py.File(file_name, 'r+')
        _tree_array = _data['t_allpar_new'][()]

        _data_df = pd.DataFrame(_tree_array)
        self._filtered_data = _data_df.drop_duplicates(subset=[('j_index') or ('index')]) 

        self._array_keys = _tree_array.dtype.names

    def get_data_df(self):
        return self._filtered_data

    def get_high_features(self):
        feats_filter = [i for i in self._array_keys if (i[0:2] == 'j_')]
        hl_features = feats_filter[:-7]
        result = dict()
        for feat in hl_features:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())
    

    def get_low_features(self):
        ll_features = [i for i in self._array_keys if (i[0:3] == 'j1_')]
        result = dict()
        for feat in ll_features:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())


    def get_labels_truth_table(self):
        keys_filter = [i for i in self._array_keys if (i[0:2] == 'j_')]
        labels = ['j_g', 'j_q', 'j_w', 'j_z', 'j_t', 'j_undef']
        result = dict()
        for feat in labels:
            result[feat] = self._filtered_data[feat]
        return list(result.keys())
