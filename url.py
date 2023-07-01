import pyshorteners

long_url = input("enter the url")

def shotner(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shotner(long_url)
