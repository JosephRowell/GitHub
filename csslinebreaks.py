##PyCSSTidy v.0.0

##Note. This does not work yet. I'm trying to get it to tidy up long
## horizontal CSS files by entering a new line after every '}' character.
## for example: p { text-align: left; margin: 20px;}.footer{text-align:center;
##the .footer would show up on the next line. See the CSS file for why I would
##find this program necessary

with open("css_25c284e666a0131ff03aede0585577c8.css", 'r') as f:
    f_content = f.read()

with open("css_25c284e666a0131ff03aede0585577c8.css", 'w') as f:
    for lines in f:
        if '}' in f_content:
            f.write('\n')
f.close()
