from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get(PRODUCT_URL)
price_dollar = driver.find_element(By.CLASS_NAME, value="a-offscreen")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}")
# driver.close()
driver.quit()