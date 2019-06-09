import sys
import os
from getopt import getopt
import configurations.configurations as configurations

SUPPORTED_ENVIRONMENTS = ["demo", 'alpha', "delta"]

def get_environment():
  """
  Returns environment in the --env flag set on command line
  If no environment is requestedm select the environment form TEST_ENV environment variable
  Verifies that the requested environment is supported 
  This is returned as a tuple so it can be parametarized by pytest fixtures
  """
  opts, _ = getopt(sys.argv[1:], 'm:n:vs', ['browser=', 'workers=',
                                            'reruns=', 'env='])
  opts_dict = dict(opts)
  if '--env' in opts_dict:
    environment_requested = opts_dict['--env']
    if environment_requested not in SUPPORTED_ENVIRONMENTS:
      raise ValueError(environment_requested + ' argument is not one of supported environments')
  else:
    environment_requested = os.environ['TEST_ENV']
    if environment_requested not in SUPPORTED_ENVIRONMENTS:
      raise ValueError(environment_requested + ' argument is not one of supported environments')
  return [environment_requested]

def get_configuration(environment):
  current_config = configurations.DEFAULT
  if hasattr(configurations, environment.upper()):
    current_config.update(getattr(configurations, environment.upper()))
  else:
    raise ValueError('Test environment ' + environment + ' is not found in the configurations.py file')
  return current_config
