import sys

file = open('web.txt', 'r+')
filetext = file.read()
start = filetext.index("ngrok.io", 0, len(filetext)) - 9
end = filetext.index('\"', start, start + 50)
url = filetext[start:end]
nocaching = "<meta http-equiv=\'cache-control\' content=\'no-cache\'/>"

html = open('index.html','r+')
html.write('%s%s%s' % ('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta http-equiv=\'Refresh\' content=\"0;URL=\'https://',url ,'\'\"\\>\n\t</head>\n\t<body>\n\t\thello world\n\t</body>\n</html>'))
html.close()

