import pandas as pd

import joblib
import config


def make_prediction(input_data):
    
    _pipe_price = joblib.load(filename=config.PIPELINE_NAME)
    results = _pipe_price.predict(input_data)

    return results
   
if __name__ == '__main__':
    
    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.metrics import fbeta_score

    data = pd.read_csv(config.TRAINING_DATA_FILE)

    data[config.TARGET] = LabelEncoder().fit_transform(data[config.TARGET])

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.2,
        random_state=0,
        stratify=data[config.TARGET])

    pred = make_prediction(X_test)
    
    # determine f2
    print('f2 test: %.2f' % fbeta_score(y_test, pred, beta=2)) 