import os

# Danh sách tên thư mục mới
danh_sach_ten_thu_muc = ["Samsung", "Xiaomi", "OPPO", "Masstel", "Panasonic", "Kindle", "Nokia", 
    "Oukitel", "Ulefone", "Apple", "Tecno", "Realme", "Vivo", "Itel", "Forme", 
    "Kobo", "Onyx Boox", "Mobell", "Yealink", "Cisco", "TCL", "Bphone", 
    "Grandstream", "Huawei", "Massel", "Vankyo", "Vtel", "ZTE", "Alcatel", 
    "China Mobile"]




# Đường dẫn hiện tại
duong_dan_hien_tai = os.getcwd()

# Lặp qua danh sách và tạo từng thư mục
for ten_thu_muc in danh_sach_ten_thu_muc:
    # Đường dẫn đầy đủ của thư mục mới
    duong_dan_moi = os.path.join(duong_dan_hien_tai, ten_thu_muc)

    # Kiểm tra xem thư mục đã tồn tại chưa
    if not os.path.exists(duong_dan_moi):
        # Tạo thư mục mới nếu chưa tồn tại
        os.makedirs(duong_dan_moi)
        print(f"Đã tạo thư mục mới: {duong_dan_moi}")
    else:
        print(f"Thư mục {duong_dan_moi} đã tồn tại.")
