import pytest

@pytest.fixture
def hello_world_fn():
  def fn():
    return 'hello world'
  return fn


@pytest.fixture
def greetings_fn():
  def fn(name):
    return 'hello %s' % name
  return fn


@pytest.fixture
def greetings_default_fn():
  def fn(name='nobody'):
    return 'hello %s' % name
  return fn


@pytest.fixture
def complex_fn():
  def fn(name, age=32, **kwargs):
    return '%s is %s years old and lives in %s' % (name, age, kwargs.get('country', 'nowhere'))
  return fn

