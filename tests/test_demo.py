import pytest
from pages.demo.google_page import GooglePage


class TestDemo:

  @pytest.mark.demo  
  def test_google_search_demo(self, driver, env_config):

    google_page = GooglePage(driver)
    google_page.enter(env_config['google-homepage'])

    search_term = 'Reuben Bagtas'
    google_page.submit_search_for(search_term)
    search_result = google_page.get_first_search_result_header_text()
    assert search_term in search_result, "Search term is not in search"