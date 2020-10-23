import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from imblearn.pipeline import Pipeline

from classification_model.config import config

def load_dataset(*, file_name: str, label: str) -> pd.DataFrame:
    _data = pd.read_csv(f"{config.DATASET_DIR}/{file_name}")
    if label == "train" :
        _data[config.TARGET] = LabelEncoder().fit_transform(_data[config.TARGET])
    return _data

def save_testset(*, file_name: str, data: pd.DataFrame) -> None:
    _data = data.to_csv(f"{config.DATASET_DIR}/{file_name}", index=False)

def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = "classification_model.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print("saved pipeline")

def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = config.TRAINED_MODEL_DIR / file_name
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline

