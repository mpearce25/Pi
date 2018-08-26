import sys

file = open('web.txt', 'r+')
filetext = file.read()
start = filetext.index("ngrok.io", 0, len(filetext)) - 9
url = filetext[start:start + 17]

html = open('CNAME','r+')
html.write(url)
html.close()
