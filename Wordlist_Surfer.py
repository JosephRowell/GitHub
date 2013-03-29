##Wordlist_Surfer.py Written in Python v.3

##NOTE this version only checks one time. I need to fix that. ----
##def check(): ##Defines the function
##    password = input("Enter password ") ##whatever the user inputs becomes the variable
##    if password in open('results.txt').read(): ##If that word is in a file...
##        print("insecure") ##computer says "insecure"
##    else:
##        print("you rock")
##
##check() ##Calls function----------

##Upcoming versions:
##Use a while loop that
##loops back every time
##user supplies insecure password

##Wordlist Surfer v1.1! 
##Features: If you are terrible at picking passwords,
##This program gives you another opportunity to pick a better password

##Note. This version is 10x more awesome than the one above.

def check(): 
    password = input("Enter password: ")
    if password not in open('results.txt').read(): 
        print("win")
    else:
        print("Don't do that. try again")
        check()##Cool loopage going on.
check()

##Note. This version below does not work. The next big feature I'm going
## to have is file matching, so that way it matches a password list
##against this wordlist. I'm also going to make the concept
##of this more effective when I use an actual database, and have
##this written in PHP

##I know that this is filled with comments at the moment. I like to write them.

##def check(): 
##    password = input("Enter password: ")
##    again = input("How about another(Y/N)? ")
##    if password not in open('results.txt').read(): 
##        while again == Y:
##            check()
##            else:
##                print("only an idiot would do that, try again")
##                ##check()##Discovered such a seet loop!
##check()
