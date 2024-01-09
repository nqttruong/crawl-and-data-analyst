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
n = 2
global title_li, link_li, numberofsales, review, price_li, location_li, discount_li
title_li, link_li, numberofsales, review, price_li, location_li, discount_li = [], [], [], [], [], [], []

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
    driver.get("https://www.lazada.vn/dien-thoai-di-dong/?spm=a2o4n.home-vn.6598063730.1.19053bdcW1D19K".format(n))
    sleep(6)

def loadMultiBrowsers(drivers_rx, n):
    for driver in drivers_rx:
        t = threading.Thread(target=loadMultiPages, args = (driver, n,))
        t.start()

def getData(driver):
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, ".RfADt [href]")
        print("Trang đã sẵn sàng!")
    except:
        print("Vui lòng thử lại")

    for i in elems:
        title_li.append(i.text)
        link_li.append(i.get_attribute('href'))

        # Truy cập từng trang sản phẩm để lấy thêm chi tiết
        # product_url = i.get_attribute('href')
        # driver.get(product_url)
        # sleep(3)

        for j in range(1, len(title_li) + 1):
            try:
                daban = driver.find_element(By.XPATH, f"(//div[@class='card-item'])[{j}]//div[2]//span[contains(@class, 'c3e8SH')]/span[1]/span[1]")
                numberofsales.append(daban.text)
            except NoSuchElementException:
                numberofsales.append("N/A")

            try:
                danhgia = driver.find_element(By.XPATH, f"(//div[@class='card-item'])[{j}]//div[2]//span[contains(@class, 'c3e8SH')]/div/span")
                review.append(danhgia.text)
            except NoSuchElementException:
                review.append("N/A")

        # Thêm logic để trích xuất thông tin bổ sung (điều chỉnh các chọn tự CSS phù hợp)
        try:
            price = driver.find_element(By.CSS_SELECTOR, ".aBrP0").text
        except NoSuchElementException:
            price = "N/A"

        try:
            location = driver.find_element(By.CSS_SELECTOR, "span.oa6ri").text
        except NoSuchElementException:
            location = "N/A"

        try:
            discount = driver.find_element(By.CSS_SELECTOR, ".WNoq3").text
        except NoSuchElementException:
            discount = "N/A"

        # Thêm thông tin đã trích xuất vào danh sách của bạn
        price_li.append(price)
        location_li.append(location)
        discount_li.append(discount)

    sleep(3)
    driver.close()
    print("Crawl hoàn tất!!! Đóng trình duyệt:\n ", driver)
    print("----------------")
    return title_li, link_li, price_li, location_li, discount_li, numberofsales, review




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
print(all2)

#return values
titles = all2[0]
links = all2[1]
prices = all2[2]
locations = all2[3]
discounts = all2[4]
numberofsales = all2[5]
reviews = all2[6]

title_li, link_li, price_li, location_li, discount_li, numberofsales, review


# Create DataFrame
df_final = pd.DataFrame({
    'Tensanpham': titles,
    'link': links,
    'Giasanpham': prices,
    'Giamgia': discounts,
    'Danhgia': reviews,
    'Diadiem': locations,
    'Daban': numberofsales
})

# Save to CSV
df_final.to_csv('tes_Lazada_{}Pages.csv'.format(n), index=False)

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

