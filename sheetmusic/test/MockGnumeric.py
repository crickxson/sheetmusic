class Workbook:
    sheets = (Sheet(), Sheet(), Sheet(), )

class Sheet:
    def cell_fetch(column, row):
        return Cell()

class Cell:
    def get_entered_text():
        return 'The entered text'

workbooks = lambda: (Workbook(),)

functions = {
    'sheet': (lambda range_ref: 1.0),
    'column': (),
    'row': (),
}
