from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime
import xlrd

# Create your views here.
@api_view()
def getFact(req):
    file = xlrd.open_workbook_xls("./facts.xls")
    sheet = file.sheet_by_index(0)
    today = str(datetime.today().date())
    s_date = date(2022, 2, 21)
    l_date = date(int(today[:4]), int(today[5:7]), int(today[8:]))
    ind = (l_date - s_date).days
    ind %= 100
    fact : str = sheet.cell_value(ind+1, 0)

    res = {
        "fact": fact.strip(),
        "date": today
    }
    return Response(data=res, status=status.HTTP_200_OK)
