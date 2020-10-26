import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from classification_model.processing.errors import InvalidModelInputError


# logarithm transformer
class LogTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables = None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> "LogTransformer":
        # to accomodate the pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        # check that the values are non-negative for log transform
        if not (X[self.variables] > 0).all().all():
            vars_ = self.variables[(X[self.variables] <= 0).any()]
            raise InvalidModelInputError(
                f"Variables contain zero or negative values, "
                f"can't apply log for vars: {vars_}"
            )

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X