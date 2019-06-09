import sys
from getopt import getopt
from selenium import webdriver

SUPPORTED_BROWSERS  = ['chrome', 'firefox']
SUPPORTED_DRIVERS = SUPPORTED_BROWSERS

def requested_browsers():
  """
  Returns a list of browsers derived from the --browser flag set by command line
  Verifies that each requested browser is supported 
  """
  opts, _ = getopt(sys.argv[1:], 'm:n:vs', ['browser=', 'workers=', 'reruns=', 'env='])
  opts_dict = dict(opts)
  if '--browser' in opts_dict:
    browsers_requested = opts_dict['--browser'].split(':')
  else: 
    browsers_requested = ['chrome']
  for browser in browsers_requested:
    if browser not in SUPPORTED_BROWSERS:
      raise ValueError('-browser argument ' + browser + 'is not supported')
  return browsers_requested

def generate_driver(driver_type, env_config):
  if driver_type not in SUPPORTED_DRIVERS:
    raise ValueError('requested driver is not supported')
  driver = None
  if driver_type == 'chrome':
    chrome_options = webdriver.ChromeOptions()
    #add chrome options
    driver = webdriver.Chrome(options=chrome_options)
  elif driver_type == 'firefox':
    profile = webdriver.FirefoxProfile()
    #set firefox preference
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile())
  return driver


