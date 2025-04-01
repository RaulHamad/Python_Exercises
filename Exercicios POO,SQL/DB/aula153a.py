
import openpyxl

#fig =plt.subplot()
#fig.plot([1,2,3],[1,2,3])
#plt.show()



wb = openpyxl.Workbook("graficos.xlsx")
ws = wb.active
print(wb,ws)