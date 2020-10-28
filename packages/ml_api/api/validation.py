from marshmallow import Schema, fields
from marshmallow import ValidationError
import json
import typing as t

# class InvalidInputError(Exception):
#     """Invalid model input."""


class ClassificationDataRequestSchema(Schema):
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

def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
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

