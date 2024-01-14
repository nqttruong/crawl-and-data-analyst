import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading

# ===============================Initial=======================================
n = 5
global title_li, price_li, link_li, discount_li, countReviews
title_li, price_li, link_li, discount_li, countReviews = [], [], [], [], []

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


# ===============================Define Logic==================================

def getData(url):
    global title_li, price_li, link_li, discount_li, countReviews

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # ======================================  GET link/title
    elems = soup.select(".RfADt [href]")

    for i in elems:
        title_li.append(i.text)
        link_li.append(i['href'])

        # Thêm logic để trích xuất thông tin bổ sung (điều chỉnh các chọn tự CSS phù hợp)
        try:
            price = soup.select_one(".aBrP0").text
        except AttributeError:
            price = np.nan

        try:
            discount = soup.select_one(".WNoq3").text
        except AttributeError:
            discount = np.nan

        # Lấy thông tin về số lượng đánh giá (countReviews)
        try:
            Reviews = soup.select_one("._6uN7R").text
        except AttributeError:
            Reviews = np.nan

        # Thêm thông tin đã trích xuất vào danh sách của bạn
        price_li.append(price)
        discount_li.append(discount)
        countReviews.append(Reviews)

    # Tạo DataFrame theo thứ tự mong muốn
    return title_li, price_li, link_li, discount_li, countReviews

def runInParallel(func, urls):
    threads = []
    outputs = []

    for url in urls:
        output = func(url)
        outputs.append(output)

    return outputs

# ...

# ===========================Chạy/Thực hiện=======================================

urls = ["https://www.lazada.vn/may-tinh-bang/poco--samsung/?page={}".format(i) for i in range(1, n + 1)]

all2 = runInParallel(getData, urls)

# Kiểm tra nếu danh sách không trống trước khi truy cập các phần tử của nó
if all2:
    titles = all2[0]
    prices = all2[1]
    links = all2[2]
    discounts = all2[3]
    numberofsales = all2[4]
else:
    print("Lỗi: Danh sách 'all2' đang trống.")

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
df.to_csv('ld_maytinhbang_ss_10124.csv', index=False)
