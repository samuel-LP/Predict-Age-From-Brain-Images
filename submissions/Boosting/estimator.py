from sklearn.base import TransformerMixin
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.base import BaseEstimator
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


class ROIsFeatureExtractor(BaseEstimator, TransformerMixin):
    """Select only the 284 ROIs features:"""
    def fit(self, X, y):
        return self

    def transform(self, X):
        return X[:, :142]


class VBMFeatureExtractor(BaseEstimator, TransformerMixin):
    """Select only the 284 ROIs features:"""
    def fit(self, X, y):
        return self

    def transform(self, X):
        return X[:, 284:]


def get_estimator():
    kernel = RBF(
        length_scale=[1] * 142)  # Ajustez la longueur de la liste selon le nombre de fonctionnalités dans vos données
    gpr = GaussianProcessRegressor(
        kernel=kernel,
        alpha=0.1441108530403702,
        n_restarts_optimizer=10,
        normalize_y=True,
        random_state=1)

    estimator = make_pipeline(ROIsFeatureExtractor(),
                              gpr
                              )
    return estimator