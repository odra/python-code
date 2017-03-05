from smcode.code import Code


def from_json(data):
  return Code.from_json(data)


def from_dict(data):
  return Code.from_dict(data)


def from_raw(*args):
  return Code(*args)
