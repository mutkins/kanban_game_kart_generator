from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from tools import *
from Stories import Stories
workbook = Workbook()

sheet = workbook.active



stories = Stories()

stories.generate_u_stories(letter_index='S', count=50)
stories.generate_f_stories(letter_index='S', count=25)
stories.generate_i_stories(letter_index='S', count=10)
stories.generate_e_stories(letter_index='S', count=10)

place_story_on_sheet(stories_list=stories.stories_list[0], sheet=sheet)
#
# a = sheet.cell(row=1, column=1)
# a.border = Border(bottom=Side(style='thin', color='000000'), top=Side(style='thin', color='000000'), left=Side(style='thin', color='000000'), right=Side(style='thin', color='000000'))
# sheet.merge_cells(start_column=1, end_column=2, start_row=1, end_row=1)
workbook.save("output.xlsx")
