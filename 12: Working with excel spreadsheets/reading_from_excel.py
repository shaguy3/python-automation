import openpyxl
import datetime
import time


def calc_work_hours():
    hour_sum = 0
    minute_sum = 0
    wb = openpyxl.load_workbook('December 2018.xlsx', data_only=True)
    for cell in wb.get_active_sheet()['E2': 'E19']:
        hour_sum += cell[0].value.hour
        minute_sum += cell[0].value.minute
    hour_sum += (minute_sum // 60)
    print(hour_sum, minute_sum % 60)


exec_start = datetime.datetime.now() + datetime.timedelta(seconds=10)

while datetime.datetime.now() < exec_start:
    time.sleep(1)

calc_work_hours()
