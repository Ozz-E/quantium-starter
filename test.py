import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of your Dash app
APP_URL = "http://127.0.0.1:8050"  # Replace with your app's URL

@pytest.fixture
def driver():
    # Initialize a WebDriver (Chrome in this example)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def test_header_present(driver):
    driver.get(APP_URL)
    
    # Ensure the header is present
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header"))
    )
    assert header.text == "Sales Data Visualizer"

def test_visualization_present(driver):
    driver.get(APP_URL)
    
    # Ensure the visualization (Graph) is present
    visualization = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sales-chart"))
    )
    assert visualization is not None

def test_region_picker_present(driver):
    driver.get(APP_URL)
    
    # Ensure the region picker (RadioItems) is present
    region_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "region-filter"))
    )
    assert region_picker is not None

if __name__ == '__main__':
    pytest.main([__file__])
