import types
import json

import schematics
from schematics.models import Model
from schematics.types import IntType, StringType
from schematics.types.compound import ModelType

from smcode.helpers.schema import BytesType, TupleType, LazyDictType
from smcode import errors, helpers


class Code(Model):
  argcount = IntType(required=True, default=0)
  kwonlyargcount = IntType(default=0)
  cellvars = TupleType(required=True)
  code = BytesType(required=True)
  consts = TupleType(required=True)
  filename = StringType(required=True)
  firstlineno = IntType(required=True)
  flags = IntType(required=True)
  freevars = TupleType(required=True)
  lnotab = BytesType(required=True)
  name = StringType(required=True, default='<string>')
  names = TupleType(required=True)
  nlocals = IntType(required=True) 
  stacksize = IntType(required=True)
  varnames = TupleType(required=True)

  def __init__(self, *args, **kwargs):
    super(Code, self).__init__(raw_data=kwargs)
    try:
      self.validate()
    except schematics.exceptions.ModelValidationError as err:
      raise errors.ValidationError(err.messages)

  @classmethod
  def from_json(cls, data):
    return cls.from_dict(json.loads(data))
  
  @classmethod
  def from_code(cls, co):
    data = helpers.code.code_props(co, preffix=False)
    return cls(**data)

  @classmethod
  def from_fn(cls, fn):
    return cls.from_code(fn.__code__)

  def as_code(self):
    return types.CodeType(
      self.argcount,
      self.kwonlyargcount,
      self.nlocals,
      self.stacksize,
      self.flags,
      self.code,
      self.consts,
      self.names,
      self.varnames,
      self.filename,
      self.name,
      self.firstlineno,
      self.lnotab,
      self.freevars,
      self.cellvars
    )

  def as_json(self):
    return json.dumps(helpers.code.pre_dump(self.as_dict()))

  def as_dict(self, prepare=False):
    if not prepare:
      return {k:v for (k, v) in self.items()}
    return helpers.code.pre_dump({k:v for (k, v) in self.items()})


