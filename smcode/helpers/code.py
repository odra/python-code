import copy


_code_props = {
  'cellvars': (tuple, list),
  'code': (lambda s: s.encode('utf8'), lambda b: b.decode('utf8')),
  'consts': (tuple, list),
  'freevars': (tuple, list),
  'lnotab': (lambda s: s.encode('utf8'), lambda b: b.decode('utf8')),
  'names': (tuple, list),
  'varnames': (tuple, list)
}


def parse_field(key, value, mode='dumps'):
  if not key in _code_props or value is None:
    return value
  (loads_fn, dumps_fn) = _code_props[key]
  if mode == 'dumps':
    return dumps_fn(value)
  return loads_fn(value)


def format_prop(name, preffix=True):
  if preffix:
    return name
  return name.replace('co_', '')


def is_prop(name):
  return name.startswith('co_')


def code_props(code, preffix=True):
  return {format_prop(k, preffix):getattr(code, k) for k in dir(code) if is_prop(k)}


def pre_dump(data):
  return {k:parse_field(k, v) for (k,v) in copy.copy(data).items()}


def pre_load(data):
  return {k:parse_field(k, v, mode='loads') for (k,v) in copy.copy(data).items()}  
