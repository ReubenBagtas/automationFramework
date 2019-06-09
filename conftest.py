import pytest
import utilities.helpers.config_helpers as config_helpers
import utilities.helpers.driver_helpers as driver_helpers

def pytest_addoption(parser):
  """Allow helpers access to the --browser command line option"""
  browsers_supported = ":".join(driver_helpers.SUPPORTED_BROWSERS)
  parser.addoption('--env', action='store',  metavar='NAME', help='only run tests matching the environment NAME.')
  parser.addoption('--browser', action='store', default='chrome', help='supported:' + browsers_supported)

@pytest.fixture(scope='session', params=config_helpers.get_environment())
def env_config(request):
  return config_helpers.get_configuration(request.param)

@pytest.fixture(params=driver_helpers.requested_browsers())
def driver(request, env_config):
  driver_instance = driver_helpers.generate_driver(request.param, env_config)
  yield driver_instance
  driver_instance.quit()

def pytest_runtest_setup(item):
  marked_environments = [mark.args[0] for mark in item.iter_markers(name='environment')]
  requested_enviroment = config_helpers.get_environment()
  #We can only possibly skip a test if it has a marked environment
  if marked_environments:
    if requested_environment[0] not in marked_environments:
        pytest.skip('This test requires an environment in ' + str(marked_environments) )
