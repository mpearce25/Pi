import sys

file = open('web.txt', 'r+')
filetext = file.read()
start = filetext.index("ngrok.io", 0, len(filetext)) - 9
end = filetext.index('\"', start, start + 50)


heading1 = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta http-equiv=\'Refresh\' content=\"0;URL=\'https://"
url = filetext[start:end]
nocaching = "<meta http-equiv=\'cache-control\' content=\'no-cache\'/>"
endtags = "</head>\n\t<body>\n\t\thello world\n\t</body>\n</html>"

html = open('index.html','r+')
html.write('%s%s%s%s' % (heading1, url,"\'/.",endtags))
html.close()

