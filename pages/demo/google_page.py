from pages.demo.google_locators import *
from pages.web_elements import BaseElement, BasePage


class GooglePage(BasePage):

  def enter(self, url:str):
    self.driver.get(url)

  def submit_search_for(self, search_term:str):
    _ = BaseElement(self.driver)
    _.set_text(SEARCH_BAR_INPUT, search_term)
    _.enter_key_press(SEARCH_BAR_INPUT)

  def get_first_search_result_header_text(self):
    _ = BaseElement(self.driver)
    result = _.get_text(FIRST_SEARCH_RESULT_HEADER)
    return result
  