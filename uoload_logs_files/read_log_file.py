from glob import glob
from tools.xlsx_tool import write_info_to_xlsx


def read_file(path_to_file: str):
    with open(path_to_file, 'r') as text_file:
        lines = text_file.readlines()
    return lines[1:]


def scrap_data_from_line(line):
    list_from_line = line.split('\t')
    return list_from_line[4].split('/')


def main(path_to_log_folder: str, file_extension: str):
    # find all log files in folder
    files_list = find_all_log_files(path_to_log_folder, file_extension)

    for path_to_log_file in files_list:

        lines = read_file(path_to_log_file)
        for line in lines:
            uploud_info = scrap_data_from_line(line)
            image_name, destination = uploud_info[-1], uploud_info[0]
            print(f"file {image_name} uploaded to {destination}")
            write_info_to_xlsx(image_name, destination)


def find_all_log_files(path_to_log_folder: str, file_extension: str):
    files_list = glob(f'{path_to_log_folder}/*{file_extension}')
    return files_list


if __name__ == '__main__':
    # print(read_file('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log/upload-231220-0949-FTP.log')[0])
    # scrap_data_from_line(read_file('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log/upload-231220-0949-FTP.log')[0])
    main('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log', 'log')
    # main('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log/upload-231220-0949-FTP.log')  # 'pavlenko.evgeniy@gmail.com@stringer.photoxpress.ru'
    # main('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log/upload-231212-1319-FTP.log')  # kommersant   ftpphoto@ftp.kommersant.ru
    # main('/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log/upload-231206-0949-FTP.log')  # kommersant   ftpphoto@ftp.kommersant.ru  'ONLINE\\\\Freelancer@ftp.itar-tass.com'
    # /Users/evgeniy/Pictures/VueScan
