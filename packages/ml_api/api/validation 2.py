from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t

class InvalidInputError(Exception):
    """Invalid model input."""

class ClassificationDataRequestSchemaTest(Schema):
    checking_account = fields.Str()
    duration_in_month = fields.Integer()
    credit_history = fields.Str()
    purpose = fields.Str()
    credit_amount = fields.Integer()
    Savings_account_bonds = fields.Str()
    present_employment_since = fields.Str()
    rate_revenu = fields.Integer()
    personal_status_sex = fields.Str()
    debtors_guarantors = fields.Str()
    present_residence_since = fields.Integer()
    Property = fields.Str()
    age_years = fields.Integer()
    other_installment_plans = fields.Str()
    housing = fields.Str()
    Number_credits_bank = fields.Integer()
    job = fields.Str()
    Number_people_liable = fields.Integer()
    telephone = fields.Str()
    foreign_worker = fields.Str()


class ClassificationDataRequestSchema(Schema):
    checking_account = fields.Str()
    duration_in_month = fields.Integer()
    credit_history = fields.Str()
    purpose = fields.Str()
    Savings_account_bonds = fields.Str()
    present_employment_since = fields.Str()
    rate_revenu = fields.Integer()
    personal_status_sex = fields.Str()
    debtors_guarantors = fields.Str()
    Property = fields.Str()
    age_years = fields.Integer()
    other_installment_plans = fields.Str()
    housing = fields.Str()
    telephone = fields.Str()
    foreign_worker = fields.Str()

FEATURES = ['checking_account', 'duration_in_month', 'credit_history', 'purpose', 'Savings_account_bonds',
            'present_employment_since', 'rate_revenu', 'personal_status_sex', 'debtors_guarantors', 'Property',
            'age_years', 'other_installment_plans', 'housing', 'telephone', 'foreign_worker']



def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data, label):
    """Check prediction inputs against schema."""

    if label == 'test':
    # set many=True to allow passing in a list
        schema = ClassificationDataRequestSchemaTest(many=True)

    else:
        schema = ClassificationDataRequestSchema(many=True)


    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages


    if errors:
        validated_input = _filter_error_rows(errors=errors, validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors

