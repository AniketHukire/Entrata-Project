import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    yield driver
    driver.quit()

def test_homepage_title(browser):
    browser.get("https://www.entrata.com/")
    assert browser.title == "Property Management Software | Entrata"

def test_navigation_to_features(browser):
    browser.get("https://www.entrata.com/")
    features_link = browser.find_element(By.XPATH, "//a[contains(text(),'Features')]")
    features_link.click()
    WebDriverWait(browser, 10).until(EC.title_contains("Features"))
    assert "Features" in browser.title

def test_search_functionality(browser):
    browser.get("https://www.entrata.com/")
    search_box = browser.find_element(By.ID, "search")
    search_box.send_keys("Property Management")
    search_box.submit()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Search Results')]")))
    assert "Search Results" in browser.title

