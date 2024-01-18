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
source_file = r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\tk_thoitrangnam_brand_npage.ipynb"

# Danh sách đường dẫn thư mục đích (nơi bạn muốn sao chép file đến)
destination_folders = [r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Jinrinteen",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Julido_Store",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\KHATOCO",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\LADOS",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\LAHstore",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\LienPhuong",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\N6",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\NIU24",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Novelty",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\NHUH20",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Owen",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\SLINEN",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\SOMIANTON",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\SZone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Titishop",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\VHL",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Viettien",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\VinhTien",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\VONESA",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Aligro",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Amazing",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\ARADO_FASHION",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Atlan",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Chandi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Doka",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\dokafashion",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Fasvin",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\Generos",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\thoitrangnam\brand\GOKING"
]



# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
