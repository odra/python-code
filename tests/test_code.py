import json

import pytest

from smcode.code import Code
from smcode import errors, helpers


def test_code_with_error():
  with pytest.raises(errors.ValidationError) as err:
    Code()
  assert err.value.args
  assert err.value.messages


def test_simple_code(hello_world_fn):
  fn = hello_world_fn
  code = fn.__code__
  data = helpers.code.code_props(code, preffix=False)
  code = Code(**data)


def test_from_code(hello_world_fn):
  fn = hello_world_fn
  code = fn.__code__
  code = Code.from_code(code)


def test_from_fn(hello_world_fn):
  code = Code.from_fn(hello_world_fn)


def test_as_dict(hello_world_fn):
  code = Code.from_fn(hello_world_fn)
  data = code.as_dict()
  for (k, v) in data.items():
    assert v == getattr(code, k)  


def test_as_json(hello_world_fn):
  code = Code.from_fn(hello_world_fn)
  data = json.loads(code.as_json())
  data = helpers.code.pre_load(data)
  for (k, v) in data.items():
    assert v == getattr(code, k)


def test_as_code(hello_world_fn):
  code = Code.from_fn(hello_world_fn)
  co = code.as_code()
  for prop in dir(co):
    if not prop.startswith('co_'):
      continue
    assert getattr(co, prop) == getattr(code, prop.replace('co_', ''))
