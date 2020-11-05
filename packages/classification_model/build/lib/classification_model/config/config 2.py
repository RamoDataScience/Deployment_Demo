import pathlib

import classification_model

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

PACKAGE_ROOT = pathlib.Path(classification_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
DATA_FILE = "german_columns.csv"
TESTING_DATA_FILE = "test.csv"
TARGET = 'customer_classification'

# all variables
All_VARS = ['checking_account', 'duration_in_month', 'credit_history', 'purpose', 'credit_amount', 'Savings_account_bonds',
            'present_employment_since', 'rate_revenu', 'personal_status_sex', 'debtors_guarantors', 'present_residence_since',
            'Property', 'age_years', 'other_installment_plans', 'housing', 'Number_credits_bank', 'job', 'Number_people_liable',
            'telephone' , 'foreign_worker']

# variables
FEATURES = ['checking_account', 'duration_in_month', 'credit_history', 'purpose', 'Savings_account_bonds',
            'present_employment_since', 'rate_revenu', 'personal_status_sex', 'debtors_guarantors', 'Property',
            'age_years', 'other_installment_plans', 'housing', 'telephone', 'foreign_worker']

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = []

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = []

# variables to log transform
NUMERICALS_LOG_VARS = []

# categorical variables to encode
CATEGORICAL_VARS = ['checking_account', 'credit_history', 'purpose', 'Savings_account_bonds',
                    'present_employment_since', 'personal_status_sex', 'debtors_guarantors',
                    'Property', 'other_installment_plans', 'housing', 'telephone', 'foreign_worker']

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]

PIPELINE_NAME = "classification_model"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
