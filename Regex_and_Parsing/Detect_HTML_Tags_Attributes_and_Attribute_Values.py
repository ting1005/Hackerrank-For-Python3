# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for a in attrs: print('->',a[0], '>', a[1])

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for a in attrs: print('->',a[0], '>', a[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
