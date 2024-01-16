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
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Huawei",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Itel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Kindle",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Kobo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Massel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Masstel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Mobell",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Nokia",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Onyx Boox",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\OPPO",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Oukitel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Panasonic",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Realme",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Samsung",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\TCL",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Tecno",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Ulefone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Vankyo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Vivo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Vtel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Xiaomi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Yealink",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\ZTE",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Alcatel",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Apple",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Bphone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Cisco",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\China Mobile",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Forme",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dienthoai_maytinhbang\Brand\Grandstream"
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
