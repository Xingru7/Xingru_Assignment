# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

# Clicking on Best Sellers in the navigation
best_sellers_link = driver.find_element("xpath", "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[2]")
best_sellers_link.click()

# Waiting for the Best Sellers page to load
time.sleep(5)

# Verifying that the Best Sellers page has loaded
assert "Best Sellers" in driver.title


# Finding the right arrow button to slide the product images to the right.
right_arrow_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[3]/a")
right_arrow_button.click()

# Waiting for the product image to slide to the right
time.sleep(5)


# Selecting a product of the bestsellers from the search results
best_seller_link = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li[2]/div[2]/div/a[1]/div/img")
# best_seller_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
best_seller_link.click()

# Waiting for the bestseller details page to load
time.sleep(5)

# Locating the detailed  product image element
image_element = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[5]/div[4]/div[3]/div[1]/div[1]/div/div/div/div[3]/ul/li[6]/span/span/span/input")

# Clicking on the image to view the details
image_element.click()

# Waiting for the details to load
time.sleep(5)



# Clicking on "Buy Now" button
buy_now_button = driver.find_element("id", "buy-now-button")
buy_now_button.click()

# Waiting for buying now to update
time.sleep(5)




# Closing the webdriver
driver.close()
