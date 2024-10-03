from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get(PRODUCT_URL)

# price_dollar = driver.find_element(By.CLASS_NAME, value="offer-price")
# # price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}")
# # driver.close()
# driver.quit()
try:
    # Wait for the element to be present in the DOM and visible
    price_dollar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "a-span12"))
    )
    print(f"The price is {price_dollar.text}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()