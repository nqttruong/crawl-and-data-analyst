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
source_file = r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\tk_dienthoai_brand_npage.ipynb"

# Danh sách đường dẫn thư mục đích (nơi bạn muốn sao chép file đến)
destination_folders = [
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Massel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Masstel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Mobell",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Nokia",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Onyx Boox",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\OPPO",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Oukitel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Panasonic",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Realme",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Samsung",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\TCL",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Tecno",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Ulefone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Vankyo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Vivo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Vtel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Xiaomi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Yealink",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\ZTE",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Alcatel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Apple",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Bphone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Cisco",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\China Mobile",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Forme",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Grandstream",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Huawei",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Itel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Kindle",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\dienthoai_maytinhbang\brand\Kobo",
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
