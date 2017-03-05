import json
import inspect

import pytest

from smcode.code import Code
from smcode.function import Function
from smcode import errors, helpers


def test_code_with_error():
  with pytest.raises(errors.ValidationError) as err:
    Function()
  assert err.value.args
  assert err.value.messages


def test_simple_fn(hello_world_fn):
  co = Code.from_fn(hello_world_fn)
  fn = Function(code=co, fglobals=globals())
  assert fn() == 'hello world'


def test_greetings_fn(greetings_fn):
  co = Code.from_fn(greetings_fn)
  fn = Function(code=co, fglobals=globals())
  assert fn('odra') == 'hello odra'


def test_greetings_default_fn(greetings_default_fn):
  co = Code.from_fn(greetings_default_fn)
  spec = inspect.getargspec(greetings_default_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn() == 'hello nobody'


def test_greetings_default_positional_fn(greetings_default_fn):
  co = Code.from_fn(greetings_default_fn)
  spec = inspect.getargspec(greetings_default_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn('bob') == 'hello bob'


def test_greetings_default_keyword_fn(greetings_default_fn):
  co = Code.from_fn(greetings_default_fn)
  spec = inspect.getargspec(greetings_default_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn(name='ted') == 'hello ted'


def test_complex_fn(complex_fn):
  co = Code.from_fn(complex_fn)
  spec = inspect.getargspec(complex_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn('odra', country='brazil') == 'odra is 32 years old and lives in brazil'


def test_complex_fn_no_kw(complex_fn):
  co = Code.from_fn(complex_fn)
  spec = inspect.getargspec(complex_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn('odra') == 'odra is 32 years old and lives in nowhere'


def test_complex_fn_arg(complex_fn):
  co = Code.from_fn(complex_fn)
  spec = inspect.getargspec(complex_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn('odra', 50) == 'odra is 50 years old and lives in nowhere'


def test_complex_fn_arg_oder(complex_fn):
  co = Code.from_fn(complex_fn)
  spec = inspect.getargspec(complex_fn)
  fn = Function(code=co, defaults=spec.defaults, fglobals=globals())
  assert fn('odra', country='anywhere', age=100) == 'odra is 100 years old and lives in anywhere'

