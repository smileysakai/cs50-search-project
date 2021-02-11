import webbrowser
import cgi, cgitb

def imgsearch(srchterm):
    return f"https://www.google.com/search?q={srchterm}&tbm=isch"

form = cgi.FieldStorage()
searchterm = form.getvalue('q')

#searchterm="test"

#webbrowser.open(imgsearch(searchterm))
print(searchterm)

input('Press ENTER to exit')