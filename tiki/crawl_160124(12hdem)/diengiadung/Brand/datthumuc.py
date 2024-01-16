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
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\lego",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\mevabe",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Mideer",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Moony",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Nifoki",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Nutricare",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Oreka_Montessori",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Pigeon",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\QMAN",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Song_An_Eco",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Tiasang",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\ViViToys",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Winfun",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Winwintoys",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Wonmom",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\AIN_Closet",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\anta",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Bee_Gee",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\BIGFOX",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Bitis",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\BK_TOTECH",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\catrio",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Chicco",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Duka",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\finish",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\HAKI",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Hando",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\KAVY",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Ku_Ku_Duckbill",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_160124(12hdem)\dochoi_mevabe\Brand\Kunkun_Kid",
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
