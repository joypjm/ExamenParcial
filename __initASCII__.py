from myascii import get_ascii, get_binary, get_results 
import sys 

menu = int(input('Menú\n=====\n1. Character\n2. Word'))
if (menu==1): 
    char= input ('Enter a character: ')
    word= char 

elif (menu==2): 
    word= input('Enter a word: ')

else: 
    sys.exit ()

print ('Results\n=========')
results= get_results(word)
print ('Total: {0}'.format(results))
