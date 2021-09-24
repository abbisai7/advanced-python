#pip isntall openpyxl
import openpyxl
from openpyxl.chart import BarChart,Reference

wb= openpyxl.Workbook()
sheet = wb.active

for i in range(10):
    sheet.append([i])

values = Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)

chart = BarChart()
chart.add_data(values)
chart.title="BOA CHART"
chart.x_axis_title='XAXIS'
chart.y_axis_title='YAXIS'
sheet.add_chart(chart,'E2')
wb.save('barchart.xlsx')
print("Bar chart created in Excel.. kindly open and see.")