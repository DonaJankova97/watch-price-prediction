from sklearn.base import BaseEstimator, TransformerMixin


class LowercaseTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for column in X.select_dtypes(include='object').columns:
            X[column] = X[column].str.lower()
        return X

