import re

print("Type in credit card number.")

creditcard=str(input())

# Remove hyphons to check total length based on numeric digits only
CCnumberlength=creditcard.replace("-","")

#check first number to match 4, 5 or 6 and that the number consists of four groups of four
#and that each group of four is either consecutive or seperated by a hyphon
match=re.search(r"^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$",str(creditcard))

# check for letters both capitals and lowercase
nomatch=re.search(r"[a-zA-z]",str(creditcard))

#Check for 4 consecutive numbers
con=re.search(r"(\d)\1{3,}",str(CCnumberlength))

if nomatch == None:
        if match != None:
                if len(creditcard.replace("-","")) == 16:
                        if match.group(0):
                                if con == None:
                                        print('Valid')
                                else:
                                        print('Invalid')
                        else:
                                print('Invalid')
                else:
                        print('Invalid')
        else:
                print('Invalid')
else:
        print('Invalid')