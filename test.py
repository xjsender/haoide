import urllib.parse
from xml.sax.saxutils import unescape

name = "Custom%3A Sales Profile"
name = urllib.parse.unquote(unescape(name, {"&apos;": "'", "&quot;": '"'}))
print (name)