from data2html.theme import Theme

out = Theme().render(None, None)
with open("out.html", 'w') as f:
    f.write(out)