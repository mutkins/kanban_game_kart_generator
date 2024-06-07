from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from borders import THICK_BORDER, THIN_BORDER
from openpyxl.styles import Alignment
from openpyxl.styles import Font

def set_dim_holder(ws, start=1, end=50, width=2 * 1.35):
    dim_holder = DimensionHolder(worksheet=ws)
    for col in range(start, end):
        dim_holder[get_column_letter(col)] = ColumnDimension(ws, width=width, index=get_column_letter(col))

    return dim_holder


def place_story_on_sheet(stories_list, sheet):
    sheet.column_dimensions = set_dim_holder(ws=sheet)
    for i, story in enumerate(stories_list):
        row = 1 if i == 0 else i * 10 + 1
        write_outline_border(sheet=sheet, start_row=row, start_column=1, size={'c': 17, 'r': 9})
        # Write cells for analyst, developer and tester estimates
        write_all_border(sheet=sheet, start_row=row+3, start_column=2, size={'c': story.analyst_estimate, 'r': 1})
        write_all_border(sheet=sheet, start_row=row + 5, start_column=2, size={'c': story.dev_estimate, 'r': 1})
        write_all_border(sheet=sheet, start_row=row + 7, start_column=2, size={'c': story.test_estimate, 'r': 1})

        # Write border for story num
        # write_all_border(sheet=sheet, start_row=row+1, start_column=2, size={'c': 1, 'r': 1})

        story_num_cell = sheet.cell(row=row, column=1)
        story_num_cell.value = story.letter_index + str(story.num)
        story_num_cell.alignment = Alignment(horizontal='center')
        story_num_cell.font = Font(bold=True, size=12)

        price_cell = sheet.cell(row=row, column=14)
        price_cell.value = '$' + str(story.price)
        price_cell.alignment = Alignment(horizontal='center')
        price_cell.font = Font(bold=True, size=12)

        sheet.merge_cells(start_column=1, end_column=3, start_row=row, end_row=row)
        sheet.merge_cells(start_column=14, end_column=17, start_row=row, end_row=row)


def write_outline_border(sheet, start_row, start_column, size):
    stop_row = start_row + size['r']
    stop_column = start_column + size['c']
    for row in range(start_row, stop_row):
        for column in range(start_column, stop_column):
            left_side = THICK_BORDER if column == 1 else None
            right_side = THICK_BORDER if column == stop_column - 1 else None
            top_side = THICK_BORDER if row == start_row else None
            bottom_side = THICK_BORDER if row == stop_row - 1 else None
            sheet.cell(row=row, column=column).border = Border(left=left_side, right=right_side, top=top_side, bottom=bottom_side)


def write_all_border(sheet, start_row, start_column, size):
    stop_row = start_row + size['r']
    stop_column = start_column + size['c']
    for row in range(start_row, stop_row):
        for column in range(start_column, stop_column):
            left_side = THIN_BORDER
            right_side = THIN_BORDER
            top_side = THIN_BORDER
            bottom_side = THIN_BORDER
            sheet.cell(row=row, column=column).border = Border(left=left_side, right=right_side, top=top_side, bottom=bottom_side)