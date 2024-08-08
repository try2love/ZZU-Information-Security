from random import sample
import openpyxl
from openpyxl.styles import Font, colors, Fill

def generateXlsx(num):
    for i in range(num):
        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]
        # 添加表头
        ws.append(['字段'+str(_) for _ in range(1,6)])
        # 添加随机数据
        for _ in range(10):
            ws.append(sample(range(10000), 5))
        wb.save(str(i)+'.xlsx')

def batchFormat(num):
    for i in range(num):
        fn = str(i)+'.xlsx'
        wb = openpyxl.load_workbook(fn)
        ws = wb.worksheets[0]
        for irow, row in enumerate(ws.rows, start=1):
            if irow == 1:
                # 表头加粗、黑体
                font = Font('黑体', bold=True)
            elif irow%2 == 0:
                # 偶数行红色，宋体
                font = Font('宋体', color=colors.RED)
            else:
                # 奇数行浅蓝色，宋体
                font = Font('宋体', color='00CCFF')
            for cell in row:
                cell.font = font
                # 偶数行添加背景填充色，从红到蓝渐变
                if irow%2 == 0:
                    cell.fill = openpyxl.styles.fills.GradientFill(stop=['FF0000', '0000FF'])
        # 另存为新文件
        wb.save('new'+fn)

generateXlsx(5)
batchFormat(5)
