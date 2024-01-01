import openpyxl
from pathlib import Path
import string
from openpyxl.styles import (
    Border, Side,
    Alignment, Font
)
from openpyxl.utils import get_column_letter

thin_border = Border(left=Side(border_style="thin"),
                     right=Side(border_style="thin"),
                     top=Side(border_style="thin"),
                     bottom=Side(border_style="thin"))

#  set columns width in sheet header
def set_column_widths(ws, columns_names, column_width):
    alphabet = string.ascii_uppercase
    for i in range(len(columns_names)):
        ws.column_dimensions[alphabet[i]].width = column_width[i]
        # I think it is not needed
        # if type(column_width) is list:
        #     ws.column_dimensions[alphabet[i]].width = column_width[i]
        # elif type(column_width) is tuple:
        #     ws.column_dimensions[alphabet[i]].width = column_width[i]
        ws.cell(row=1, column=i + 1).font = Font(color="FF0000", size=14, bold=True)
        ws.cell(row=1, column=i + 1).alignment = Alignment(horizontal='center')
        ws.cell(row=1, column=i + 1).border = thin_border

    write_column_headers(ws, columns_names)

# Write the column headers if sheet is empty
def write_column_headers(ws, columns_names):
    if ws.max_row == 1:
        for col_num, column in enumerate(columns_names, 1):
            cell = ws.cell(row=1, column=col_num)
            cell.value = column



def write_info_to_xlsx(image_name, destination, path_to_log_folder):
    columns_names = ['File Name',
                     'Tass-Photo',
                     'PhotoXpress',
                     'Kommersant', ]
    # Create the file if it doesn't exist yet
    file_path = f"{path_to_log_folder}/uploaded_files.xlsx"
    if not Path(file_path).is_file():
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'uploads'
        set_column_widths(ws, columns_names=columns_names,
                          column_width=[50,50,50,50])

        wb.save(f'{path_to_log_folder}/uploaded_files.xlsx')





    # check uploaded server


    # write image name to column

    # at first check file name in column, if it doesn't exist , write to new row

    # ws[f'{get_column_letter(1)}{row}'].font = Font(size=14, bold=True)
    # ws[f'{get_column_letter(1)}{row}'].alignment = Alignment(vertical='center')
    # ws[f'{get_column_letter(1)}{row}'].border = thin_border
    # ws[f'{get_column_letter(1)}{row}'].value = image_name

    # wb = openpyxl.load_workbook(file_path, read_only=False)




if __name__ == '__main__':
    write_info_to_xlsx('20230822EPAV3563.JPG',
                       'pavlenko.evgeniy@gmail.com@stringer.photoxpress.ru',
                       '/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/uploads_log')
