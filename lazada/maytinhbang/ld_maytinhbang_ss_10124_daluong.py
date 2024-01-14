import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
import pandas as pd
import threading
from queue import Queue

# ===============================Initial=======================================
n = 5
global title_li, price_li, link_li, discount_li, countReviews
title_li, price_li, link_li, discount_li, countReviews = [], [], [], [], []

# ===============================Define Logic==================================

def openMultiBrowsers(n):
    drivers = []
    for i in range(n):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        drivers.append(driver)
    return drivers

def loadMultiPages(driver, n):
    # for driver in drivers:
    driver.maximize_window()
    driver.get("https://www.lazada.vn/may-tinh-bang/poco--samsung/?page=19".format(n))
    sleep(6)

def loadMultiBrowsers(drivers_rx, n):
    for driver in drivers_rx:
        t = threading.Thread(target=loadMultiPages, args = (driver, n,))
        t.start()

def getData(driver):
    # ======================================  GET link/title
    elems = driver.find_elements(By.CSS_SELECTOR, ".RfADt [href]")

    for i in elems:
        title_li.append(i.text)
        link_li.append(i.get_attribute('href'))

        # Thêm logic để trích xuất thông tin bổ sung (điều chỉnh các chọn tự CSS phù hợp)
        try:
            price = driver.find_element(By.CSS_SELECTOR, ".aBrP0").text
        except NoSuchElementException:
            price = np.nan

        try:
            discount = driver.find_element(By.CSS_SELECTOR, ".WNoq3").text
        except NoSuchElementException:
            discount = np.nan

        # Lấy thông tin về số lượng đánh giá (countReviews)
        try:
            Reviews = driver.find_element(By.CSS_SELECTOR, "._6uN7R").text
        except NoSuchElementException:
            Reviews = np.nan

        # Thêm thông tin đã trích xuất vào danh sách của bạn
        price_li.append(price)
        discount_li.append(discount)
        countReviews.append(Reviews)

    # Tạo DataFrame theo thứ tự mong muốn
    return title_li, price_li, link_li, discount_li, countReviews

def runInParallel(func, drivers_rx):
    for driver in drivers_rx:  
        que = Queue()
        print("-------Running parallel---------")
        t1 = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(que, driver))
        t1.start()
    try:    
        ouput = que.get()
    except:
        ouput = [] 

    return ouput

# ===========================Run/Execute=======================================

drivers_r1 = openMultiBrowsers(n)
loadMultiBrowsers(drivers_r1, n)  
sleep(10)

# ===== GET link/title

all2 = runInParallel(getData, drivers_r1)

#return values
titles = all2[0]
prices = all2[1]
links = all2[2]
discounts = all2[3]
numberofsales = all2[4]



# Create DataFrame
df = pd.DataFrame({
    'title': title_li,
    'price': price_li,
    'link_item': link_li,
    'index_': np.arange(1, len(title_li) + 1),
    'Discount': discount_li,
    'countReviews': countReviews
})

# Save to CSV
df.to_csv('ld_maytinhbang_ss_10124.csv'.format(n), index=False)

# =============================================================================
# CONNECT TO SQL SERVER BY PYTHON
# =============================================================================
    
# import pandas as pd
# import pyodbc 

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-RFH0PE8\SQLEXPRESS;'
#                       'Database=Challenge;'
#                       'Trusted_Connection=yes;')

# # df = pd.read_sql_query('SELECT * FROM dbo.sales', conn)

# df_final.to_sql('titleLinkLazada_{}Pages'.format(n), conn, if_exists='append')

