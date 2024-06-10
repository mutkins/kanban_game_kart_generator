from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from tools import *
from Stories import Stories
workbook = Workbook()

sheet = workbook.active



stories = Stories()

stories.generate_u_stories(letter_index='S', count=50)
stories.generate_f_stories(letter_index='F', count=26)
stories.generate_i_stories(letter_index='I', count=14)
stories.generate_e_stories(letter_index='E', count=20)

for stories_list in stories.stories_list:
    sheet = workbook.create_sheet()
    place_story_on_sheet(stories_list=stories_list, sheet=sheet)

workbook.save("output.xlsx")
