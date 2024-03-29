import os

import pandas as pd
import numpy as np
import rampwf as rw
import os.path

from sklearn.model_selection import KFold

N_FOLDS = 5
problem_title = 'Predict age from brain grey matter (regression)'

_target_column_name = 'age'
# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_regression()
# An object implementing the workflow
workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.RMSE()#,
    #rw.score_types.RelativeRMSE(name='rel_rmse'),
]

def get_cv(X, y):
    cv_train = KFold(n_splits=N_FOLDS, shuffle=True, random_state=0)
    return cv_train.split(X, y)

def _read_data(path, dataset, datatype=['rois', 'vbm'], notebook = False):
    """ Read data.

    Parameters
    ----------
    path : str
        DESCRIPTION.
    dataset : str
        'train' or 'test'.
    datatype : [str, ]
        Data set type within 'rois', 'vbm', 'vbm3d' default is ['rois', 'vbm']
        which return a concatenation of rois and vbm data.

    Returns
    -------
    x_arr : array (n_samples, n_features)
        Input data.
    y_arr : array (n_samples, )
        target data.

    """
    # Read target
    if notebook :
        participants = pd.read_csv(f"../data/{dataset}_participants.csv")
    else :
        participants = pd.read_csv(f"./data/{dataset}_participants.csv")
    y_arr = participants[_target_column_name].values

    x_arr_l = []
    # Read ROIs
    if'rois' in datatype:
        if notebook :
            rois = pd.read_csv(f"../data/{dataset}_rois.csv")
        else :
            rois = pd.read_csv(f"./data/{dataset}_rois.csv")
        x_rois_arr = rois.loc[:, 'l3thVen_GM_Vol':]
        assert x_rois_arr.shape[1] == 284
        x_arr_l.append(x_rois_arr)

    # Read 3d images and mask
    if'vbm' in datatype:
        if notebook :
            imgs_arr_zip = np.load(f"../data/{dataset}_vbm.npz")
        else :
            imgs_arr_zip = np.load(f"./data/{dataset}_vbm.npz")
        x_img_arr = imgs_arr_zip['imgs_arr'].squeeze()
        mask_arr = imgs_arr_zip['mask_arr']
        x_img_arr = x_img_arr[:, mask_arr]
        x_arr_l.append(x_img_arr)

    x_arr = np.concatenate(x_arr_l, axis=1)

    if datatype == ['rois', 'vbm']:  # TODO: Remove this check
        assert np.all(x_arr[:, :284] == x_rois_arr)
        assert np.all(x_arr[:, 284:] == x_img_arr)

    return x_arr, y_arr


def get_train_data(notebook = False, path='.', datatype=['rois', 'vbm']):
    dataset = 'train'
    return _read_data(path, dataset, datatype, notebook)


def get_test_data(notebook = False, path='.', datatype=['rois', 'vbm']):
    dataset = 'test'
    return _read_data(path, dataset, datatype, notebook)



