def pala(string):

    revstr = "" 
 
    #Iterate string with for loop 
    for i in string: 
        revstr = i + revstr 
    print("Original string : ", string)
    print("Reversed string : ", revstr) 
 
    if(string==revstr): 
        print("The string is a palindrome.") 
    else: 
        print("The string is not a palindrome.")
pala("dad")
pala("rodent")
pala("mom")
