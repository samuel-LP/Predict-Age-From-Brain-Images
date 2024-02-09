from sklearn.base import TransformerMixin
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.base import BaseEstimator
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
    estimator = make_pipeline(ROIsFeatureExtractor(),
                              StandardScaler(),
                              GradientBoostingRegressor(learning_rate = 0.01,
                                                        max_depth= 3,
                                                        n_estimators= 1000)
                              )
    return estimator