import six
from schematics.types import BaseType
from schematics.exceptions import ValidationError


class TupleType(BaseType):
  """
  Shematics custom tuple type.
  """
  def validate_tuple(self, value):
    if type(value) is not tuple:
      raise ValidationError('Type must be a tuple')


class BytesType(BaseType):
  """
  Schematics custom bytes type.
  """
  def validate_bytes(self, value):
    if type(value) is not bytes:
      raise ValidationError('Type must be a valid bytes format')


class LazyDictType(BaseType):
  """
  Typeless dict custom schematics type.
  """
  def validate_lazydicttype(self, value):
    if type(value) is not dict:
      raise ValidationError('Type must be a valid dict')


class LazyDictOrListType(BaseType):
  """
  Schematics type that accepts both dict or list.
  """
  def validate_lazydictorlist(self, value):
    if not type(value) in (dict, list):
      raise ValidationError('Type must be a valid dict or list')



class DynamicType(BaseType):
  """
  Schematics dynamic type to accept anything.
  """
  def validate_dynamic(self, value):
    pass
