import inspect

from smcode.code import Code
from smcode.function import Function


def from_fn(fn, fn_globals=None):
  co = Code.from_fn(fn)
  spec = inspect.getargspec(fn)
  kw = {
    'code': co,
    'fglobals': {'__builtins__': globals()['__builtins__']}
  }
  if fn_globals:
    kw['fglobals'].update(**fn_globals)
  if spec.defaults:
    kw['defaults'] = spec.defaults
  return Function(**kw)


def from_code(code, fn_globals=None, defaults=None):
  co = Code.from_code(code)
  kw = {
    'code': co,
    'fglobals': {'__builtins__': globals()['__builtins__']}
  }
  if fn_globals:
    kw['fglobals'].update(**fn_globals)
  if defaults:
    kw['defaults'] = defaults
  return Function(**kw)
