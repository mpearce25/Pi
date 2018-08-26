import sys

file = open('web.txt', 'r+')
filetext = file.read()
start = filetext.index("ngrok.io", 0, len(filetext)) - 9
end = filetext.index('\"', start, start + 50) -1


heading1 = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta http-equiv=\'Refresh\' content=\"4; URL=\'https://"
url = filetext[start:end]
nocaching = "<meta http-equiv=\'cache-control\' content=\'no-cache\'>"
endtags = "\n\t</head>\n\t<body>\n\t\t<p>hello world</p>\n\t</body>\n</html>"

html = open('index.html','r+')
html.write('%s%s%s%s%s' % (heading1, url,"'\">\n\t\t", nocaching,endtags))
html.close()

