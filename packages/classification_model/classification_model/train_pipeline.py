from sklearn.model_selection import train_test_split
from sklearn.metrics import fbeta_score

from classification_model import pipeline
from classification_model.processing.data_management import load_dataset, save_pipeline, save_testset
from classification_model.config import config


def run_training():
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.DATA_FILE, label="train")

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.2,
        random_state=0,
        stratify=data[config.TARGET])

    save_testset(file_name=config.TESTING_DATA_FILE, data=X_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)

    save_pipeline(pipeline_to_persist=pipeline.price_pipe)

    pred = pipeline.price_pipe.predict(X_train[config.FEATURES])
    print('f2 train: %.2f' % fbeta_score(y_train, pred, beta=2))

    pred = pipeline.price_pipe.predict(X_test[config.FEATURES])
    print('f2 test: %.2f' % fbeta_score(y_test, pred, beta=2))


if __name__ == '__main__':
    run_training()