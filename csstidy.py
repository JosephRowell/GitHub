
## CSSTidy v. 1.0 Written in Python 3.2

def tidy():
    f = open('css_25c284e666a0131ff03aede0585577c8.css', 'r+')
    b = '}' + '\n'
    contents = f.read()
    print (contents, "\n")
    newcontents = contents.replace('}', b)
    print (newcontents)
    f.close()
tidy()
