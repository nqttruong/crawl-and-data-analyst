import shutil
import os

def copy_file_to_folders(source_file, destination_folders, num_copies):
    # Kiểm tra và tạo bản sao của file cho mỗi thư mục và số lượng bản sao cần tạo
    for destination_folder in destination_folders:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for i in range(num_copies):
            file_name = f"{os.path.splitext(os.path.basename(source_file))[0]}_{i+1}{os.path.splitext(source_file)[1]}"
            destination_path = os.path.join(destination_folder, file_name)

            shutil.copy2(source_file, destination_path)

# Đường dẫn file nguồn (file cần sao chép)
source_file = r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\tk_dienthoai_thuonghieu_npage.ipynb"

# Danh sách đường dẫn thư mục đích (nơi bạn muốn sao chép file đến)
destination_folders = [
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\KHANH_LINH_STYLE",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\LA_BELLE_STORE",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\LAHstore",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\LQ_luxury",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\LUPERI",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\lylylorem",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Miley_Lingerie",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\NIU24",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\NHUH20",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\OLV",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Song_An_Eco",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\VHL",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Vincy",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\VONESA",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Wannabe",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\ARCTIC HUNTER",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\ArcticHunter",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Atlan",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\B.Lingerie",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\BARE",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Baw",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\CCHAT CLOTHES",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\CHONMUA_365",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Dottie",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\ĐuiViet",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\GOKING",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Haint_Boutique",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\HoYang",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Jinrinteen",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnu\brand\Kun93",
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
