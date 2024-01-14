import numpy as np
from selenium import webdriver
from time import sleep
#from selenium.webdriver. common.keys import Keys
import random
#from selenium.webdriver import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Declare browser
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--lang=en-US")

# Khởi tạo trình duyệt với các tùy chọn
driver = webdriver.Chrome(options=chrome_options)
 
# for j in range(47, 56):
driver.get("https://tiki.vn/dien-thoai-smartphone/c1795")                                                                                            
sleep(random.randint(5,10))
# ======================================  GET link/title
elems = driver.find_elements(By.CSS_SELECTOR, ".name")
title = [elem.text for elem in elems]

elem_link = driver.find_elements(By.CSS_SELECTOR, ".style__ProductLink-sc-7xd6qw-2.fHwskZ.product-item")
links = [elem.get_attribute('href') for elem in elem_link]

# ======================================  GET price
elems_price = driver.find_elements (By.CSS_SELECTOR, ".price-discount__price")
price = [elem_price.text for elem_price in elems_price]


df1 = pd.DataFrame(list(zip(title, price, links)), columns =['title', 'price', 'link_item'])
df1["index_"]=np.arange(1,len(df1) + 1)



# ======================================  GET discount
elems_discount = driver.find_elements (By.CSS_SELECTOR, ".price-discount__discount")
discount = [elem_discount.text for elem_discount in elems_discount]

if len(discount) == len(df1):
    df1["discount"] = discount
else:
    diff_length = len(df1) - len(discount)
    df1["discount"] = discount + [float('nan')] * diff_length if diff_length > 0 else discount[:len(df1)]

elems_sale = driver.find_elements(By.CSS_SELECTOR, ".style__StyledRatingList-sc-7xd6qw-6.eMNcac")
sale = [elem.text for elem in elems_sale]

if len(sale) == len(df1):
    df1["sales"] = sale
else:
    diff_length = len(df1) - len(sale)
    df1["sales"] = sale + [float('nan')] * diff_length if diff_length > 0 else sale[:len(df1)]

print("discount:", discount)
print("sales:", price)

df1
# brand, store = [], []

# for i in range(0, 51):
#     print(links[i])
#     driver.get(links[i])
    
#     wait = WebDriverWait(driver, 10)

#     elems_brand = driver.find_elements(By.CSS_SELECTOR, "a.pdp_details_view_brand")
#     elem_brand = [elem.text for elem in elems_brand]
    
#     # Gắn giá trị NaN nếu danh sách là rỗng
#     brand_value = elem_brand[0] if elem_brand else np.nan
#     brand.append(brand_value)

#     elems_store = driver.find_elements(By.CSS_SELECTOR, "SellerName__SellerNameStyled-sc-10q5b8s-0.jmFfcj")
#     elem_store = [elem.text for elem in elems_store]
    
#     # Gắn giá trị NaN nếu danh sách là rỗng
#     store_value = elem_store[0] if elem_store else np.nan
#     store.append(store_value)

# df1["Brand"] = brand
# df1["Store"] = store

# df1.to_csv('tk_dtsmartphone_10124_t1.csv', index=False, encoding='utf-8')


