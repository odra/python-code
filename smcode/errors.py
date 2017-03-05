from schematics.exceptions import ModelValidationError


class BaseError(Exception):
  def __init__(self, message):
    super(BaseError, self).__init__(message)


class ValidationError(ModelValidationError, BaseError):
  def __init__(self, *args, **kwargs):
    super(ValidationError, self).__init__(*args, **kwargs)

