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
#https://www.lazada.vn/may-tinh-bang/?spm=a2o4n.home-vn.6598063730.2.7d6a3bdcsPdPaK
#https://www.lazada.vn/laptop/
# Open URL 


for j in range(47, 56):
    driver.get("https://www.lazada.vn/dien-thoai-di-dong/?page={}&spm=a2o4n.home-vn.6598063730.1.19053bdcW1D19K".format(j))                                                                                            
    sleep(random.randint(5,10))
    # ======================================  GET link/title
    elems = driver.find_elements(By.CSS_SELECTOR, ".RfADt [href]")
    title = [elem.text for elem in elems]
    links = [elem.get_attribute('href') for elem in elems]

    # ======================================  GET price
    elems_price = driver.find_elements (By.CSS_SELECTOR, ".aBrP0")
    price = [elem_price.text for elem_price in elems_price]


    df1 = pd.DataFrame(list(zip(title, price, links)), columns =['title', 'price','link_item'])
    df1["index_"]=np.arange(1,len(df1) + 1)

    # ======================================  GET discount
    elems_discount = driver.find_elements (By.CSS_SELECTOR, ".WNoq3")
    discount = [elem_discount.text for elem_discount in elems_discount]
            
    df1["Discount"] = discount

    elems_countReviews = driver.find_elements(By.CSS_SELECTOR, "._6uN7R")
    countReviews = [elem.text for elem in elems_countReviews]

    df1["countReviews"] = countReviews


    brand, store = [], []

    for i in range(0, 40):
        driver.get(links[i])
        
        wait = WebDriverWait(driver, 10)

        elems_brand = driver.find_elements(By.CSS_SELECTOR, "a.pdp-link.pdp-link_size_s.pdp-link_theme_blue.pdp-product-brand__brand-link")
        elem_brand = [elem.text for elem in elems_brand]
        
        # Gắn giá trị NaN nếu danh sách là rỗng
        brand_value = elem_brand[0] if elem_brand else np.nan
        brand.append(brand_value)

        elems_store = driver.find_elements(By.CSS_SELECTOR, "a.pdp-link.pdp-link_size_l.pdp-link_theme_black.seller-name__detail-name")
        elem_store = [elem.text for elem in elems_store]
        
        # Gắn giá trị NaN nếu danh sách là rỗng
        store_value = elem_store[0] if elem_store else np.nan
        store.append(store_value)

    df1["Brand"] = brand
    df1["Store"] = store

    df1.to_csv('t{}_dtdd.csv'.format(j), index=False, encoding='utf-8')


