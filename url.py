 
import pyshorteners
def short(v): 
    shorternedurl= pyshorteners.Shortener()
    print(shorternedurl.tinyurl.short(v)) 


v=input("enter the url to shortern the url: ") 
short(v)