from data2html import DView, DTable, DStack, DImage, DText

data = [
    {"title": "test", "url": "test", "label": "label"},
    {"title": "test", "url": "test", "label": "label"}
]

view = DView(title='test')

table = DTable()
table.add_col(DStack([
    DText("$[].title"),
    DImage("$[].url"),
]), title='query')

table.add_col(DText("$[].label"), title='label')

view.add(table)
view.add(table)

print(view)