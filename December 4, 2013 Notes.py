#December 4, 2013 Notes
#accessing files
import urllibr.request #lets you get info from web
#combo of operations that perform retrievals
page = urllib.request.urlopen('http://www.google.com')
text = page.read()

text = text.decode('UTF-8') #unicode turns data into text

