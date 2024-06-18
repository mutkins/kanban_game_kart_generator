from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder

from Troubles import Troubles
from tools import *
from Stories import Stories
workbook = Workbook()

sheet = workbook.active



stories = Stories()

stories.generate_u_stories(letter_index='S', count=50)
stories.generate_f_stories(letter_index='F', count=26)
stories.generate_o_stories(letter_index='O', count=14)
stories.generate_e_stories(letter_index='E', count=20)

for stories_list in stories.stories_list:
    sheet = workbook.create_sheet()
    place_story_on_sheet(stories_list=stories_list, sheet=sheet)

place_card_back(sheet=workbook.create_sheet(), color=MED_GREEN_FILL, count=50)
place_card_back(sheet=workbook.create_sheet(), color=MED_BLUE_FILL, count=26)
place_card_back(sheet=workbook.create_sheet(), color=MED_YELLOW_FILL, count=14)
place_card_back(sheet=workbook.create_sheet(), color=MED_RED_FILL, count=20)

troubles = Troubles()
troubles.generate_troubles(count=20, rate=0)
troubles.generate_troubles(count=14, rate=1)
troubles.generate_troubles(count=14, rate=2)
troubles.generate_troubles(count=14, rate=3)

for troubles_list in troubles.troubles_list:
    sheet = workbook.create_sheet()
    place_troubles_on_sheet(troubles_list=troubles_list, sheet=sheet)

place_card_back(sheet=workbook.create_sheet(), color=MED_BLACK_FILL, count=42)


workbook.save("output.xlsx")
