from sklearn.linear_model import LogisticRegression
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import RepeatedEditedNearestNeighbours

from classification_model.processing import preprocessors as pp
from classification_model.processing import features
from classification_model.config import config


price_pipe = Pipeline(
      [   
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS_WITH_NA)),
         
        ('numerical_inputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA)),
         
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=config.CATEGORICAL_VARS)),
         
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
         
        ('log_transformer',
            features.LogTransformer(variables=config.NUMERICALS_LOG_VARS)),
         
        ('scaler', MinMaxScaler()),

        ('RENN', RepeatedEditedNearestNeighbours()),

        ('linear_regression', LogisticRegression(solver='liblinear',class_weight={0: 1, 1: 1}, random_state=1, 
                                                 C= 1.623776739188721))

        
    ]
)
