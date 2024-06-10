from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from Styles import THICK_BORDER, THIN_BORDER, GREEN_FILL, BLUE_FILL, YELLOW_FILL, RED_FILL
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from intangible_catalog import gen


def set_dim_holder(ws, start=1, end=50, width=2 * 1.35):
    dim_holder = DimensionHolder(worksheet=ws)
    for col in range(start, end):
        dim_holder[get_column_letter(col)] = ColumnDimension(ws, width=width, index=get_column_letter(col))

    return dim_holder


def place_story_on_sheet(stories_list, sheet, columns=[1, 19]):
    sheet.column_dimensions = set_dim_holder(ws=sheet)

    row = -9
    for i, story in enumerate(stories_list):
        # распределяем сторисы по двум колонкам
        if not i % 2:
            start_column = columns[0]
            row += 10
        else:
            start_column = columns[1]

        write_outline_border(sheet=sheet, start_row=row, start_column=start_column, size={'c': 17, 'r': 9})
        # Write cells for analyst, developer and tester estimates
        write_all_border(sheet=sheet, start_row=row + 3, start_column=start_column + 1,
                         size={'c': story.analyst_estimate, 'r': 1})
        write_all_border(sheet=sheet, start_row=row + 5, start_column=start_column + 1,
                         size={'c': story.dev_estimate, 'r': 1})
        write_all_border(sheet=sheet, start_row=row + 7, start_column=start_column + 1,
                         size={'c': story.test_estimate, 'r': 1})

        story_num_cell = sheet.cell(row=row, column=start_column)
        story_num_cell.value = story.letter_index + str(story.num)
        story_num_cell.alignment = Alignment(horizontal='center')
        story_num_cell.font = Font(bold=True, size=12)
        sheet.merge_cells(start_column=start_column, end_column=start_column + 2, start_row=row, end_row=row)

        price_cell = sheet.cell(row=row, column=start_column + 13)
        price_cell.value = '$' + str(story.price) if story.price else str(story.stability_score) + ' о.с.'
        price_cell.alignment = Alignment(horizontal='center')
        price_cell.font = Font(bold=True, size=12)
        sheet.merge_cells(start_column=start_column + 13, end_column=start_column + 16, start_row=row, end_row=row)

        title_cell = sheet.cell(row=row + 1, column=start_column + 1)
        title = ''
        match story.letter_index:
            case 'S':
                title = 'Стандарная история'
            case 'F':
                title = f'Крайний срок: {story.due_day} день'
            case 'I':
                title = next(gen)
            case 'E':
                title = f'Крайний срок: {story.due_day} день'

        title_cell.value = title
        title_cell.alignment = Alignment(horizontal='center')
        title_cell.font = Font(bold=True, size=12)
        sheet.merge_cells(start_column=start_column + 1, end_column=start_column + 15, start_row=row + 1,
                          end_row=row + 1)

        match story.letter_index:
            case 'S':
                fill = GREEN_FILL
            case 'F':
                fill = BLUE_FILL
            case 'I':
                fill = YELLOW_FILL
            case 'E':
                fill = RED_FILL
        color_cells(sheet=sheet, start_row=row, start_column=start_column, size={'c': 17, 'r': 9}, fill=fill)


def write_outline_border(sheet, start_row, start_column, size):
    stop_row = start_row + size['r']
    stop_column = start_column + size['c']
    for row in range(start_row, stop_row):
        for column in range(start_column, stop_column):
            left_side = THICK_BORDER if column == start_column else None
            right_side = THICK_BORDER if column == stop_column - 1 else None
            top_side = THICK_BORDER if row == start_row else None
            bottom_side = THICK_BORDER if row == stop_row - 1 else None
            sheet.cell(row=row, column=column).border = Border(left=left_side, right=right_side, top=top_side,
                                                               bottom=bottom_side)


def write_all_border(sheet, start_row, start_column, size):
    stop_row = start_row + size['r']
    stop_column = start_column + size['c']
    for row in range(start_row, stop_row):
        for column in range(start_column, stop_column):
            left_side = THIN_BORDER
            right_side = THIN_BORDER
            top_side = THIN_BORDER
            bottom_side = THIN_BORDER
            sheet.cell(row=row, column=column).border = Border(left=left_side, right=right_side, top=top_side,
                                                               bottom=bottom_side)


def color_cells(sheet, start_row, start_column, size, fill):
    stop_row = start_row + size['r']
    stop_column = start_column + size['c']
    for row in range(start_row, stop_row):
        for column in range(start_column, stop_column):
            sheet.cell(row=row, column=column).fill = fill
