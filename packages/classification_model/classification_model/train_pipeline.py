import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import fbeta_score
import joblib

from classification_model import pipeline
from classification_model.config import config


def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = "classification_model.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print("saved pipeline")

def run_training():
    """Train the model."""

    # read training data
    data = pd.read_csv(config.DATASET_DIR / config.DATA_FILE)

    data[config.TARGET] = LabelEncoder().fit_transform(data[config.TARGET])

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.2,
        random_state=0,
        stratify=data[config.TARGET])

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


    pred = pipeline.price_pipe.predict(X_train[config.FEATURES])
    print('f2 train: %.2f' % fbeta_score(y_train, pred, beta=2))


if __name__ == '__main__':
    run_training()