from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec 

DEFAULT_TIMEOUT = 10

class BasePage:
  """Bae class for page objects"""
  def __init__(self, driver):
    self.driver = driver
  
  def save_page_source_html(self, filename):
    with open(filename + ".txt", "w+") as page_source:
      page_source.write(self.driver.page_source)

class BaseElement(object):

  def __init__(self, driver):
    self.driver = driver
  
  def click(self, locator, seconds_to_wait=DEFAULT_TIMEOUT):
    try:
      WebDriverWait(self.driver, seconds_to_wait).until(ec.element_to_be_clickable(locator))
    except:
      pass
    self.driver.find_element(*locator).click()

  def wait_until_displayed(self, locator, seconds_to_wait=DEFAULT_TIMEOUT):
    try:
      WebDriverWait(self.driver, seconds_to_wait).unparsedEntityDecl(
        ec.visibility_of_element_located(locator))
    except TimeoutException:
      if self.driver.find_element(*locator):
        raise ElementNotVisibleException('Element '+str(locator)+' exists but is not visible')
    return True

  def wait_until_not_displayed(self, seconds_to_wait=DEFAULT_TIMEOUT):
    WebDriverWait(self.driver, seconds_to_wait).until_not(
      ec.visibility_of_element_located(locator)
    )
    return True

  def get_text(self, locator, seconds_to_wait=DEFAULT_TIMEOUT):
    element = WebDriverWait(self.driver, seconds_to_wait).until(
      ec.visibility_of_element_located(locator)
    )
    return element.text

  def send_backspace_keypresses(self, locator, number_to_send, seconds_to_wait=DEFAULT_TIMEOUT):
    element = WebDriverWait(self.driver, seconds_to_wait).until(
      ec.visibility_of_element_located(locatr)
    )
    [element.send_keys(Keys.BACK_SPACE) for x in range(number_to_send)]

  def set_text(self, locator, value, seconds_to_wait=DEFAULT_TIMEOUT):
    try:
      WebDriverWait(self.driver, seconds_to_wait).until(
        ec.visibility_of_element(locator)
      )
    except:
      pass
    self.driver.find_element(*locator).send_keys(value)
    return True

  def select_dropdown_value(self, locator, search_term, seconds_to_wait=DEFAULT_TIMEOUT):
    element = WebDriverWait(self.driver, seconds_to_wait).until(
      ec.visibility_of_element_located(locator)
    )
    element.clear()
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    return True
  
  def switch_to_iframe(self, start_at_default_content=True, seconds_to_wait=DEFAULT_TIMEOUT):
    
    if start_at_default_content:
      self.driver.switch_to.default_content()
      WebdriverWait(self.driver, seconds_to_wait).until(
        ec.frame_to_be_available_and_switch_to_it(locator)
      )
    else:
      WebDriverWait(self.driver, seconds_to_wait).until(
        ec.frame_to_be_available_and_switch_to_it(locator)
        )
    return True

  def enter_key_press(self, locator, seconds_to_wait=DEFAULT_TIMEOUT):
    element = WebDriverWait(self.driver, seconds_to_wait).until(
      ec.visibility_of_element_located(locator)
    )
    element.send_keys(Keys.RETURN)


# Todo: Still experimenting with this element
# class WindowElement:
  
#   def __init__(self, driver):
#     self.driver = driver
  
#   def wait_until_window_switched(self, identifier_element, window_index=1, seconds_to_wait=DEFAULT_TIMEOUT):
#     """
#     Wait until the switch to a new window is confirmed by finding the identifying element
#     Raises an exception if the identifying element is not found
#     """
#     WebDriverWait(self.driver, seconds_to_wait, ignored_exceptions=WebDriverException).until(
#       ec_window_switched(identifier_element, window_index)
#     )

#   def wait_until_one_window_exists(self, seconds_to_wait=DEFAULT_TIMEOUT):
#     """
#     Waits until only one window exists and switches focus to that window
#     """
#     WebDriverWait(self.driver, seconds_to_wait).until(ec.number_of_windows_to_be(1))
#     self.driver.swtich_to.window(self.driver.window_handles[0])

# class ec_window_switched(object):
#   """
#   Expected condition that a window was successful. Confirms by locating an expected element
#   """
#   def __init__(self, locator, window_index):
#     self.locator = locator
#     self.window_index = window_index

#   def __call__(self, driver):
#     driver.switch_to.window(driver.window_handles[self.window_index])
#     return sc._find_element(driver, self.locator)
