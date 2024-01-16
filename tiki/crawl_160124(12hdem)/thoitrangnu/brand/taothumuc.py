import os

# Danh sách tên thư mục mới
danh_sach_ten_thu_muc = ["VONESA", "NIU24", "Jinrinteen", "Haint_Boutique", "Atlan", "ARCTIC HUNTER", 
    "NHUH20", "OLV", "LAHstore", "ĐuiViet", "Kun93", "LUPERI", "Miley_Lingerie", 
    "B.Lingerie", "ArcticHunter", "Dottie", "Baw", "BARE", "Wannabe", "LA_BELLE_STORE", 
    "VHL", "Song_An_Eco", "CCHAT CLOTHES", "Vincy", "GOKING", "HoYang", "CHONMUA_365", 
    "LQ_luxury", "KHANH_LINH_STYLE", "lylylorem"]




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
