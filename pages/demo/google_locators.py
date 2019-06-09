from selenium.webdriver.common.by import By

SEARCH_BAR_INPUT = (By.XPATH, "//form//input[@name='q']")
FIRST_SEARCH_RESULT_HEADER = (By.XPATH, "//div[@class='srg']/div[1]//h3")