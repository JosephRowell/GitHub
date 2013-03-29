## Lottery

import random
print ("QuickDraw Picker")

#def lottery(n=6, min_value=1, max_value=50):   ***Commented out for further investigation.***
 #   return [random.randint(min_value, max_value) for i in range(n)]


def lottery():                          # no parameters!
    lottoNumber1 = random.randint(1,80)
    print(lottoNumber1)
    lottoNumber2 = random.randint(1,80)
    print(lottoNumber2)
    lottoNumber3 = random.randint(1,80)
    print(lottoNumber3)
    lottoNumber4 = random.randint(1,80)
    print(lottoNumber4)
    lottoNumber5 = random.randint(1,80)
    print(lottoNumber5)
    lottoNumber6 = random.randint(1,80)
    print(lottoNumber6)
    lottoNumber7 = random.randint(1,80)
    print(lottoNumber7)
    lottoNumber8 = random.randint(1,80)
    print(lottoNumber8)
    lottoNumber9 = random.randint(1,80)
    print(lottoNumber9)
    lottoNumber10 = random.randint(1,80)
    
    return lottoNumber1,lottoNumber2,lottoNumber3,lottoNumber4,lottoNumber5,lottoNumber6,lottoNumber7, lottoNumber8, lottoNumber9, lottoNumber10
lottery()
##userChoice1 = int(input('Choose a number between 1 and 56: ')) #User input
##userChoice2 = int(input('Choose a number between 1 and 56: '))
##userChoice3 = int(input('Choose a number between 1 and 56: '))
##userChoice4 = int(input('Choose a number between 1 and 56: '))
##userChoice5 = int(input('Choose a number between 1 and 56: '))
##userChoice6 = int(input('Choose a number between 1 and 46: '))
##
##
##lottoNumber1, lottoNumber2, lottoNumber3, lottoNumber4, lottoNumber5, lottoNumber6 = lottery()
##
##if userChoice1 == lottoNumber1:
##    print('You win $1,000')
##else:
##    print('Spend your money on something else instead of buying stupid lotto tickets')
