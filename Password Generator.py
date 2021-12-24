#import string and random modules
import string
import random
#Contains both lowercase and uppercase letters
letters=string.ascii_letters
#Digits from 0 to 9
digits= string.digits
#Special Characters
punc= string.punctuation
#List containing all letters, digits and special characters
char=list(letters)+list(digits)+list(punc)
#Define a function to generate password
def passwordgen():
    #Shuffle the list
    random.shuffle(char)
    #Input of the length of password from the user
    lenpswd=input("Enter your desired password length: ")
    #Check if the user input is integer
    if lenpswd.isdigit()==True:
        #Check if the input is +ve integer
        if int(lenpswd)>0:
            #If input is +ve int print the password
            print("Your password is:\n"+"".join(char[0:int(lenpswd)]))
        #If input is 0 or -ve then invalid
        else:
            print('Invalid Input')
        #If input is not integer then invalid
    else:
        print('Invalid Input')
#Function Call
passwordgen()
