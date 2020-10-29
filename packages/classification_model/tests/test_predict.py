from classification_model.predict import make_prediction
from classification_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv', label='test')
    single_test = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test)

    # Then
    assert subject is not None
    assert subject.get('predictions')[0] == 0
    assert isinstance(int(subject.get('predictions')[0]), int)


def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv', label='test')
    original_data_length = len(test_data)
    multiple_test = test_data

    # When
    subject = make_prediction(input_data=multiple_test)

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == 200

    # We expect no rows to be filtered out
    assert len(subject.get('predictions')) == original_data_length