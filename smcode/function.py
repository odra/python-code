import types
import json
import inspect

import schematics
from schematics.models import Model
from schematics.types import IntType, StringType
from schematics.types.compound import ModelType

from smcode.helpers.schema import BytesType, TupleType, LazyDictType
from smcode import errors, helpers
from smcode.code import Code


class Function(Model):
  code = ModelType(Code, required=True)
  fglobals = LazyDictType(required=True)
  name = StringType()
  argdefs = TupleType()
  closure = TupleType()
  defaults = TupleType()

  def __init__(self, *args, **kwargs):
    super(Function, self).__init__(raw_data=kwargs)
    try:
      self.validate()
    except schematics.exceptions.ModelValidationError as err:
      raise errors.ValidationError(err.messages)
  
  def __call__(self, *args, **kwargs):
    return self.run(*args, **kwargs)

  def run(self, *args, **kwargs):
    fargs = [
      self.code.as_code(),
      self.fglobals
    ]
    if self.name is None:
      fargs.append(self.code.name)
    else:
      fargs.append(self.name)
    if self.defaults:
      fargs.append(self.defaults)
    fn = types.FunctionType(*fargs)
    return fn(*args, **kwargs)

  def as_dict(self):
    return {
      'code': self.code.as_dict(),
      'fglobals': self.fglobals,
      'name': self.name,
      'argdefs': self.argdefs,
      'closure': self.closure,
      'defaults': self.defaults
    }
