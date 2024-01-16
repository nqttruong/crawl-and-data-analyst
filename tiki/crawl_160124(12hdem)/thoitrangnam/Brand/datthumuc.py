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
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Generos",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\GOKING",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Jinrinteen",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Julido Store",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\KHATOCO",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\LADOS",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\LAHstore",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\LienPhuong",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\N6",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\NIU24",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Novelty",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\NHUH20",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Owen",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\SLINEN",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\SOMIANTON",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\SZone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Titishop",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\VHL",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Viettien",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\VinhTien",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\VONESA",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Aligro",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Amazing",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\ARADO FASHION",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Atlan",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Chandi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Doka",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\dokafashion",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\thoitrangnam\Brand\Fasvin",
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
