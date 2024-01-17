# Đường dẫn cần thêm vào danh sách
duong_dan_moi = r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\tk_dienthoai_brand_npage.ipynb"

# Tách tên file từ đường dẫn
ten_file_moi = duong_dan_moi.split("\\")[-1]
duong_dan_list, ten_file_list = [], []

# Thêm đường dẫn và tên file mới vào danh sách
duong_dan_list.append(duong_dan_moi)
ten_file_list.append(ten_file_moi)

# In danh sách sau khi thêm đường dẫn mới
print(duong_dan_list)
print(ten_file_list)


# Tạo danh sách mới cho tên file
ten_file_list = []

# Thêm tên file mới vào danh sách
ten_file_list.append(ten_file_moi)

# In danh sách tên file
print(ten_file_list)
